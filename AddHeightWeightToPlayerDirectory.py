# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:30:29 2019

@author: nbatt
"""

import pandas as pd
import numpy as np
import os

df = pd.read_csv('PlayerDirectory.csv')
os.chdir('C:/NBA DFS/Anthropomorphic')
files = os.listdir('C:/NBA DFS/Anthropomorphic')
#df.set_index('Player',inplace=True)

df['Height'] = [1]*df.shape[0]
df['Weight'] = [1]*df.shape[0]

for j in files:
    rosters = pd.read_csv(j)
    #rosters = rosters.set_index('Player')    
    for i in rosters['Player']:    
        df.loc[df['Player']==i,'Height'] = float(rosters.loc[rosters['Player']==i,'Ht'])
        df.loc[df['Player']==i,'Weight'] = float(rosters.loc[rosters['Player']==i,'Wt'])

df = df.loc[df['Tm']!='TOT']
os.chdir('C:/NBA DFS')
df.to_csv('PlayerDirectory.csv',index=False)