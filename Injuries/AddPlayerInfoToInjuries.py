# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 16:06:31 2019

@author: nbatt
"""

import pandas as pd
import numpy as np
import os

#Read through each player's unpolished logs

os.chdir('C:/NBA DFS')
tmPace = pd.read_csv('TeamAdvanced.csv')
tmPace.set_index('Team',inplace=True)

os.chdir('C:/NBA DFS/Injuries/Unpolished Gamelogs')
logs = os.listdir('C:/NBA DFS/Injuries/Unpolished Gamelogs')
advanced = pd.read_csv('C:/NBA DFS/PlayerAdvanced.csv')
advanced['MPG'] = advanced['MP']/advanced['G']
advanced.set_index(['Player','Tm'],inplace=True)

injuredPlayers = []

for i in logs:
    
    df = pd.read_csv(i)
    
    if(len(df)==0):
        print(i)
    df = df.loc[df['Tm']!='Tm',:]
    
    #df = df.loc[df['G']!='G',:]
    df['DRB'] = pd.to_numeric(df['DRB'],errors='coerce')
    
    df['Play'] = df['DRB'].isna() 
    #np.issubdtype(df['DRB'].dtype, np.number)
    
    #noPlay = df.loc[df['Play']==True,:]
        
    consecGames = 0
    for ap in range(len(df)):
        
        if df['Play'].iloc[ap] == True:
            
            consecGames += 1
            
            if consecGames<=3 and (i[:-4],df['Tm'].iloc[ap]) in advanced.index:   
                 
                injuryLog = pd.read_csv('C:/NBA DFS/Injuries/InjuriesDF/'+df['Tm'].iloc[ap]+'/'+df['Date'].iloc[ap]+'.csv')                
                row = advanced.loc[(i[:-4],df['Tm'].iloc[ap]),['MPG','USG.','Pos']]
                pace = tmPace.loc[df['Tm'].iloc[ap],'PACE']
                
                injuryLog = injuryLog.append({'Player':i[:-4],'Min':row.iloc[0],'USG':row.iloc[1],'Pos':row.iloc[2],'Pace':pace},ignore_index=True)
                injuryLog.to_csv('C:/NBA DFS/Injuries/InjuriesDF/'+df['Tm'].iloc[ap]+'/'+df['Date'].iloc[ap]+'.csv',index=False)        
            
            elif (i[:-4],df['Tm'].iloc[ap]) in advanced.index:
                    
                injuryLog = pd.read_csv('C:/NBA DFS/Injuries/InjuriesDF/'+df['Tm'].iloc[ap]+'/'+df['Date'].iloc[ap]+'.csv')                
                row = advanced.loc[(i[:-4],df['Tm'].iloc[ap]),['MPG','USG.','Pos']]
                pace = tmPace.loc[df['Tm'].iloc[ap],'PACE']
                
                injuryLog = injuryLog.append({'Player':i[:-4],'Min':row.iloc[0],'USG':0,'Pos':row.iloc[2],'Pace':pace},ignore_index=True)
                injuryLog.to_csv('C:/NBA DFS/Injuries/InjuriesDF/'+df['Tm'].iloc[ap]+'/'+df['Date'].iloc[ap]+'.csv',index=False)
            
    
        else:
            consecGames = 0
        
        

#C:/NBA DFS/Injuries/InjuriesDF
#If player didn't play, get date and team he was on
#Go to that team's folder and get injury df file
#Insert his data there