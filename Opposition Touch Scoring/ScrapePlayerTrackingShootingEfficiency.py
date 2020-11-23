# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 10:34:32 2019

@author: nbatt
"""
from selenium import webdriver
import pandas as pd
import os
import time
from selenium.webdriver.support.select import Select
import numpy as np


def getStuff(teamNum):
    path_to_chromedriver = 'C:\ChromeDriver\chromedriver.exe' # Path to access a chrome driver
    browser = webdriver.Chrome(executable_path=path_to_chromedriver)
    
    url = 'https://stats.nba.com/players/shooting-efficiency/?Season=2018-19&SeasonType=Regular%20Season'
    browser.get(url)
    # =============================================================================

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
    
    # Select against opponent
    # browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div/label/select/option[2]').click()
    # 
    
    #Click advanced filter
    #browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/div[1]/div[5]/a').click()

    #time.sleep(1)

    
    
    table = browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/div/table')
    
    team_names = []
    team_stats = []
    
    for q in range(0,11):
        if q > 0:
            browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[3]/div/div/a[2]').click()
            time.sleep(1)
        for line_id, lines in enumerate(table.text.split('\n')):
            print(line_id)
            print(lines)
            
            if line_id > 12:
                if line_id % 2 == 1:
                    team_names.append(lines)
                else:
                    lineSplits = lines.split(' ')
                    row = []
                     
                    for i in lineSplits:
                        try:
                            row.append(float(i))
                                 
                        except:
                            row.append(-9000)
                     
                    team_stats.append(row)
# =============================================================================
#         if line_id < 3:
#             column_names = lines.split(' ')[1:]
#         else:
#             if line_id % 3 == 0:
#                 team_ids.append(lines)
#             if line_id % 3 == 1:
#                 team_names.append(lines)
#             if line_id % 3 == 2:
#                 
#                 lineSplits = lines.split(' ')
#                 row = []
#                 
#                 for i in lineSQplits:
#                     try:
#                         row.append(float(i))
#                             
#                     except:
#                         row.append(-9000)
#                 
#                 team_stats.append(row)
#                             
#                 
#                 
#     
#     db = pandas.DataFrame({'team': team_names,
#                            'pace': [i[16] for i in team_stats]})
#     
#     db = db[['team', 'pace']]
#        
#     os.chdir('C:\YDFS Project\Data Prep')
# =============================================================================

    db = pd.DataFrame({'Player': team_names
                       ,'DRIVEPTS': [i[6] for i in team_stats]
                       ,'CSPTS': [i[8] for i in team_stats]
                       ,'PULLPTS': [i[10] for i in team_stats]
                       ,'PAINTPTS': [i[12] for i in team_stats]
                       ,'POSTPTS': [i[14] for i in team_stats]
                       ,'ELBOWPTS': [i[16] for i in team_stats]
                       ,'DRIVEPTS%': [i[7]/100 for i in team_stats]
                       ,'CSPTS%': [i[9]/100 for i in team_stats]
                       ,'PULLPTS%': [i[11]/100 for i in team_stats]
                       ,'PAINTPTS%': [i[13]/100 for i in team_stats]
                       ,'POSTPTS%': [i[15]/100 for i in team_stats]
                       ,'ELBOWPTS%': [i[17]/100 for i in team_stats]
                       })
    
    fileName = "PlayerTrackingShooting.csv"
    db.to_csv(fileName)
    browser.quit()
    
teamID = pd.read_csv('C:/NBA DFS/TeamID.csv')    

getStuff(1)