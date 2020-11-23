# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 21:39:12 2019

@author: nbatt
"""
import pandas as pd
import os

teamID = pd.read_csv("C:/YDFS Project/Data Prep/TeamID.csv")
os.chdir("C:/YDFS Project/Data Prep/Rosters")
#Polish
#Remove (TW)
#place height in inches

for i in teamID.ABB:
        
    roster = pd.read_csv("C:/YDFS Project/Data Prep/Rosters/"+str(i)+".csv")
    
    for j in range(roster.Player.size):
        
        playerName = roster.Player[j]
        
        if playerName[len(playerName)-5:]==" (TW)":
            roster.Player[j] = playerName[0:len(playerName)-5]
        
        heightString = roster.Ht[j]
        height = float(heightString[0])*12+float(heightString[2:])
        
        roster.Ht[j] = height
        
        roster.to_csv(str(i)+".csv",sep=",")