# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:19:18 2019

@author: nbatt
"""

import pandas as pd
import numpy as np
import os

peaks = pd.DataFrame({'Date':[],'Perf Score':[],'Top Score':[],'Peak':[],'Survival':[]})

files = os.listdir('C:/NBA DFS/lineupOutputs')  

for i in files:
    
    try:
        df = pd.read_csv('Perfect Lineups/'+i)
        df2 = pd.read_csv('lineupOutputs/'+i)
        
        perfectScore = np.sum(df['Score'])-np.min(df['Score'])
        df2['Error'] = (perfectScore - df2['P'])/perfectScore 
        
        peaks = peaks.append({'Top Score':np.max(df2['P']),'Perf Score':perfectScore,'Date':i,'Peak':abs(perfectScore - np.max(df2['P']))/perfectScore,'Survival':len(df2.loc[df2['Error']<=0.25,:])/40},ignore_index=True)    
        #print(abs(np.sum(df['Score'])-np.max(df2['P']))/np.max(df2['P']))
    
    except:
        print(i)
    
print('Win %')
print(len(peaks.loc[peaks['Peak']<=0.05,:])/len(peaks)*100)

print('Survive %')

print(np.mean(peaks['Survival']*100))

print('Wins')
print(len(peaks.loc[peaks['Peak']<=0.05,:]))
print(len(peaks.loc[peaks['Peak']<=0.06,:]))
print(len(peaks.loc[peaks['Peak']<=0.07,:]))
print(len(peaks.loc[peaks['Peak']<=0.10,:]))