# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:01:48 2019

@author: nbatt
"""

import pandas as pd
import numpy as np
import os

os.chdir('InjuriesDF')
files = os.listdir()
megInjury = pd.DataFrame({'Team':[],'Date':[],'USGMIN':[],'FC':[],'BC':[],'PG':[],'SG':[],'PF':[],'SF':[],'C':[]})

for i in files:
    os.chdir('C:/NBA DFS/Injuries/InjuriesDF/'+i)
    innerFiles = os.listdir()
    
    pos = ['PG','SG','SF','PF','C']
    entries = {}
        
    for j in innerFiles:
        injLog = pd.read_csv(j)
        
        entries['Team'] = i
        entries['USGMIN'] = np.sum(injLog['USG']/100*injLog['Min']/48*injLog['Pace'])

        fcPos = ['PF','SF','C']
        bcPos = ['PG','SG']
        
        entries['Date'] = j[:-4]
        entries['FC'] = np.sum(injLog.loc[injLog['Pos'].isin(fcPos),'Min']/48*injLog.loc[injLog['Pos'].isin(fcPos),'USG']/100*injLog.loc[injLog['Pos'].isin(fcPos),'Pace'])
        entries['BC'] = np.sum(injLog.loc[injLog['Pos'].isin(bcPos),'Min']/48*injLog.loc[injLog['Pos'].isin(bcPos),'USG']/100*injLog.loc[injLog['Pos'].isin(bcPos),'Pace'])
        
        for qo in pos:
            entries[qo] = np.sum(injLog.loc[injLog['Pos']==qo,'USG']/100*injLog.loc[injLog['Pos']==qo,'Min']/48*injLog.loc[injLog['Pos']==qo,'Pace'])
        
        megInjury = megInjury.append(entries,ignore_index=True)

os.chdir('C:/NBA DFS')        
megInjury.to_csv('InjuriesDF.csv',index=False)


