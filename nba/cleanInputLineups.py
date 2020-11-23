# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 16:39:13 2019

@author: nbatt
"""

import pandas as pd
import pulp
import re
import numpy as np
import math

def addFullName():
    space = []
    for i in range(pt.FPPG.size):
        space.append(" ")
        firstName = pt["First Name"][i]
        lastName = pt["Last Name"][i]
        
        if(firstName=="JJ"):
            pt["First Name"][i]="J.J."
            
        if(firstName=="TJ"):
            pt["First Name"][i]="T.J."
        
        if(lastName[len(lastName)-3:]=="Jr." or lastName[len(lastName)-3:]=="III"):
            print(lastName)
            pt["Last Name"][i]=lastName[:len(lastName)-4]

    pt["Nickname"]=pt["First Name"]+str(" ")+pt["Last Name"]

def findPlayer(ptIndex):
    player = pt['Nickname'][ptIndex]
    return player

def getMedians():
    medians = np.array([])
    for i in range(pt.FPPG.size):
        player = findPlayer(i)
        
        try:
            essentials = pd.read_csv("C:/YDFS Project/Data Prep/Gamelogs/"+player+".csv")
            essentials['FPTS']=essentials.PTS.astype(float)+essentials.ORB.astype(float)*1.2+essentials.DRB.astype(float)*1.2+essentials.AST.astype(float)*1.+essentials.STL.astype(float)*3+essentials.BLK.astype(float)*3-essentials.TOV.astype(float)
            medians = np.append(medians,np.median(essentials.FPTS))   
            
        except:
            medians = np.append(medians,-1000)   
    return medians

def getMid50Average():
    mid50 = np.array([])
    for i in range(pt.FPPG.size):
        player = findPlayer(i)
        
        try:
            essentials = pd.read_csv("C:/YDFS Project/Data Prep/Gamelogs/"+player+".csv")
            essentials['FPTS']=essentials.PTS.astype(float)+essentials.ORB.astype(float)*1.2+essentials.DRB.astype(float)*1.2+essentials.AST.astype(float)*1.+essentials.STL.astype(float)*3+essentials.BLK.astype(float)*3-essentials.TOV.astype(float)
            #essentials = essentials.sort(essentials.FPTS,ascending=True)                        
            #mid50 = np.append(medians,np.median(essentials.FPTS))    
            
            p25 = np.percentile(essentials.FPTS,25)
            p75 = np.percentile(essentials.FPTS,75)
            
            fpts = np.array([])
            
            
            for i in essentials.FPTS:
                if i>=p25 and i<=p75:
                    fpts = np.append(fpts,i)
                    
            mid50 = np.append(mid50,np.mean(fpts))    
            
        except:
            #print(i)
            mid50 = np.append(mid50,-1000)
            
    return mid50

def getXGameAvg(numGames):
    addendum = np.array([])
    for i in range(pt.FPPG.size):
        player = findPlayer(i)
        
        try:
            essentials = pd.read_csv("C:/YDFS Project/Data Prep/Gamelogs/"+player+".csv")
            essentials['FPTS']=essentials.PTS.astype(float)+essentials.ORB.astype(float)*1.2+essentials.DRB.astype(float)*1.2+essentials.AST.astype(float)*1.5+essentials.STL.astype(float)*3+essentials.BLK.astype(float)*3-essentials.TOV.astype(float)
              
            last3 = np.mean(essentials['FPTS'][essentials['FPTS'].size-numGames:])
                                
            addendum = np.append(addendum,float(last3))    
            
        except:
            #print(i)
            addendum = np.append(addendum,-1000)
            
    return addendum

def addPER():
    addendum = []
    al = pd.read_csv("C:/YDFS Project/Data Prep/advancedLogs.csv")
    
    for i in range(pt.FPPG.size):
        player = findPlayer(i)
        
        try:
            toAdd = -1000
            for j in range(al.Name.size):
                if player == al.Name[j]:
                    toAdd = al["PER"][j]
                    addendum.append(toAdd)
                    break
                
                if j == al.Name.size-1:
                    addendum.append(toAdd)
                          
        except:
            addendum = np.append(addendum,-1000)
            
    return addendum
    
    
def addUSG():
    addendum = []
    al = pd.read_csv("C:/YDFS Project/Data Prep/advancedLogs.csv")
    
    for i in range(pt.FPPG.size):
        player = findPlayer(i)
        
        try:
            toAdd = -1000
            for j in range(al.Name.size):
                if player == al.Name[j]:
                    toAdd = al["USG"][j]
                    addendum.append(toAdd)
                    break
                
                if j == al.Name.size-1:
                    addendum.append(toAdd)
                          
        except:
            addendum = np.append(addendum,-1000)
            
    return addendum

def addMPG(numGames):
    addendum = np.array([])
    for i in range(pt.FPPG.size):

        try:
            player = findPlayer(i)
            
            essentials = pd.read_csv("C:/YDFS Project/Data Prep/Gamelogs/"+player+".csv")
            mpString = []
            
            for i in range(numGames):
                mpString.append(essentials["MP"][essentials.MP.size-(i+1)])
            
            mpInt = np.array([])
            
            for i in range(len(mpString)):
                if len(mpString[i])==4:
                    mpInt = np.append(int(mpString[i][0:1]),mpInt)
                elif len(mpString[i])==5:
                    mpInt = np.append(int(mpString[i][0:2]),mpInt)
                else:
                    mpInt = np.append(int(0),mpInt)

            addendum = np.append(addendum,np.mean(mpInt))
        
        except:
           addendum = np.append(addendum,-1000)

    return addendum

def addDefVPos():
    addendum = []
    dp = pd.read_csv("C:/YDFS Project/Data Prep/dvpAvg.csv")
    
    for i in range(pt.FPPG.size):
        pos = pt.Position[i]
        opp = pt.Opponent[i]
        
        try:
            for q in range(dp.team.size):
                if dp.team[q]==opp:
                    
                    if pos=="PG":
                        bcAvg = float(dp["SG"][q]/np.mean(dp["SG"])+dp[pos][q]/np.mean(dp[pos]))/2
                        addendum.append(1/(1+math.exp(50*(1-bcAvg)))) 
                    elif pos=="SG":
                        bcAvg = float(dp["PG"][q]/np.mean(dp["PG"])+dp["SF"][q]/np.mean(dp["SF"])+dp[pos][q]/np.mean(dp[pos]))/3
                        addendum.append(1/(1+math.exp(50*(1-bcAvg))))
                    elif pos=="SF":
                        bcAvg = float(dp["SG"][q]/np.mean(dp["SG"])+dp["PF"][q]/np.mean(dp["PF"])+dp[pos][q]/np.mean(dp[pos]))/3
                        addendum.append(1/(1+math.exp(50*(1-bcAvg))))
                    elif pos=="PF":
                        bcAvg = float(dp["SF"][q]/np.mean(dp["SF"])+dp["C"][q]/np.mean(dp["C"])+dp[pos][q]/np.mean(dp[pos]))/3
                        addendum.append(1/(1+math.exp(50*(1-bcAvg))))
                    elif pos=="C":
                        bcAvg = float(dp["PF"][q]/np.mean(dp["PF"])+dp[pos][q]/np.mean(dp[pos]))/2
                        addendum.append(1/(1+math.exp(50*(1-bcAvg))))
                         
        except:
            addendum = np.append(addendum,-1000)
            
    return addendum

def addUQR(numGames):
    addendum = np.array([])
    
  
    for i in range(pt.FPPG.size):
    
        try:
            player = findPlayer(i)
            
            essentials = pd.read_csv("C:/YDFS Project/Data Prep/Gamelogs/"+player+".csv")
            #essentials["FPTS"] = essentials.TRB*1.2+essentials.AST*1.5+essentials.STL*3+essentials.BLK*3-essentials.TOV+essentials.PTS
            
            fpts = essentials["FPTS"][essentials.FPTS.size-numGames:]
            
            uqr = np.percentile(fpts,float(75))
            
            addendum = np.append(addendum,uqr)
    
        except:
            addendum = np.append(addendum,np.NAN)
        
    return addendum

def getRAT():
    medians = np.array([])
    for i in range(pt.FPPG.size):
        player = findPlayer(i)
        
        try:
            essentials = pd.read_csv("C:/YDFS Project/Data Prep/Gamelogs/"+player+".csv")
            essentials['FPTS']=essentials.PTS.astype(float)+essentials.ORB.astype(float)*1.2+essentials.DRB.astype(float)*1.2+essentials.AST.astype(float)*1.+essentials.STL.astype(float)*3+essentials.BLK.astype(float)*3-essentials.TOV.astype(float)
            medians = np.append(medians,np.median(essentials.FPTS))   
            
        except:
            medians = np.append(medians,-1000)   
    return medians

# =============================================================================
# def addBoom():
#     addendum = np.array([])
#     for i in range(pt.MPG.size):
#         boom = float((pt.FPPG+pt.USG[i]/20+ ((1+pt.DP[i])**2))*(pt.MPG[i]/25))
#         addendum = np.append(boom,addendum)
#    
#     return addendum
# =============================================================================
    
pt=pd.read_csv("Mar24-2019.csv")


for j in range(pt.Opponent.size):
                 
    if(pt.Opponent[j]=="CHA"):
        pt.Opponent[j]="CHO"
    
    elif(pt.Opponent[j]=="PHX"):
        pt.Opponent[j]="PHO"
        
    elif(pt.Opponent[j]=="BKN"):
        pt.Opponent[j]="BRK"
                
    elif(pt.Opponent[j]=="GS"):
        pt.Opponent[j]="GSW"
        
    elif(pt.Opponent[j]=="SA"):
        pt.Opponent[j]="SAS"
        
    elif(pt.Opponent[j]=="NY"):
        pt.Opponent[j]="NYK"
        
    elif(pt.Opponent[j]=="NO"):
        pt.Opponent[j]="NOP"
        
for j in range(pt.Team.size):
                 
    if(pt.Team[j]=="CHA"):
        pt.Team[j]="CHO"
    
    elif(pt.Team[j]=="PHX"):
        pt.Team[j]="PHO"
        
    elif(pt.Team[j]=="BKN"):
        pt.Team[j]="BRK"
                
    elif(pt.Team[j]=="GS"):
        pt.Team[j]="GSW"
        
    elif(pt.Team[j]=="SA"):
        pt.Team[j]="SAS"
        
    elif(pt.Team[j]=="NY"):
        pt.Team[j]="NYK"
        
    elif(pt.Team[j]=="NO"):
        pt.Team[j]="NOP"
        
addFullName()

pt["Injury Indicator"][5] = np.NaN

pt["5GameAvg"]=getXGameAvg(5)
pt["MPG"]=addMPG(5)
pt["PER"]=addPER()
pt["USG"]=addUSG()
pt["DP"]= addDefVPos()

pt["UQR"]= addUQR(5)

boom = []

#pt["DVP_Percentage"] = pt.DP/(pt.PER/15+pt.USG/20+ pt.DP)
pt = pt.set_index('Nickname')

#look at injured, add usg reservoir for each team's backcourt, frontcourt, midcourt
#teamID = pd.read_csv("C:/YDFS Project/Data Prep/TeamID.csv")    
#reserves = pd.DataFrame({'TEAM':teamID.ABB,'BC':[0]*30,'MC':[0]*30,'FC':[0]*30})
#al = pd.read_csv("C:/YDFS Project/Data Prep/advancedLogs.csv")

# =============================================================================
# for i in range(pt["Injury Indicator"].size):
#     if pt["Injury Indicator"][i]=="INJ" or pt["Injury Indicator"][i]=="O" or pt["Injury Indicator"][i]=="GTD" :
#         #get team
#         #get usg rate
#         #add to reserves
#         team = pt.Team[i]
#         for aj in range(teamID.ABB.size):
#             if team == teamID.ABB[aj]:
#                 team = aj
#         
#         player = pt.FullName[i]
#         for j in range(al.Name.size):
#             if player == al.Name[j]:
#                 toAdd = al["USG"][j]
#                 if pt.Position[i] == "PG" or pt.Position[i] == "SG":
#                     reserves["BC"][team] = reserves["BC"][team] + toAdd
#                 
#                 if pt.Position[i] == "SF":
#                     reserves["MC"][team] = reserves["MC"][team] + toAdd
#                     
#                 if pt.Position[i] == "PF" or pt.Position[i] == "C":
#                     reserves["FC"][team] = reserves["FC"][team] + toAdd
# 
# 
# for i in range(pt.Position.size):
#     
#     team = pt.Team[i]
#     for aj in range(teamID.ABB.size):
#         if team == teamID.ABB[aj]:
#             team = aj
#     
#     if pt.Position[i]=="PG" or pt.Position[i]=="SG":
#         boom.append(pt.FPPG[i]/30*2.5+pt.UQR[i]/40*2.5+ 5*(pt.USG[i]+reserves["BC"][aj])/20+ ((1+pt.DP[i])**2)*pt.MPG[i]/25)
# 
#     elif pt.Position[i]=="SF":
#         boom.append(pt.FPPG[i]/30*2.5+pt.UQR[i]/40*2.5+ 5*(pt.USG[i]+reserves["MC"][aj])/20+ ((1+pt.DP[i])**2)*pt.MPG[i]/25)
#         
#     elif pt.Position[i]=="PF" or pt.Position[i]=="C":
#         boom.append(pt.FPPG[i]/30*2.5+pt.UQR[i]/40*2.5+ 5*(pt.USG[i]+reserves["FC"][aj])/20+ ((1+pt.DP[i])**2)*pt.MPG[i]/25)
# 
#         
# pt["BOOM"]=boom
# =============================================================================

#remove injured
pt=pt[pt["Injury Indicator"]!="INJ"]
pt=pt[pt["Injury Indicator"]!="O"]
pt=pt[pt["Injury Indicator"]!="GTD"]
# =============================================================================
# pt=pt[pt["Opponent"]!="WAS"]
# pt=pt[pt["Opponent"]!="BRK"]
# pt=pt[pt["Opponent"]!="CHI"]
# pt=pt[pt["Opponent"]!="MEM"]
# pt=pt[pt["Opponent"]!="POR"]
# pt=pt[pt["Opponent"]!="BOS"]
# pt=pt[pt["Opponent"]!="DET"]
# pt=pt[pt["Opponent"]!="SAS"]
# pt=pt[pt["Opponent"]!="IND"]
# pt=pt[pt["Opponent"]!="DAL"]
# pt=pt[pt["Opponent"]!="LAC"]
# pt=pt[pt["Opponent"]!="UTA"]
# pt=pt[pt["Opponent"]!="WAS"]
# pt=pt[pt["Opponent"]!="BRK"]
# pt=pt[pt["Opponent"]!="GSW"]
# pt=pt[pt["Opponent"]!="MIA"]
# =============================================================================


# =============================================================================
# # Add F
# forward = pt[pt.Position.isin(["SF","PF"])].copy()
# forward.Position = "F"
# pt = pd.concat([pt, forward])
# 
# # Add G
# guard = pt[pt.Position.isin(["SG","PG"])].copy()
# guard.Position = "G"
# pt = pd.concat([pt, guard])
# 
# # Add UTIL
# util = pt[pt.Position.isin(["SF","PF","SG","PG","C"])].copy()
# util.Position = "UTIL"
# pt = pd.concat([pt, util])
# 
# =============================================================================
#Gunna tape good
SALARY_CAP = 60000

pos_num_available = {
    "PG": 2,
    "SG": 2,
    "PF": 2,
    "SF": 2,
    "C": 1
}

rp = 9

def optimize(colName):
    
    availables = pt[["Position", "FullName", "Salary",
      colName]].groupby(["Position", "FullName", "Salary",
      colName]).agg("count")
    availables = availables.reset_index()
    
    salaries = {}
    points = {}

    for pos in availables.Position.unique():
        available_pos = availables[availables.Position == pos]
        salary = list(available_pos[["FullName","Salary"]].set_index("FullName").to_dict().values())[0]
        point = list(available_pos[["FullName",colName]].set_index("FullName").to_dict().values())[0]
       
        salaries[pos] = salary
        points[pos] = point
    
    _vars = {k: pulp.LpVariable.dict(k, v, cat="Binary") for k, v in points.items()}
    
    prob = pulp.LpProblem("Fantasy", pulp.LpMaximize)
    rewards = []
    costs = []
    #position_constraints = []
    
    for k, v in _vars.items():
        costs += pulp.lpSum([salaries[k][i] * _vars[k][i] for i in v])
        rewards += pulp.lpSum([points[k][i] * _vars[k][i] for i in v])
        
        prob += pulp.lpSum([_vars[k][i] for i in v]) <= pos_num_available[k]
    
    prob += pulp.lpSum([_vars[p] for p in ['SF','PF', 'SG','PG','C']]) == rp
    
# =============================================================================
#     for position_name in ('C'):
#         for player_name in _vars[position_name]:
#             prob += pulp.lpSum([_vars[p][player_name] for p in ['UTIL', position_name]]) <= 1
#             
#     for position_name in ('PF','SF'):
#         for player_name in _vars[position_name]:
#             prob += pulp.lpSum([_vars[p][player_name] for p in ['UTIL','F', position_name]]) <= 1
#         
#     for position_name in ('PG','SG'):
#         for player_name in _vars[position_name]:
#             prob += pulp.lpSum([_vars[p][player_name] for p in ['UTIL','G', position_name]]) <= 1
#                 
# =============================================================================
    prob += pulp.lpSum(rewards)
    prob += pulp.lpSum(costs) <= SALARY_CAP
    
    MIN = SALARY_CAP*0.95
    prob += pulp.lpSum(costs) >= MIN
    
    prob.solve()
    summary(prob,colName)
    
def summary(prob,col):
    div = '---------------------------------------\n'
    print(col)
    print("Variables:\n")
    score = str(prob.objective)
    constraints = [str(const) for const in prob.constraints.values()]
    for v in prob.variables():
        score = score.replace(v.name, str(v.varValue))
        constraints = [const.replace(v.name, str(v.varValue)) for const in constraints]
        if v.varValue != 0:
            print(v.name, "=", v.varValue)
    print(div)
    print("Constraints:")
    for constraint in constraints:
        constraint_pretty = " + ".join(re.findall("[0-9\.]*\*1.0", constraint))
        if constraint_pretty != "":
            print("{} = {}".format(constraint_pretty, eval(constraint_pretty)))
    print(div)
    
pt.to_csv("Mar24-2019.csv")
