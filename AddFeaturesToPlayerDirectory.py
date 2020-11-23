# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 12:38:30 2019

@author: nbatt
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:30:29 2019

@author: nbatt
"""

import pandas as pd
import numpy as np

def addFeature(colName,newColName):

    df = pd.read_csv('PlayerDirectory.csv')
    df[newColName] = [None]*df.shape[0]
    df2 = pd.read_csv('MegGameLogs.csv')
    
    for i in range(df.shape[0]):
        holder = df2.loc[(df2['Player']==df['Player'].iloc[i]) & (df2['Tm']==df['Tm'].iloc[i])]
        df[newColName].iloc[i] = np.std(holder[colName])
        
    
    df.to_csv('PlayerDirectory.csv',index=False)

def addFreq():
    df = pd.read_csv('PlayerDirectory.csv')
    df['BOOMFREQ'] = [None]*df.shape[0]
    df2 = pd.read_csv('MegGameLogs.csv')
    
    for i in range(df.shape[0]):
        holder = df2.loc[(df2['Player']==df['Player'].iloc[i]) & (df2['Tm']==df['Tm'].iloc[i])]
        df['BOOMFREQ'].iloc[i] = holder.loc[(holder['FPTS']>=40)].shape[0]/holder.shape[0]*100
        
    
    df.to_csv('PlayerDirectory.csv',index=False)
    
#addFreq()
#addFeature('FPTS','FPTS')
addFeature('FPTS','STD')
