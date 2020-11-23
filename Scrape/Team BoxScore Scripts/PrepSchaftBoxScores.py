# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 12:46:05 2018

@author: nbatt
"""

#matplotlib inline
import pandas as pd

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
                        
#team_stats=team_stats[1:]

#teamID = pd.read_csv("C:/YDFS Project/Data Prep/Team Boxscores/ATL.csv")
teamID = pd.read_csv("C:/YDFS Project/Data Prep/TeamID.csv")



def addOpponentsAndDate(teamLog):
    opponents=[]
    dates=[]
    home=[]
    
    for i in range(teamLog.TEAM.size):
        
        #Add opponent
        opponents.append(teamLog.MATCHUP[i][len(teamLog.MATCHUP[i])-3:])
        
        #Add date
        dMonth=teamLog.DATE[i][0:2]
        dDate=teamLog.DATE[i][3:5]
        dYear=teamLog.DATE[i][6:]
        dates.append(dYear+"-"+dMonth+"-"+dDate) 
        
        #Add home bool
        if teamLog.MATCHUP[i][3]=="@":
            home.append(bool(False))
        else:
            home.append(bool(True))
    
    teamLog["OPP"]=opponents
    teamLog["DATE"]=dates
    teamLog["HOME"]=home
        
    teamLog = teamLog.drop('MATCHUP', 1)

    return teamLog

def GetOpponentStats(opponent,date):
   
    teamLogs = pd.read_csv("C:/YDFS Project/Data Prep/Team Boxscores/Cleaned/"+str(opponent)+"Cleaned.csv")
    
    for i in range(teamLogs.DATE.size):
        if teamLogs.DATE[i]==date:        
            gameRow = pd.DataFrame([{'FGA':teamLogs.FGA[i],'FTA':teamLogs.FTA[i],'OREB':teamLogs.OREB[i],
                          'DREB':teamLogs.DREB[i],'FGM':teamLogs.FGM[i],
                          'TOV':teamLogs.TOV[i],'PTS':teamLogs.PTS[i]}])
            return gameRow

def formatTable():
    
    for i in teamID.ABB:
        teamLogs = pd.read_csv("C:/YDFS Project/Data Prep/Team Boxscores/"+str(i)+".csv")
        teamLogs=addOpponentsAndDate(teamLogs) 
        teamLogs.to_csv("C:/YDFS Project/Data Prep/Team Boxscores/Cleaned/"+str(i)+"Cleaned.csv",sep=',')
    
    #Opp data to cleaned game logs
    for i in teamID.ABB:
        
        if (i!="u9h9"):
        
            teamLogs = pd.read_csv("C:/YDFS Project/Data Prep/Team Boxscores/Cleaned/"+str(i)+"Cleaned.csv")
            
            fga=[]
            fta=[]
            oreb=[]
            dreb=[]
            fgm=[]
            tov=[]
            pts=[]
            
            
            for j in range(teamLogs.DATE.size):
                 
                if(teamLogs.OPP[j]=="CHA"):
                    teamLogs.OPP[j]="CHO"
                
                if(teamLogs.TEAM[j]=="CHA"):
                    teamLogs.TEAM[j]="CHO"
                    
                if(teamLogs.OPP[j]=="PHX"):
                    teamLogs.OPP[j]="PHO"
                
                if(teamLogs.TEAM[j]=="PHX"):
                    teamLogs.TEAM[j]="PHO"
                    
                if(teamLogs.OPP[j]=="BKN"):
                    teamLogs.OPP[j]="BRK"
                
                if(teamLogs.TEAM[j]=="BKN"):
                    teamLogs.TEAM[j]="BRK"
                
                row = GetOpponentStats(teamLogs.OPP[j],teamLogs.DATE[j])
                
                print(teamLogs.OPP[j])
                print(teamLogs.DATE[j])
                print(row)
                
                fga.append(row.FGA[0])
                fta.append(row.FTA[0])
                oreb.append(row.OREB[0])
                dreb.append(row.DREB[0])
                fgm.append(row.FGM[0])
                tov.append(row.TOV[0])
                pts.append(row.PTS[0])
            
            teamLogs["OppFGA"]=fga
            teamLogs["OppFTA"]=fta
            teamLogs["OppOREB"]=oreb
            teamLogs["OppDREB"]=dreb
            teamLogs["OppFGM"]=fgm
            teamLogs["OppTOV"]=tov
            teamLogs["OppPTS"]=pts
            
            teamLogs.to_csv("C:/YDFS Project/Data Prep/Team Boxscores/Cleaned/"+str(i)+"Cleaned.csv",sep=',')

# =============================================================================
# offRating
# defRating
# for i in range(1,db.TEAM.size):
#     soFar = db.iloc[0:i]
#     
#     pointsScored = np.sum(soFar.PTS,axis=0)*100
#     totalPossCol = 0.96*soFar.FGA+soFar.TOV+0.44*soFar.FTA-soFar.OREB
#     totalPoss = np.sum(totalPossCol,axis=0)
#     
# 
# 
# 
# =============================================================================
