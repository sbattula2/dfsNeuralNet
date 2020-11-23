# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 14:24:07 2018

@author: nbatt
"""

import pandas as pd
import numpy as np


def formatTable():
    teamID = pd.read_csv("C:/YDFS Project/Data Prep/TeamID.csv")
    
    for i in teamID.ABB:
        teamLogs = pd.read_csv("C:/YDFS Project/Data Prep/Team Boxscores/Cleaned/"+str(i)+"Cleaned.csv")
        
        offRating = [0]
        defRating = [0]
        
        for j in range(1,teamLogs.TEAM.size):
            
            tmPTS=np.sum(teamLogs.PTS[0:j])
            tmFGA=np.sum(teamLogs.FGA[0:j])
            tmFGM=np.sum(teamLogs.FGM[0:j])
            tmFTA=np.sum(teamLogs.FTA[0:j])
            tmOREB=np.sum(teamLogs.OREB[0:j])
            tmTOV=np.sum(teamLogs.TOV[0:j])
            tmDREB=np.sum(teamLogs.DREB[0:j])
            
            OppPTS=np.sum(teamLogs.OppPTS[0:j])
            OppDREB=np.sum(teamLogs.OppDREB[0:j])
            OppFGA=np.sum(teamLogs.OppFGA[0:j])
            OppFTA=np.sum(teamLogs.OppFTA[0:j])
            OppOREB=np.sum(teamLogs.OppOREB[0:j])        
            OppFGM=np.sum(teamLogs.OppFGM[0:j])
            OppTOV=np.sum(teamLogs.OppTOV[0:j])
            
            #100 x Pts / (0.5 * ((Tm FGA + 0.4 * Tm FTA - 1.07 * (Tm ORB / (Tm ORB + Opp DRB)) * (Tm FGA - Tm FG) + Tm TOV) + (Opp FGA + 0.4 * Opp FTA - 1.07 * (Opp ORB / (Opp ORB + Tm DRB)) * (Opp FGA - Opp FG) + Opp TOV)))
            
            offTotalPts=tmPTS
            
            offTotalPoss=0.5*((tmFGA + 0.4*tmFTA - 1.07*(tmOREB/(tmOREB+OppDREB))*(tmFGA-tmFGM)+tmTOV)+(OppFGA + 0.4*OppFTA - 1.07*(OppOREB/(OppOREB+tmDREB))*(OppFGA-OppFGM)+OppTOV))
            offensiveRating = 100*offTotalPts/offTotalPoss
            
            offRating.append(offensiveRating)
            
            defTotalPts=OppPTS
            defTotalPoss=0.5*((OppFGA + 0.4*OppFTA - 1.07*(OppOREB/(OppOREB+tmDREB))*(OppFGA-OppFGM)+OppTOV)+(tmFGA + 0.4*tmFTA - 1.07*(tmOREB/(tmOREB+OppDREB))*(tmFGA-tmFGM)+tmTOV))
            defensiveRating = 100*defTotalPts/defTotalPoss
            
            defRating.append(defensiveRating)
           
        teamLogs["OppRating"]=offRating
        teamLogs["DefRating"]=defRating
        
        #teamLogs["EffRating"]=teamLogs.OppRating/teamLogs.DefRating
        
        teamLogs.to_csv("C:/YDFS Project/Data Prep/Team Boxscores/Cleaned/"+str(i)+"Cleaned.csv",sep=',')
    
            
            
            
            
            
            
        
        
        
        
            
            
            
            
            
            
            
            
            
            
            
            