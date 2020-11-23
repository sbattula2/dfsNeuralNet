# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 12:00:30 2019

@author: nbatt
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 12:46:05 2018

@author: nbatt
"""

#matplotlib inline
from selenium import webdriver
import pandas as pd
import os
import time
from selenium.webdriver.support.select import Select

def getStuff():
    path_to_chromedriver = 'C:\ChromeDriver\chromedriver.exe' # Path to access a chrome driver
    browser = webdriver.Chrome(executable_path=path_to_chromedriver)
    
    url = 'https://basketballmonster.com/dfsdvp.aspx'
    browser.get(url)
    # =============================================================================
    # #Get 17-18 season
    # browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div/label/select/option[2]').click()
    # 
    # #Get season type
    # browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/div[1]/div[2]/div/div/label/select/option[2]').click()
    # 
    # #Get per game
    # browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/div[1]/div[3]/div/div/label/select/option[2]').click()
    # 
    # #Get season segment
    # browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/div[1]/div[4]/div/div/label/select/option[2]').click()
    # 
    # =============================================================================
    
    time.sleep(3)
    
    dateSelect = Select(browser.find_element_by_xpath('//*[@id="DateFilterControl"]'))
    dateSelect.select_by_index(1)
    
    leagueSelect = Select(browser.find_element_by_xpath('//*[@id="DAILYTYPEDROPDOWN"]'))
    leagueSelect.select_by_index(2)
    
    
    table = browser.find_element_by_class_name('datatable')
    
    col_names = []
    team_stats = []
    
    for line_id, lines in enumerate(table.text.split('\n')):
        
        if line_id == 0:
            col_names.append(lines)
        
        elif line_id > 1:
            cursor = lines.split(' ')[1:]
            team_stats.append(cursor)
    
    for i in range(len(team_stats)):
        if team_stats[i][0]=="BKN":
            team_stats[i][0]="BRK"
        
        if team_stats[i][0]=="NOR":
            team_stats[i][0]="NOP"
            
        if team_stats[i][0]=="CHA":
            team_stats[i][0]="CHO"
            
    db = pd.DataFrame({'team': [i[0] for i in team_stats],
                           'All': [i[2] for i in team_stats],
                           'PG': [i[3] for i in team_stats],
                           'SG': [i[4] for i in team_stats],
                           'SF': [i[5] for i in team_stats],
                           'PF': [i[6] for i in team_stats],
                           'C': [i[7] for i in team_stats]})
       
    os.chdir('C:/NBA DFS/seasonData')
    db.to_csv('dvpWeek.csv',sep=',')

def fuseWithSeasonStats():
    import numpy as np
    os.chdir('C:\YDFS Project\Data Prep')
    sd = pd.read_csv("dvpSeason.csv")   
    wd = pd.read_csv("dvpWeek.csv")
    
    sd = sd.sort_values(by=['team'],axis=0,ascending=True)
    wd = wd.sort_values(by=['team'],axis=0,ascending=True)
    
    print(sd)
    print(wd)
    
    tms = sd.team
    pf = np.array((sd.PF+wd.PF)/2)
    sf = np.array((sd.SF+wd.SF)/2)
    pg = np.array((sd.PG+wd.PG)/2)
    sg = np.array((sd.SG+wd.SG)/2)
    c = np.array((sd.C+wd.C)/2)
    
    sd.PF = pf
    sd.SF = sf
    sd.PG = pg
    sd.SG = sg
    sd.C = c
    
    ad = pd.DataFrame({'team':tms,'PG':pg,'SG':sg,'PF':pf,'SF':sf,'C':c})
    
    ad.to_csv('dvpAvg.csv',sep=',')

    
