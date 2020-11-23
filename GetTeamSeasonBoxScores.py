# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 12:46:05 2018

@author: nbatt
"""

#matplotlib inline
from selenium import webdriver
import pandas as pd
import os

path_to_chromedriver = 'C:\ChromeDriver\chromedriver.exe' # Path to access a chrome driver

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
def gatherTeamIDCSV():
    ids=pd.read_csv("TeamID.csv")    
    return ids

teamID = gatherTeamIDCSV()

os.chdir('Team Boxscores')

import time

for i in range(14,teamID.ABB_NBA.size):

    browser = webdriver.Chrome(executable_path=path_to_chromedriver)

    fileName =str(teamID.ABB_NBA[i])+'.csv' 
    url = 'https://stats.nba.com/search/team-game/#?sort=GAME_DATE&dir=1&Season=2018-19&SeasonType=Regular%20Season&TeamID='+str(teamID.IDNUM[i])
    
    browser.get(url)
    
    browser.find_element_by_xpath('//*[@id="custom-filters"]/div/table/tbody/tr/td[4]/button').click()
    browser.find_element_by_xpath('//*[@id="streak-finder"]/div[2]/section/div/div[2]/div/div[2]/stats-run-it/button').click()
    #browser.find_element_by_xpath('//*[@id="stat-table"]/nba-stat-table/div[2]/div/a').click()
    
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="stat-table"]/nba-stat-table/div[2]/div/a').click()
    
    table = browser.find_element_by_class_name('nba-stat-table')
    
    team_ids = []
    team_names = []
    team_stats = []
        
    for line_id, lines in enumerate(table.text.split('\n')):
            
        if line_id < 1:
            column_names = lines.split(' ')[1:]
        else:
            lineSplits = lines.split(' ')
            row = []
            
            for i in lineSplits:
                try:
                    row.append(float(i))
                        
                except:
                    row.append(i)
            
            team_stats.append(row)
                            
    db = pd.DataFrame({'TEAM': [i[0] for i in team_stats],
                            'DATE': [i[1] for i in team_stats],
                            'MATCHUP':[i[2]+str(i[3])+str(i[4]) for i in team_stats]})
        
    for q in range(2,len(column_names)):
        db[column_names[q]]=[i[q+3] for i in team_stats]
        
    db.to_csv(fileName,sep=',')
    browser.quit()

