# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:01:51 2019

@author: nbatt
"""

import pandas as pd
import calendar
import numpy as np
import os

names = pd.read_csv('Player Name Edits.csv')
#names.set_index('BBREF',inplace=True)

gameLogs = pd.read_csv('MegGameLogs.csv')

#change gamelogs dates to file date format

gameLogs['Date'] = gameLogs['Date'].apply(lambda x: calendar.month_abbr[int(x[5:7])]+'_'+str(x[-2:])+'_'+str(x[:4]))
gameLogs.loc[(gameLogs['Date'].str[4]=='0'),'Date'] = gameLogs['Date'].str[:4]+gameLogs['Date'].str[5:]

#gameLogs.set_index('Player',inplace=True)
#gameLogs.loc[gameLogs['Player'].isin(names['BBREF']),'Player'] = gameLogs['Player'].map({True})

soop = None

for q in names['BBREF']:
    soop = names.loc[names['BBREF']==q,'FANDUEL']
    gameLogs.loc[gameLogs['Player']==q,'Player'] = names.loc[names['BBREF']==q,'FANDUEL'].iloc[0]

#gameLogs['Player'] = gameLogs['Player'].apply(lambda x: names.loc[names['BBREF']==x,'FANDUEL'])
#gameLogs.set_index(['Player','Date'],inplace=True)
gameLogs['Player'] = gameLogs['Player'].str.replace('.','')

os.chdir('C:/NBA DFS/lineupInputs')
files = os.listdir('C:/NBA DFS/lineupInputs')

notFound = pd.DataFrame({'Player':[],'Date':[],'Score':[]})

for i in files:
    
    gameLogsToday = gameLogs.loc[(gameLogs['Date']==i[:-4]),:]
    gameLogsToday.set_index('Player',inplace=True)
    
    df  = pd.read_csv(i)
    df['Player'] = df['Player'].str.replace('.','')

    df['ExpectedGame'] = [0]*len(df)
    
    for ij in df['Player']:
        #df.loc[df['Player']==ij,'ExpectedGame'] = gameLogs.loc[ij,'ExpectedGame'].iloc[0]
        try:
            df.loc[df['Player']==ij,'ExpectedGame'] = gameLogsToday.loc[ij,'ExpectedGame']
        except:
            1+1
# =============================================================================
#             score = df.loc[df['Player']==ij,'FPTS'].iloc[0]
#             if (ij not in notFound) and (score!=0):
#                 notFound = notFound.append({'Player':ij,'Date':i,'Score':score},ignore_index=True)
#     
# =============================================================================
    df['ExpectedGame'] = np.around(df['ExpectedGame'],decimals=1)
    df = df.fillna(-1)
    df.to_csv(i,index=False)