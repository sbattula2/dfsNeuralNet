# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 21:53:20 2019

@author: nbatt
"""

import pandas as pd
import numpy as np
import os

fantrax = pd.read_csv('Fantrax.csv',index_col='Names')
mainDF = pd.read_csv('Yahoo.csv',index_col='Names')
espn = pd.read_csv('Espn.csv')
espn['Names'] = espn['Names'].astype(str) 

espn['Names'] = espn['Names'].apply(lambda x: x[x.find(' ')+1:x.find(',')])
espn['Rank'] = [i+1 for i in range(0,len(espn))]
espn.set_index('Names',inplace=True)

mainDF['Fantrax'] = fantrax['Rank']
mainDF.loc[mainDF['Fantrax'].isna(),'Fantrax'] = mainDF['Rank']

mainDF['ESPN'] = espn['Rank']
mainDF.loc[mainDF['ESPN'].isna(),'ESPN'] = mainDF['Rank']

mainDF['Average Rank'] = mainDF.mean(axis=1)

mainDF.to_csv('AverageRanks.csv')