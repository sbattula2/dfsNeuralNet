# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:58:50 2019

@author: nbatt
"""

import os
import pandas as pd

df = pd.read_csv('TeamID.csv')
#df.set_index('ABB_REF',inplace=True)

os.chdir('C:/NBA DFS/Basic Box Scores')
for i in df['ABB_REF']:
    os.mkdir(i)
    os.chdir(i)
    os.mkdir('Away')
    os.mkdir('Home')
    os.chdir('C:/NBA DFS/Basic Box Scores')    
    