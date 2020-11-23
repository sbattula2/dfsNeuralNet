# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:51:37 2019

@author: nbattpl
"""

import pandas as pd

gameLogs = pd.read_csv('MegGameLogs.csv')

playersAdvanced = pd.read_csv('PlayerAdvanced.csv')
playersAdvanced.set_index(['Player','Tm'],inplace=True)



# =============================================================================
# def f(x):
#     print(playersAdvanced.loc[(playersAdvanced['Player']==x[0])&(playersAdvanced['Tm']==x[1]),'USG.'].astype(float))
#     gameLogs.loc[(gameLogs['Player']==x[0])&(gameLogs['Tm']==x[1]),'USG'] = playersAdvanced.loc[(playersAdvanced['Player']==x[0])&(playersAdvanced['Tm']==x[1]),'USG.'].astype(float)
# def f(x):
# =============================================================================
def f(x):    
    print('hopzplkd')
    return playersAdvanced.loc[x,'USG.']

df3 = gameLogs[['Player','Tm']].apply(f)['Player']
gameLogs.set_index(['Player','Tm'],inplace=True)

# = ['None']*gameLogs.shape[0]
#add gametype to gamelogs

gameLogs['USG'] =df3
gameLogs['Playtype'] = gameLogs['PTS'].astype(int)//10
gameLogs['Playtype'] = gameLogs['Playtype']-1   
gameLogs.loc[gameLogs['Playtype']>6,'Playtype'] = 6
gameLogs.loc[gameLogs['Playtype']<0,'Playtype'] = 0

gameLogs.to_csv('MegGameLogs.csv')
