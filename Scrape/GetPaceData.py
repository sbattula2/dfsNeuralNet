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
    
    url = 'https://stats.nba.com/teams/advanced/?sort=PACE&dir=-1&Season=2018-19&SeasonType=Regular%20Season'
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
        
        if line_id < 3:
            column_names = lines.split(' ')[1:]
        else:
            if line_id % 3 == 0:
                team_ids.append(lines)
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
                            
                
                
    
    db = pandas.DataFrame({'team': team_names,
                           'pace': [i[16] for i in team_stats]})
    
    db = db[['team', 'pace']]
       
    os.chdir('C:/NBA DFS/seasonData')
    db.to_csv('pace.csv',sep=',')
    
