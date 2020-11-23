# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 21:39:12 2019

@author: nbatt
"""
import pandas as pd
import os

os.chdir("C:/NBA DFS 2019/Anthropomorphic")  
files = os.listdir("C:/NBA DFS 2019/Anthropomorphic")
#Polish
#Remove (TW)
#place height in inches
for i in files:
    roster = pd.read_csv(i)
    
    roster.loc[roster['Player'].str[:-5]==" (TW)",'Player'] = roster['Player'].str[:-5]
    try:
        roster['Ht'] = roster['Ht'].str[0].astype(float)*12+roster['Ht'].str[2:].astype(float)
    
    except:
        print('ppp')
    
    roster = roster.loc[:,~roster.columns.str.contains('^Unnamed')]
    roster.to_csv(i,index=False)
    
# =============================================================================
#     for j in range(roster['Player'].size):
#         
#         playerName = roster.Player[j]
#         
#         if playerName.loc[len(playerName)-5:]==" (TW)"]roster.Player[j] = 
#         
#         heightString = roster.Ht[j]
#         height = float(heightString[0])*12+float(heightString[2:])
#         
#         roster.Ht[j] = height
#         
#         roster.to_csv(str(i)+".csv",sep=",")
# 
# =============================================================================
