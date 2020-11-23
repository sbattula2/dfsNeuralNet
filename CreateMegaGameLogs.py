# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:25:07 2019

@author: nbatt
"""

import os
import pandas as pd

os.chdir('C:/NBA DFS/Game Logs')
files = os.listdir('C:/NBA DFS/Game Logs')

currentDF = None

for i in files:
    df = pd.read_csv(i,encoding='latin-1')
    df['Player'] = [i[:-4]]*df.shape[0]
    
    print(i)
    
    if currentDF is None:
        currentDF = df
        
    else:
        currentDF = currentDF.append(df)

os.chdir('C:/NBA DFS')

currentDF['MP'] = currentDF['MP'].apply(lambda x: x[:x.find(':')])
currentDF.to_csv('MegGameLogs.csv')
