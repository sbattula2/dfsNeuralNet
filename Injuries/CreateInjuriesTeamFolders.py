# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 13:37:07 2019

@author: nbatt
"""

import os
import pandas as pd

teamID = pd.read_csv('C://NBA DFS//TeamID.csv')

os.chdir('C://NBA DFS//Injuries//InjuriesDF')

def createFolders():
    for i in teamID.ABB_REF:
        os.mkdir(i)
        
def createFiles():
    global teamID
    
    for i in teamID.ABB_REF:    
        os.chdir('C://NBA DFS//Injuries//InjuriesDF//'+str(i))
        teamScores = pd.read_csv('C://NBA DFS//Team Boxscores//'+str(i)+'.csv')
        for j in teamScores['DATE']:
            df = pd.DataFrame({'Player':[],'Min':[],'USG':[],'Pace':[],'Pos':[]})
            df.to_csv(j+'.csv',index=False)            
#create empty df file for every day that team played a game
 
createFolders()                   
createFiles()
            