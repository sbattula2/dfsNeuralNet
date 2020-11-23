# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 14:40:50 2019

@author: nbatt
"""

import pandas as pd
import numpy as np
import os

def getError(numGames):
    #error of 6% or less essentially means you won it all
    
    #column P has num points scored
    errorDF = pd.DataFrame({'Date':[],'Error':[]})
    files = os.listdir('C:/NBA DFS/lineupOutputs')
    
    for i in files:
    
        try:
            os.chdir('C:/NBA DFS/lineupOutputs')
            lineupDF = pd.read_csv(i)
    
            #lineupDF.sort_values('P',ascending=False,inplace=True)
        
            os.chdir('C:/NBA DFS/Perfect Lineups')
            
            perfDF = pd.read_csv(i)
            
            perfScore = np.sum(perfDF['Score'])
            lineupScore = np.mean(lineupDF['P'].iloc[:numGames])
            
    
            errorDF.loc[errorDF.shape[0]] = [i,abs((perfScore-lineupScore)/perfScore*100)]
                
                
        except:
            print("whoops")
            print(i)
            
    return errorDF

df = pd.read_csv('C:/NBA DFS/lineupOutputs/Apr_11_2019.csv')
urf = getError(1)