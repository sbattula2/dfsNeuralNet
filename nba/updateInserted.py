# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:03:57 2019

@author: nbatt
"""
import pandas as pd

generated = pd.read_csv("outputLineups.csv")
tabloid = pd.read_csv("updateTabloid - updateTabloid.csv")

for i in range(3,12):
    for j in range(0,tabloid["PG"].size):
        player = generated.iloc[j,i-3]
        entry = ""
        
        for q in range(len(player)):
            if(player[q]!=":"):
                entry+=player[q]
            else:
                break
        
        tabloid.iloc[j,i] = entry
        
for a in range(0,12):
    for b in range(0,tabloid["PG"].size):
        player = tabloid.iloc[b,a]
        player = '"'+str(player)+'"'
        
        tabloid.iloc[j,i] = player

tabloid.to_csv("updatedLineups.csv",index=False)