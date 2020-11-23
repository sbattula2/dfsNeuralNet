import pulp
from fanduel import Fanduel as NBAFanduel
import os
#from draftkings import Draftkings as NBADraftkings

os.chdir('C:/NBA DFS/lineupInputs')
files = os.listdir('C:/NBA DFS/lineupInputs')

for i in files:
    try:
        optimizer = NBAFanduel(num_lineups=40,
        						   overlap=4,
        						   solver=pulp.CPLEX_PY(msg=0),
        						   players_filepath = i,  
        						   output_filepath = 'C:/NBA DFS/lineupOutputs/'+i)
        #create the indicators used to set the constraints to be used by the formula
        optimizer.create_indicators()
        #generate the lineups with the formula and the indicators
        lineups = optimizer.generate_lineups(formula=optimizer.type_1)
        #fill the lineups with player names - send in the positions indicator
        filled_lineups = optimizer.fill_lineups(lineups)
        #save the lineups
        #optimizer.save_file(optimizer.header, filled_lineups)
        optimizer.save_file(optimizer.header, filled_lineups, show_proj=True)
        
    except:
        print(i+str('bad'))