# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 08:23:52 2019

@author: nbatt
"""

import os
import pandas as pd
import numpy as np

gameLogs = pd.read_csv('MegGameLogs.csv')

os.chdir("C:/NBA DFS/Anthropomorphic")  
files = os.listdir('C:/NBA DFS/Anthropomorphic')
masterDF = pd.read_csv('ATL.csv',encoding='latin-1')
masterDF['TEAM'] = 'ATL'

for i in files:
    if i != 'ATL.csv':
        df = pd.read_csv(i,encoding='latin-1')
        df['TEAM'] = i[0:3]
        masterDF = masterDF.append(df)

#add minutes played to each player
masterDF.set_index('Player',inplace=True)
masterDF['MPG'] = [0]*masterDF.shape[0]

os.chdir("C:/NBA DFS/Game Logs")
gamelogFiles = os.listdir("C:/NBA DFS/Game Logs")
for i in gamelogFiles:
    masterDF.loc[str(i[:-4]),'MPG']= np.mean(gameLogs['MP'].loc[gameLogs['Player']==str(i[:-4])])


os.chdir("C:/NBA DFS")          



masterDF.to_csv('PlayerRolodex.csv',index=False)