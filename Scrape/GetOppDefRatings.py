# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 12:46:05 2018

@author: nbatt
"""

#matplotlib inline
from selenium import webdriver
import pandas
import os

def getStuff():
    path_to_chromedriver = 'C:\ChromeDriver\chromedriver.exe' # Path to access a chrome driver
    browser = webdriver.Chrome(executable_path=path_to_chromedriver)
    
    url = 'https://stats.nba.com/teams/defense/?sort=W&dir=-1&Season=2018-19&SeasonType=Regular%20Season'
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
    
    table = browser.find_element_by_class_name('nba-stat-table__overflow')
    
    team_ids = []
    team_names = []
    team_stats = []
    
    
    
    for line_id, lines in enumerate(table.text.split('\n')):
            
        if line_id <= 8:
            column_names = lines.split(' ')[1:]
        else:
            if line_id % 3 == 0:
                team_names.append(lines)
            if line_id % 3 == 1:
                
                lineSplits = lines.split(' ')
                row = []
                
                for i in lineSplits:
                    try:
                        row.append(float(i))
                            
                    except:
                        row.append(i)
                
                team_stats.append(row)
                            
                
    print(team_stats)
                
    
    db = pandas.DataFrame({'team': team_names,
                           'DEFRTG': [i[4] for i in team_stats],
                           'DREBPER': [i[6] for i in team_stats],
                           'STL': [i[7] for i in team_stats],
                           'BLK': [i[8] for i in team_stats], 
                           'OppPAINTPTS': [i[12] for i in team_stats]})
    
       
    os.chdir('C:/NBA DFS/seasonData')
    db.to_csv('DefRatings.csv',sep=',')
    
