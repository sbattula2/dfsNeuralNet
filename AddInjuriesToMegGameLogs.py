# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 18:42:24 2019

@author: nbatt
"""

import pandas as pd

injuries = pd.read_csv('InjuriesDF.csv')
injuries.set_index(['Date','Team'],inplace=True)

directory = pd.read_csv('PlayerDirectory.csv')
directory['Player'] = directory['Player'].str.replace('.','') 
directory.set_index('Player',inplace=True)

gameLogs = pd.read_csv('MegGameLogs.csv')
#gameLogs['Pos'] = gameLogs['Player'].apply(lambda x: directory.loc[x,'Pos'])
#gameLogs.to_csv('MegGameLogs.csv',index=False)

gameLogs['USGMIN'] = [None]*len(gameLogs)
gameLogs['USGMIN_COURT'] = [None]*len(gameLogs)
#gameLogs['USGMIN_POS'] = [None]*len(gameLogs)

pos = ['PG','SG','SF','PF','C']

for p in pos:
    df = gameLogs.loc[gameLogs['Pos']==p,:]
    df['USGMIN'] = df.apply(lambda x: injuries.loc[(x['Date'],x['Tm']),'USGMIN'],axis=1)
    
    if p in ['PF','C','SF']:
        df['USGMIN_COURT'] = df.apply(lambda x: injuries.loc[(x['Date'],x['Tm']),'FC'],axis=1)
        
    else:
        df['USGMIN_COURT'] = df.apply(lambda x: injuries.loc[(x['Date'],x['Tm']),'BC'],axis=1)
            
    gameLogs.loc[gameLogs['Player'].isin(df['Player']),'USGMIN'] = df['USGMIN']
    gameLogs.loc[gameLogs['Player'].isin(df['Player']),'USGMIN_COURT'] = df['USGMIN_COURT']

gameLogs.to_csv('MegGameLogs.csv')