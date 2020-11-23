# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 20:23:41 2019

@author: nbatt
"""

import pandas as pd
import matplotlib as plt
import os
from scipy import stats
import numpy as np

players = pd.read_csv('PlayerDirectory.csv')
namEdits = pd.read_csv('Player Name Edits.csv')
#names = players.loc[players['Player'].isin(namEdits['BBREF']),'Player'].apply(lambda x: namEdits.loc[namEdits['BBREF'].str==x,'FANDUEL'])  
#players.loc[players['Player'].isin(namEdits['BBREF']),'Player'] = namEdits.loc[namEdits['BBREF'].isin(players['Player']),'FANDUEL']

#players.set_index('Player',inplace=True)
for i in namEdits['BBREF']:
    players.loc[players['Player']==i,'Player'] = namEdits.loc[namEdits['BBREF']==i,'FANDUEL'].iloc[0]
    #players['Player'].str.replace(i,namEdits.loc[namEdits['BBREF']==i,'FANDUEL'].iloc[0])

players.set_index('Player',inplace=True)
os.chdir('lineupOutputs')
files = os.listdir()

def f(x):
    try:
        return players.loc[x,'CLUSTER'].iloc[0]
    except:
        return np.nan

clusterCounts = pd.DataFrame({})    
for qo in range(0,10):
    clusterCounts['CLUSTER'+str(qo)] = [None]*len(clusterCounts)

for i in files:
    print(i)
    df = pd.read_csv(i)
    df['PERC'] = df['P'].apply(lambda x: stats.percentileofscore(df['P'],x))
    
    good = df.loc[df['PERC']>=85,:]
    
    players = []
    clusters = []
    
    row = {}
    
    for qo in range(0,10):
        players.append(good[good.columns[qo]])
    
    for qo in players:
        try:
            clusters.append(players.loc[qo,'CLUSTER']).iloc[0]
        