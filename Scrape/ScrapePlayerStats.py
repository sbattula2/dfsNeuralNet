# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 14:05:27 2019

@author: nbatt
"""

import GetPosDefSeason as s1
import GetPosDefPerWeek as s2
import GetPaceData as s3
import GetOpp2FGData as s4
import GetOpp3FGData as s5
import GetOppDefRatings as s6
import GetOppOffRatings as s7
import os 
    
s1.getStuff()
os.chdir('C:/NBA DFS/Scrape')

s2.getStuff()

os.chdir('C:/NBA DFS/Scrape')
s3.getStuff()
os.chdir('C:/NBA DFS/Scrape')

s4.getStuff()
os.chdir('C:/NBA DFS/Scrape')

s5.getStuff()
os.chdir('C:/NBA DFS/Scrape')

s6.getStuff()
os.chdir('C:/NBA DFS/Scrape')

s7.getStuff()
os.chdir('C:/NBA DFS/Scrape')


