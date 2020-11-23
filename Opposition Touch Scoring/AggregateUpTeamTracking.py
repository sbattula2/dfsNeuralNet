# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 17:48:16 2019

@author: nbatt
"""

import pandas as pd
import os

os.chdir('C:/NBA DFS/Opposition Touch Scoring/Team Tracking')
files = os.listdir('C:/NBA DFS/Opposition Touch Scoring/Team Tracking')

team_stats = [None]*30

db = pd.DataFrame({'Team': team_stats
                   ,'DRIVEPTS': team_stats
                   ,'CSPTS': team_stats
                   ,'PULLPTS': team_stats
                   ,'PAINTPTS': team_stats
                   ,'POSTPTS': team_stats
                   ,'ELBOWPTS': team_stats
                   ,'DRIVEPTS%': team_stats
                   ,'CSPTS%': team_stats
                   ,'PULLPTS%': team_stats
                   ,'PAINTPTS%': team_stats
                   ,'POSTPTS%': team_stats
                   ,'ELBOWPTS%': team_stats
                   })

db['Team'] = files
db['Team'] = db['Team'].str[:-4]
db.set_index('Team',inplace=True)

for i in files:
    df = pd.read_csv(i)
    soop = (df.describe())
    db.loc[i[:-4]] = soop.loc['mean'][1:].astype(float)
    
db.to_csv('C:/NBA DFS/Opposition Touch Scoring/TeamScoreTracking.csv')