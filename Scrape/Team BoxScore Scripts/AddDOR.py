# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 18:36:37 2019

@author: nbatt
"""
import pandas as pd

def formatTable():
    teamID = pd.read_csv("C:/YDFS Project/Data Prep/TeamID.csv")
   
    for i in (teamID.ABB):
      teamLogs = pd.read_csv("C:/YDFS Project/Data Prep/Team Boxscores/Cleaned/"+str(i)+"Cleaned.csv")
      teamLogs['GOR']=addGamesOnRoad(teamLogs)
      #addDaysRest()
      teamLogs.to_csv("C:/YDFS Project/Data Prep/Team Boxscores/Cleaned/"+str(i)+"Cleaned.csv",sep=',')


def addGamesOnRoad(gameLogs):
    
    gOR = []
    for i in range(gameLogs['HOME'].size):
        gORNum = 0
        if not gameLogs['HOME'][i]:
            gORNum = 1
            for j in range(i-1,-1,-1):
                if not gameLogs['HOME'][j]:
                    gORNum+=1      
                else:
                    break
        gOR.append(gORNum)
    
    return gOR

