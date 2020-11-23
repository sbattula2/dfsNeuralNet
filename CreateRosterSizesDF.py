# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:09:41 2019

@author: nbatt
"""

import pandas as pd
import os
import numpy as np

playerDir = pd.read_csv('PlayerDirectory.csv',index_col=['Player','Tm'])
os.chdir('Anthropomorphic')
files = os.listdir()
sizes = pd.DataFrame({'Team':[],'Ht':[],'Wt':[],'Density':[],'Ht_Min':[],'Wt_Min':[],'Density_Min':[]})

for i in files:
    df = pd.read_csv(i)
    df['Tm'] = i[:-4]
    #df = 
    #df = df.apply(lambda x: playerDir.loc[(x['Player'],x['Tm']),'MP'],axis=1)
    #df['Min'] = df.apply(lambda x: playerDir.loc[(x['Player'],x['Tm']),'MP'],axis=1)
    df.set_index(['Player','Tm'],inplace=True)
    df['Min'] = playerDir['MP']
    row = {'Team':i[:-4],'Ht':np.mean(df['Ht']),'Wt':np.mean(df['Wt']),'Density':np.mean(df['Wt'])/np.mean(df['Ht'])}
    row['Ht_Min'] = np.mean(df['Ht']*df['Min']/48)
    row['Wt_Min'] = np.mean(df['Wt']*df['Min']/48)
    row['Density_Min'] = np.mean(df['Wt']/df['Ht']*df['Min'])/48
    
    sizes = sizes.append(row,ignore_index=True)
    