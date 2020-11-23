# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:20:12 2019

@author: nbatt
"""

import pandas as pd
import os

df = pd.read_csv('Player Name Edits.csv')
df.set_index('BBREF',inplace=True)

os.chdir('C:/NBA DFS/Daily Leaders')
dailyLeaderFiles = os.listdir('C:/NBA DFS/Daily Leaders')

for i in dailyLeaderFiles:
    print(i)
    df2 = pd.read_csv(i,encoding='latin-1')
    df2.set_index('Name',inplace=True)
    
    for q,p in df.iterrows():
        df2.rename(index={q:df['FANDUEL'].loc[q]},inplace=True)
    
    df2.to_csv(i)