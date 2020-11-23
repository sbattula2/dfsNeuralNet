import pulp
from optimizer import Optimizer
import numpy as np

class Fanduel(Optimizer):
    """
    Fanduel Optimizer Settings
    Fanduel will inherit from the super class Optimizer
    """
    def __init__(self, num_lineups, overlap, solver, players_filepath, output_filepath):
        super().__init__(num_lineups, overlap, solver, players_filepath, output_filepath)
        self.salary_cap = 60000
        self.header = ['PG', 'PG', 'SG', 'SG', 'SF', 'SF', 'PF', 'PF', 'C']

    def type_1(self, lineups):
        """ 
        Sets up the pulp LP problem, adds all of the constraints and solves for the maximum value for each generated lineup.

        Type 1 constraints include:
            - 3-2 stacking (1 line of 3 players and one seperate line of 2 players)
            - goalies stacking
            - team stacking

        Returns a single lineup (i.e all of the players either set to 0 or 1) indicating if a player was included in a lineup or not.
        """
        #define the pulp object problem
        prob = pulp.LpProblem('NBA', pulp.LpMaximize)

        #define the player and goalie variables
        player_lineup = [pulp.LpVariable("player_{}".format(i+1), cat="Binary") for i in range(self.num_players)]
        
        #add the max player constraints
        prob += (pulp.lpSum(player_lineup[i] for i in range(self.num_players)) == 9)
        
        #add the positional constraints
        prob += (pulp.lpSum(self.positions['PG'][i]*player_lineup[i] for i in range(self.num_players)) == 2)
        prob += (pulp.lpSum(self.positions['SG'][i]*player_lineup[i] for i in range(self.num_players)) == 2)
        prob += (pulp.lpSum(self.positions['SF'][i]*player_lineup[i] for i in range(self.num_players)) == 2)
        prob += (pulp.lpSum(self.positions['PF'][i]*player_lineup[i] for i in range(self.num_players)) == 2)
        prob += (pulp.lpSum(self.positions['C'][i]*player_lineup[i] for i in range(self.num_players)) == 1)
        
        #add the salary constraint
        prob += (pulp.lpSum(self.players_df.loc[i, 'Salary']*player_lineup[i] for i in range(self.num_players))<= self.salary_cap)
        
        #variance constraints - each lineup can't have more than the num overlap of any combination of players in any previous lineups
        for i in range(len(lineups)):
           prob += ((pulp.lpSum(lineups[i][k]*player_lineup[k] for k in range(self.num_players)) <= self.overlap))
        
        #add the objective
        
        prob += pulp.lpSum(pulp.lpSum(self.players_df.loc[i, 'ExpectedGame']*player_lineup[i] for i in range(self.num_players)))
        
        #solve the problem
        status = prob.solve(self.solver)

        #check if the optimizer found an optimal solution
        if status != pulp.LpStatusOptimal:
            print('Only {} feasible lineups produced'.format(len(lineups)), '\n')
            return None

        # Puts the output of one lineup into a format that will be used later
        lineup_copy = []
        for i in range(self.num_players):
            if player_lineup[i].varValue >= 0.9 and player_lineup[i].varValue <= 1.1:
                lineup_copy.append(1)
            else:
                lineup_copy.append(0)
        return lineup_copy

    def fill_lineups(self, lineups):
        """ 
        Takes in the lineups with 1's and 0's indicating if the player is used in a lineup.
        Matches the player in the dataframe and replaces the value with their name.
        Adds up projected points and actual points (if provided) to save to each lineup.
        """
        filled_lineups = []
        for lineup in lineups:
            a_lineup = ["", "", "", "", "", "", "", "", ""]
            player_lineup = lineup[:self.num_players]
            total_proj = []

            for num, player in enumerate(player_lineup):
                if player > 0.9 and player < 1.1:
                    if self.positions['PG'][num] == 1:
                        if a_lineup[0] == "":
                            a_lineup[0] = self.players_df.loc[num, 'Player']
                        elif a_lineup[1] == "":
                            a_lineup[1] = self.players_df.loc[num, 'Player']
                    elif self.positions['SG'][num] == 1:
                        if a_lineup[2] == "":
                            a_lineup[2] = self.players_df.loc[num, 'Player']
                        elif a_lineup[3] == "":
                            a_lineup[3] = self.players_df.loc[num, 'Player']
                    elif self.positions['SF'][num] == 1:
                        if a_lineup[4] == "":
                            a_lineup[4] = self.players_df.loc[num, 'Player']
                        elif a_lineup[5] == "":
                            a_lineup[5] = self.players_df.loc[num, 'Player']
                    elif self.positions['PF'][num] == 1:
                        if a_lineup[6] == "":
                            a_lineup[6] = self.players_df.loc[num, 'Player']
                        elif a_lineup[7] == "":
                            a_lineup[7] = self.players_df.loc[num, 'Player']
                    elif self.positions['C'][num] == 1:
                        if a_lineup[8] == "":
                            a_lineup[8] = self.players_df.loc[num, 'Player']
                    total_proj.append(self.players_df.loc[num, 'Score'])
            a_lineup.append(round(sum(total_proj)-min(total_proj), 2))
            filled_lineups.append(a_lineup)
        return filled_lineups
