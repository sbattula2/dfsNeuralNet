# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:09:55 2019

@author: nbatt
"""

import pandas as pd
import numpy as np
import os

def createDatesDF():
    os.chdir('C:/NBA DFS/Monthly Schedules/ScrapedFiles')
    files = ['schedOct.csv','schedNov.csv','schedDec.csv','schedJan.csv','schedFeb.csv','schedMar.csv','schedApr.csv']
    playedDates = pd.DataFrame({'Dates':[],'Filename':[]})
    
    for i in files:
        df = pd.read_csv(i)
        
        uniqDates = np.array(df.Date.unique()).astype(str)
        
        datesDF = pd.DataFrame({'Dates':uniqDates})
        datesDF = datesDF.loc[datesDF['Dates'].str.count(',')==2]
        datesDF['Filename'] = [None]*datesDF['Dates'].size
        
        playedDates = playedDates.append(datesDF)
        playedDates.reset_index(drop=True,inplace=True)
    
    playedDates.loc[playedDates['Dates'].str.len()==16,'Filename'] = playedDates['Dates'].str[5:8]+'_'+playedDates['Dates'].str[9]+'_'+playedDates['Dates'].str[-4:]+'.csv'
    playedDates.loc[playedDates['Filename'].isnull(),'Filename'] = playedDates['Dates'].str[5:8]+'_'+playedDates['Dates'].str[9:11]+'_'+playedDates['Dates'].str[-4:]+'.csv'
    return playedDates

df = createDatesDF()  
df['LinkNum'] = np.arange(820,820+df.shape[0],1)    
os.chdir('C:/NBA DFS')
df.to_csv('playedDates.csv',index=False)
