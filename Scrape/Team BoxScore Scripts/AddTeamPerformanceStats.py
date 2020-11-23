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

# =============================================================================
# #Get 17-18 season
# browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div/label/select/option[2]').click()
# 
# #Get season type
# browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/label/select/option[2]').click()
# 
# #Get per game
# browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div/label/select/option[2]').click()
# 
# #Get season segment
# browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/div[1]/div[4]/div/div/label/select/option[2]').click()
# 
# =============================================================================

teamID = pd.read_csv("C:/YDFS Project/Data Prep/TeamID.csv")

def insertGameData(frame,columnField,newColName,numTimes):
    
    addendum=[]
    timesRan=0
    latest5 = []
    
    for i in range(frame[columnField].size):
        if timesRan<=numTimes-1:
            latest5.append((i))
            
            if timesRan>0:    
                addendum.append(getGameAvg(latest5,frame,columnField))
            
            else:
                addendum.append(0)                        
            
        else:
            
            #get FG and 3P of previous game to calc eFG
            try:
                val = getGameAvg(latest5,frame,columnField)    
                
            except:
                val = 0
            
            latest5.pop(0)
            latest5.append(i)
            
            addendum.append(val)
        
        timesRan+=1
    
    frame[newColName] = addendum    
    
def getGameAvg(indices,frame,columnField):
    
    avg = 0
    
    for i in indices:
        avg += float(frame[columnField][i])

    return avg/(len(indices))

def AddTS1Game(tmLog):
    ts=tmLog.PTS/(2*tmLog.FGA+0.44*tmLog.FTA)
    tmLog["TS%"]=ts
    tmLog["TS%1GAME"]=tmLog["TS%"].shift(1)
    
def Add1GameCol(tmLog,colName,newColName):
    tmLog[newColName]=tmLog[colName].shift(1)

def addForm(boxScore,numGames,newColName):    
    
    formList=[0]
    
    for blah in range(1,numGames):
        
        lastGames=np.array([])
        
        currentGame=blah
        
        for j in range(currentGame,0,-1):
            if boxScore.MOV[j]<0:
                lastGames = np.append(lastGames,-1)
            elif boxScore.MOV[j]>0:
                lastGames = np.append(lastGames,1)
            
        formList.append(np.sum(lastGames))
                      
    #print(boxScore.PTS.size)
    for i in range(numGames,boxScore.PTS.size):    
        
        lastGames=np.array([])
        
        currentGame=i
        
        for j in range(currentGame-1,currentGame-(numGames+1),-1):
            if boxScore.MOV[j]<0:
                lastGames = np.append(lastGames,-1)
            elif boxScore.MOV[j]>0:
                lastGames = np.append(lastGames,1)
        
        formList.append(np.sum(lastGames))
    
    boxScore[newColName]=formList
    
def addBoxScoreElement(teamID,boxScore,colName):
    
    1+1
    
def addPTDifferential(boxScore,numGames,newColName):    
    
    diffList=[0]
    
    for blah in range(1,numGames):
        
        lastGames=np.array([])
        
        currentGame=blah
        
        for j in range(currentGame,0,-1):
            lastGames = np.append(lastGames,boxScore.MOV[j])
            
        diffList.append(np.sum(lastGames))
                      
    #print(boxScore.PTS.size)
    for i in range(numGames,boxScore.PTS.size):    
        
        lastGames=np.array([])
        
        currentGame=i
        
        for j in range(currentGame-1,currentGame-(numGames+1),-1):
            lastGames = np.append(lastGames,boxScore.MOV[j])
            
        diffList.append(np.sum(lastGames))
    
    boxScore[newColName]=diffList


#Add Distance
def formatTable():
    for i in (teamID.ABB):
      
      teamLogs = pd.read_csv("C:/YDFS Project/Data Prep/Team Boxscores/Cleaned/"+str(i)+"Cleaned.csv")
      teamLogs["MOV"]=teamLogs.PTS-teamLogs.OppPTS
      
      AddTS1Game(teamLogs)
      
      Add1GameCol(teamLogs,"3P%","3P%1GAME")
        
      Add1GameCol(teamLogs,"PTS","PTS1GAME")
      
      Add1GameCol(teamLogs,"OppPTS","PTSALLOWED1GAME")
      
      insertGameData(teamLogs,"TS%","TS%5GAME",5)
      insertGameData(teamLogs,"3P%","3P%5GAME",5)
      insertGameData(teamLogs,"PTS","PTS5GAME",5)
      insertGameData(teamLogs,"OppPTS","PTSALLOWED5GAME",5)
      
      insertGameData(teamLogs,"TS%","TS%3GAME",3)
      insertGameData(teamLogs,"3P%","3P%3GAME",3)
      insertGameData(teamLogs,"PTS","PTS3GAME",3)
      insertGameData(teamLogs,"OppPTS","PTSALLOWED3GAME",3)
      
      addForm(teamLogs,1,"Form1Game")
      addForm(teamLogs,3,"Form3Game")
      addForm(teamLogs,5,"Form5Game")
      
      addPTDifferential(teamLogs,1,"PTDiff1Game")
      addPTDifferential(teamLogs,3,"PTDiff3Game")
      addPTDifferential(teamLogs,5,"PTDiff5Game")
      
      
      colNames = list(teamLogs)
      for ak in colNames:
          if ak[0:7]=='Unnamed':
              teamLogs=teamLogs.drop(ak,axis=1)
      
      teamLogs.to_csv("C:/YDFS Project/Data Prep/Team Boxscores/Cleaned/"+str(i)+"Cleaned.csv",sep=',')
    
      
#teamATL = pd.read_csv("C:/YDFS Project/Data Prep/Team Boxscores/Cleaned/ATLCleaned.csv")