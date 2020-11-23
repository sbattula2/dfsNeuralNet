# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 17:36:53 2019

@author: nbatt
"""
import os
import pandas as pd

#Loop through each lineupInput
#Add score based on the file name
#go through each player in the output 
#and find him in daily leaders
#if not found, add him to not found list

#os.chdir('C:/NBA DFS/lineupInputs')
#df = pd.read_csv('Nov_3_2018.csv')
#df.set_index('Player',inplace=True)
def getNamesNotFound():
    os.chdir('C:/NBA DFS/lineupInputs')
    
    files = os.listdir()       
    notFound = []
    
    for i in files:        
        os.chdir('C:/NBA DFS/lineupInputs')
        lineup = pd.read_csv(i)
        
        os.chdir('C:/NBA DFS/Daily Leaders')
        dl = pd.read_csv(i,encoding='latin-1')
        dl.set_index('Name',inplace=True)
        
        for q in lineup['Player']:
            #dl.loc[q]
            
            try:
                dl.loc[q]    
                
            except:
                if q not in notFound:
                    notFound.append(q)
                    if q == 'Walter Jr.':
                        print(i)
    #create notFound csv file
    os.chdir('C:/NBA DFS')
    dl.to_csv('NameEdits.csv')

def renameDailyLeaders():
    
    os.chdir('C:/NBA DFS')
    nameEdits = pd.read_csv('Player Name Edits.csv')
    
    os.chdir('C:/NBA DFS/Daily Leaders')
    files = os.listdir()       
    
    for i in files:   
        
        print(i)
        
        dl = pd.read_csv(i,encoding='latin-1')
        dl = dl.loc[dl['Name']!='Player']
        #dl.set_index('Name',inplace=True)
        
        for q in range(nameEdits.shape[0]):
            dl.loc[dl['Name']==nameEdits['BBREF'].iloc[q],'Name'] = nameEdits['FANDUEL'].iloc[q]
        
        dl.to_csv(i)
        

def addDFSPoints():
    os.chdir('C:/NBA DFS/Daily Leaders')
    
    files = os.listdir()       
    
    for i in files:   
        print(i)
        os.chdir('C:/NBA DFS/lineupInputs')
        lineup = pd.read_csv(i)
        lineup['Score'] = [0] * lineup.shape[0]
        
        os.chdir('C:/NBA DFS/Daily Leaders')
        dl = pd.read_csv(i,encoding='latin-1')
        dl = dl.loc[dl['Name']!='Player']
        dl.set_index('Name',inplace=True)
        
        for j,k in dl.iterrows():
            lineup.loc[lineup["Player"]==j,'Score'] = dl['FPTS'].loc[j]
        
        dl.to_csv(i)
        
        os.chdir('C:/NBA DFS/lineupInputs')
        lineup.to_csv(i,index=False)

#getNamesNotFound()
renameDailyLeaders()
addDFSPoints()
        
#os.chdir('C:/NBA DFS/lineupInputs') 
