# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 17:15:01 2019

@author: nbatt
"""

import os
import pandas as pd
import numpy as np

os.chdir('C:/NBA DFS/lineupInputs')
files = os.listdir('C:/NBA DFS/lineupInputs')

teamNames = np.array([])

for i in files:
    df = pd.read_csv(i)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df.to_csv(i)
    
    uniqTeams = df['Team'].unique().astype(str)
    #teamNames = np.append(teamNames,uniqTeams[uniqTeams not in teamNames].reshape(-1))
    for i in uniqTeams:
        if str(i) not in teamNames.astype(str):
            teamNames = np.append(teamNames,i)

    
os.chdir('C:/NBA DFS')
np.savetxt('FanduelTeamNames.csv',teamNames,delimiter=",",fmt='%s')