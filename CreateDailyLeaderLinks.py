# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:55:29 2019

@author: nbatt
"""

import pandas as pd
import os
from time import strptime

def createLinks():
    os.chdir('C:/NBA DFS/lineupInputs')
    files = os.listdir('C:/NBA DFS/lineupInputs')
    df = pd.DataFrame({'File':[],'Link':[]})
    
    for i in files:
        
        month = strptime(i[0:3], '%b').tm_mon
        
        day = i[4:6]
        year = i[7:11]
        
        if i[5] == '_':
            day = i[4]
            year = i[6:10]    
        
        link = 'https://www.basketball-reference.com/friv/dailyleaders.fcgi?month='+str(month)+'&day='+str(day)+'&year='+str(year)
        df.loc[df.shape[0]] = [i,link]
    
    return df

mykeTowers = createLinks()
os.chdir('C:/NBA DFS')
mykeTowers.to_csv('dailyLinks.csv')