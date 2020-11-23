# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 18:44:24 2018

@author: nbatt
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 12:46:05 2018

@author: nbatt
"""

#matplotlib inline
import pandas as pd
import numpy as np

teamID = pd.read_csv("C:/YDFS Project/Data Prep/TeamID.csv")


def addBoxScoreElement(abb,boxScore,colName):
    
      
    for i in range(boxScore.DATE.size):
        date=boxScore.DATE[i]
    
        month=date[5:7]
        day=date[8:]
        year=date[0:4]
         
        fileName="AdvancedGame"+str(abb)+str(year)+str(month)+str(day)+"0.csv"  
        print(fileName)        
             
#Add Distance
for i in (teamID.ABB):
  
  teamLogs = pd.read_csv("C:/YDFS Project/Data Prep/Team Boxscores/Cleaned/"+str(i)+"Cleaned.csv")

  addBoxScoreElement(i,teamLogs,"Test")

  colNames = list(teamLogs)
  for ak in colNames:
      if ak[0:7]=='Unnamed':
          teamLogs=teamLogs.drop(ak,axis=1)
  
  teamLogs.to_csv("C:/YDFS Project/Data Prep/Team Boxscores/Cleaned/"+str(i)+"Cleaned.csv",sep=',')

  
teamATL = pd.read_csv("C:/YDFS Project/Data Prep/Team Boxscores/Cleaned/ATLCleaned.csv")