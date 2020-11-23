# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:41:45 2019

@author: nbatt
"""

import pandas as pd
import numpy as np
import os

gameLogs = pd.read_csv('MegGameLogs.csv')
gameLogs['STREAK'] = [None]*len(gameLogs)

#gameLogs.set_index('Player',inplace=True)
os.chdir('Injuries\\Unpolished Gamelogs')
files = os.listdir()

for i in files:
    print(i)
    df = pd.read_csv(i)
    df['FG.'] = pd.to_numeric(df['FG.'], errors='coerce')
    
    shootingAvg = np.mean(df['FG.'])
    df['FG.'] = df['FG.'].fillna(shootingAvg)
    df.set_index('Date',inplace=True)
    
    if 'Date' in df.index:
        df = df.drop(['Date'])
        
    df = df.loc[~df.index.duplicated(keep='last')]
    df['FG_Streak'] = (df['FG.'].shift(1) + df['FG.'].shift(2)) / 2
    df['FG_Streak'].iloc[0:2] = shootingAvg    
    df['FG_Streak'] = df['FG_Streak']/shootingAvg
    
    i = i.replace(".","")
    
    df2 = gameLogs.loc[gameLogs['Player']==i[:-3],:]
    df2.set_index('Date',inplace=True)    
    df2['STREAK'] = df['FG_Streak']
    
    df2.reset_index(inplace=True)
    
    df2.set_index(['Player','Date'],inplace=True)    
    gameLogs.set_index(['Player','Date'],inplace=True)    
    
    gameLogs.loc[df2.index,'STREAK'] = df2['STREAK']
    
    gameLogs.reset_index(inplace=True)
    
os.chdir(r'C:\NBA DFS')
gameLogs.to_csv('MegGameLogs.csv')