# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:17:54 2019

@author: nbatt
"""

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


def getStuff():
    path_to_chromedriver = 'C:\ChromeDriver\chromedriver.exe' # Path to access a chrome driver
    browser = webdriver.Chrome(executable_path=path_to_chromedriver)
    
    url = 'https://stats.nba.com/teams/advanced/?sort=PACE&dir=-1&Season=2018-19&SeasonType=Regular%20Season'
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
    
    table = browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table')
    
    team_names = []
    team_stats = []
    
    for line_id, lines in enumerate(table.text.split('\n')):
        print(line_id)
        print(lines)
        
        if line_id > 3:
            if line_id % 3 == 1:
                team_names.append(lines)
            if line_id % 3 == 2:
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
    
    db = pd.DataFrame({'Team': [teamID.loc[i,'ABB_REF'] for i in team_names]
                       ,'GP': [i[0] for i in team_stats]
                       ,'W': [i[1] for i in team_stats]
                       ,'L': [i[2] for i in team_stats]
                       ,'MIN': [i[3] for i in team_stats]
                       ,'OFFRTG': [i[4] for i in team_stats]
                       ,'DEFRTG': [i[5] for i in team_stats]
                       ,'NETRTG': [i[6] for i in team_stats]    
                       ,'AST%': [i[7] for i in team_stats]
                       ,'ASTRATIO%': [i[8] for i in team_stats]
                       ,'AST_TOV': [i[9] for i in team_stats]
                       ,'OREB%': [i[10] for i in team_stats]
                       ,'DREB%': [i[11] for i in team_stats]
                       ,'REB%': [i[12] for i in team_stats]
                       ,'TOV%': [i[13] for i in team_stats]
                       ,'EFG%': [i[14] for i in team_stats]
                       ,'TS%': [i[15] for i in team_stats]
                       ,'PACE': [i[16] for i in team_stats]
                       ,'PIE': [i[17] for i in team_stats]})
    
    fileName = "TeamAdvanced.csv"
    os.chdir('C:/NBA DFS')
    db.to_csv(fileName)
    browser.quit()
    
teamID = pd.read_csv('C:/NBA DFS/TeamID.csv')    
teamID.set_index('FULLNAME',inplace=True)
getStuff()  