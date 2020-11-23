import sys
import csv
import pulp
import copy
import pandas as pd
from tqdm import tqdm

class Optimizer:
	"""
	Optimizer Base Class
	"""
	def __init__(self, num_lineups, overlap, solver, players_filepath, output_filepath):
		self.num_lineups = num_lineups
		self.overlap = overlap
		self.solver = solver
		self.players_df = self.load_inputs(players_filepath)
		self.num_players = len(self.players_df.index)
		self.output_filepath = output_filepath
		self.positions = {'C':[], 'SG':[], 'PG':[], 'SF':[], 'PF':[]}
		self.players_teams = []
		self.actuals = True if 'actual' in self.players_df else False

	def load_inputs(self, filepath):
		"""
		Returns the loaded data from the user filepath into a pandas dataframe.
		"""
		try:
			data = pd.read_csv(filepath)
		except IOError:
			sys.exit('INVALID FILEPATH: {}'.format(filepath))
		return data

	def save_file(self, header, filled_lineups, show_proj=False):
		"""
		Save the filled lineups to CSV.
		If show_proj is True the file will be saved with the projections
			and possibly the actual fantasy points if they exist.
		"""
		#Remove the projections and actuals if they exist to get lineups ready to upload to DK or FD
		header_copy = copy.deepcopy(header)
		output_projection_path = self.output_filepath.split('.')[0] + '.csv'
		if self.actuals:
			lineups_for_upload = [lineup[:-2] for lineup in filled_lineups]
			header_copy.extend(('P', 'A'))
		else:
			lineups_for_upload = [lineup[:-1] for lineup in filled_lineups]
			header_copy.extend(('P'))
		#save the file for upload
		if show_proj == False:
			with open(self.output_filepath, 'w') as f:
					writer = csv.writer(f)
					writer.writerow(header)
					writer.writerows(lineups_for_upload)
			print("Saved lineups for upload to: {}".format(self.output_filepath))
		elif show_proj == True:
			with open(output_projection_path, 'w') as f:
					writer = csv.writer(f)
					writer.writerow(header_copy)
					writer.writerows(filled_lineups)
			print("Saved lineups with projection to: {}".format(output_projection_path))

	def create_indicators(self):
		"""
		Preprocesses the data and classifies players into different indicators for constraints.
		The indicators are saved as class variables.
		"""
		teams = list(set(self.players_df['Team'].values))
		#self.num_teams = len(teams)

		#Create player position indicators so you know which position they are playing
		for pos in self.players_df.loc[:, 'Pos']:
			for key in self.positions:
				self.positions[key].append(1 if key in pos else 0)
		
		#Create player team indicators so you know which team they are on (for use in DK team constraint)
		for player_team in self.players_df.loc[:, 'Team']:
			self.players_teams.append([1 if player_team == team else 0 for team in teams])

	def generate_lineups(self, formula):
		"""
		Generate n lineups with the forumla's specified constraints.
		"""
		lineups = []
		for _ in tqdm(range(self.num_lineups)):
			lineup = formula(lineups)
			if lineup:
				lineups.append(lineup)
			else:
				break
		return lineups
