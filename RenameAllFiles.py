# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:35:31 2019

@author: nbatt
"""

import pandas as pd
import os

#perfect lineups
#lineupOutputs
#lineupInputs
#rename links
def renameFiles():
    os.chdir('C:/NBA DFS/lineupInputs')
    files = os.listdir()
    changeMonths = ['O','N','D']
    
    for i in files:
        fileName = i
        if fileName[0] in changeMonths:
            fileList = list(fileName)
            fileList[-5] = '8'
    
            try:        
                os.chdir('C:/NBA DFS/Perfect Lineups')        
                os.rename(i,"".join(fileList))
            except:
                print("huh")
                
            try:        
                os.chdir('C:/NBA DFS/lineupInputs')        
                os.rename(i,"".join(fileList))
            except:
                print("huh")
                
            try:        
                os.chdir('C:/NBA DFS/lineupOutputs')        
                os.rename(i,"".join(fileList))
            except:
                print("huh")
                    
            print("".join(fileList))
            
renameFiles()