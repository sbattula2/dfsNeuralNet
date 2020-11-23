# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 18:38:23 2019

@author: nbatt
"""
import pandas as pd
import numpy as np

def formatTable():
    
    teamID = pd.read_csv("C:/YDFS Project/Data Prep/TeamID.csv")
    for i in (teamID.ABB):
      
      soup=np.array([0])
      efgMean=np.array([0])
      teamLogs = pd.read_csv("C:/YDFS Project/Data Prep/Team Boxscores/Cleaned/"+str(i)+"Cleaned.csv")
      
      teamLogs["EFG"] = (teamLogs.FGM+teamLogs["3PM"]*0.5)/teamLogs.FGA
      
      for ik in range(1,teamLogs.DATE.size):
          soup = np.append(soup,np.mean(teamLogs["OppPTS"][0:ik]))
          efgMean = np.append(efgMean,np.mean(teamLogs["EFG"][0:ik])) 
      
      teamLogs["PPGAllowedSeasonAvg"]=soup
      teamLogs["EFGSeasonAvg"]=efgMean
        
      teamLogs.to_csv("C:/YDFS Project/Data Prep/Team Boxscores/Cleaned/"+str(i)+"Cleaned.csv",sep=',')
    
    
    
    
    for j in (teamID.ABB):
      
      efg3Game=np.array([0])
      
      teamLogs = pd.read_csv("C:/YDFS Project/Data Prep/Team Boxscores/Cleaned/"+str(j)+"Cleaned.csv")
    
      for ik in range(1,teamLogs.DATE.size):
          if ik < 3:
              efg3Game = np.append(efg3Game,np.mean(teamLogs["EFG"][0:ik]))
              
          else:
              efg3Game = np.append(efg3Game,np.mean(teamLogs["EFG"][ik-3:ik]))
      
      teamLogs["EFG3Game"]=efg3Game
        
      teamLogs.to_csv("C:/YDFS Project/Data Prep/Team Boxscores/Cleaned/"+str(j)+"Cleaned.csv",sep=',')
