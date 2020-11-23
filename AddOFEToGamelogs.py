# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 17:44:14 2019

@author: nbatt
"""

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt


teamID = pd.read_csv('TeamID.csv',index_col = 'ABB_NBA')
df = pd.read_csv('MegGameLogs.csv')
df['OFE'] = [None]*df.shape[0]

os.chdir('C:/NBA DFS/Opposition Touch Scoring')
teamTracking = pd.read_csv('TeamScoreTracking.csv')

playerTracking = pd.read_csv('PlayerTrackingShooting.csv')


#change player tracking names to fit game logs
#take out Jr. in the name
#take out the dots in all names

playerTracking['Player'] = playerTracking['Player'].str.replace(".","")
df['Player'] = df['Player'].str.replace(".","")
playerTracking['Player'] = playerTracking['Player'].str.replace(" Jr","")
playerTracking['Player'] = playerTracking['Player'].str.replace(" III","")
playerTracking['Player'] = playerTracking['Player'].str.replace(" II","")
playerTracking['Player'] = playerTracking['Player'].str.replace(" IV","")
playerTracking['Player'] = playerTracking['Player'].str.replace("Poeltl","Poltl")
playerTracking['Player'] = playerTracking['Player'].str.replace("Mitchell Creek","Mitch Creek")
playerTracking['Player'] = playerTracking['Player'].str.replace("Mo Bamba","Mohamed Bamba")
playerTracking['Player'] = playerTracking['Player'].str.replace("Juancho Hernangomez","Juan Hernangomez")
playerTracking['Player'] = playerTracking['Player'].str.replace("Vincent Edwards","Vince Edwards")
playerTracking['Player'] = playerTracking['Player'].str.replace("Nene","Nene Hilario")
playerTracking['Player'] = playerTracking['Player'].str.replace("Svi Mykhailiuk","Sviatoslav Mykhailiuk")
playerTracking['Player'] = playerTracking['Player'].str.replace("Taurean Prince","Taurean Waller-Prince")
playerTracking['Player'] = playerTracking['Player'].str.replace("Walter Lemon","Walt Lemon")
playerTracking['Player'] = playerTracking['Player'].str.replace("Wes Iwundu","Wesley Iwundu")

playerTracking.set_index('Player',inplace=True)
teamTracking['Team'] = teamTracking['Team'].apply(lambda x: teamID.loc[x,'ABB_REF'])
teamTracking.set_index('Team',inplace=True)

notFound = []
def f(x):
    teamStats = teamTracking.loc[x[1]]
    
    try:
        ofe = 0
        playerStats = playerTracking.loc[x[0]]
        for p in range(12,18):
            if(x[0]=='James Harden'):
                print(playerStats[p-11])
            ofe += teamStats[p]*playerStats[p-11]
        
        return ofe       

    except:
        if x[0] not in notFound:
            notFound.append(x[0])
            

    
    #ofe = playerTracking
    #return 
    
#go through each player in playertracking
#add percentile rankings to the teamtracking df

    
#get gamelog rows with the player
 
    
#soop = df[['Player','Opp']]
percColNames=[]
for q in range(0,6):
    percColNames.append(teamTracking.columns[q]+'PERCENTILE')
    teamTracking[teamTracking.columns[q]+'PERCENTILE'] = teamTracking[teamTracking.columns[q]].rank(pct=True)
    
df['OFE']=df[['Player','Opp']].apply(f,axis=1)
    
bins = [i for i in range(0,27)]
binWins = pd.Series([])

for q in bins:
    #add boom freq
    numBoomGames = df.loc[(df['OFE']>=q)&(df['OFE']<q+1)&(df['FPTS']>=40),'FPTS'].shape[0]
    numGames = df.loc[(df['OFE']>=q)&(df['OFE']<q+1),'FPTS'].shape[0]
    
    if numGames>0:
        binWins = binWins.append(pd.Series((numBoomGames/numGames)*100,index=[q]))
    else:
        binWins = binWins.append(pd.Series(0,index=[q]))

os.chdir('C:/NBA DFS')
df.set_index('Player',inplace=True)
df.to_csv('MegGameLogs.csv')

soop = df.loc['Kevin Huerter',['FPTS','Opp','OFE']]
soop['OfeRank'] = soop['OFE'].rank(ascending=False)


plt.scatter(df['OFE'],df['FPTS'], color='g',marker="o")

plt.xlabel('OFE')
plt.ylabel('FPTS')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()

