# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 15:44:49 2019

@author: nbatt
"""

import pandas as pd
import os

dir = pd.read_csv('PlayerDirectory.csv')

os.chdir('Daily Leaders')

#Analyze the top 20 players and see how often each cluster top shows up

files = os.listdir()

for i in files:
    