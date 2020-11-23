import numpy as np
import pandas as pd
import os



teamID=pd.read_csv("C:/YDFS Project/Data Prep/TeamID.csv")    
os.chdir('C:\YDFS Project\Data Prep\Team Boxscores\Cleaned')

hmm=None

def removeDashes(date):
    trunc=""
    for i in range(len(date)):
        if not date[i]=="-":
            trunc=trunc+str(date[i])

    return str(trunc)

#boxScore=pd.read_csv("C:\YDFS Project\Data Prep\Scores_2017\ATL\Away\GameATL201710200.csv")
#rs=pd.read_csv("C:\YDFS Project\Data Prep\Rosters\Cleaned\ATL.csv")

#Get name return index of player in roster
def getPlayerIndex(name,roster):
    for j in range(roster["Var.2"].size):
        if roster["Var.2"][j]==name:
            return j
                   
def getAverageAge(gameSummary,roster):
    
    age=np.array([])
    
    for j in range(gameSummary["Var.1"].size):
        mp = gameSummary["Basic.Box.Score.Stats"][j]
        if mp[len(mp)-3]==":":
            try:  
                yearsOld=roster.Age[getPlayerIndex(gameSummary["Var.1"][j],roster)]
                age=np.append(age,float(yearsOld))
                
            except:
                1
                
    return np.mean(age)        


for i in range(teamID.ABB.size):
        
    teamName=str(teamID.ABB[i])
    boxScore=pd.read_csv("C:/YDFS Project/Data Prep/Team Boxscores/Cleaned/"+str(teamID.ABB[i])+"Cleaned.csv")
    
    age = []
        
    for j in range(boxScore.DATE.size):
        
        fileName="Game"+teamName+removeDashes(boxScore.DATE[j])+"0.csv"
        
        if boxScore.HOME[j]:
            filePath="C:/YDFS Project/Data Prep/Scores_2017/"+teamName+"/Home/"       
        
        else:
            filePath="C:/YDFS Project/Data Prep/Scores_2017/"+teamName+"/Away/"
        
        gameSummary = pd.read_csv(filePath+fileName)
        roster = pd.read_csv("C:\YDFS Project\Data Prep\Rosters\Cleaned\\"+teamName+".csv")
        
        age.append(getAverageAge(gameSummary,roster))
        #drpm.append(getDRPMStats(gameSummary,roster))
        
    boxScore["AGE"]=age
        
    boxScore.to_csv(teamName+'Cleaned.csv',sep=',')  
    

            
#notFoundFrame = pd.DataFrame({'Name':nanNames,'Position':nanPOS,'Team':nanTeams})
#notFoundFrame.to_csv('NanNames.csv',sep=',')    



