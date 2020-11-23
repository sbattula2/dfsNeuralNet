# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 13:28:58 2019

@author: nbatt
"""
from selenium import webdriver
from datetime import date, timedelta
import pandas as pd
import numpy as np
import os
import calendar


def getPerf(dayNum):
    os.chdir('C:/NBA DFS/Perfect Lineups')

    #dateToGet = getDateFromDN(dayNum)
    
    url = 'https://www.linestarapp.com/Perfect/Sport/NBA/Site/FanDuel/PID/'
    url += str(dayNum)
    
    browser.get(url)

    date = browser.find_element_by_xpath('//*[@id="dnn_ctr763_ModuleContent"]/div/div/div[1]/div/span')
    date = date.text
    
    if len(date) == 12:
        fileName = (date[0:3]+"_"+date[4:6]+"_"+date[8:]+'.csv')
    
    else:
        fileName = (date[0:3]+"_"+date[4]+"_"+date[7:]+'.csv')
    
    print(fileName)

    try:
        table = browser.find_element_by_xpath('//*[@id="table_FanDuel_0"]')

        
        stats = []
        
        for line_id, lines in enumerate(table.text.split('\n')):
    
            if line_id > 0:
                lineSplits = lines.split(' ')        
                row=[]
                
                #Helps account for players with very long names, Jr., III, etc.
                if len(lineSplits) == 6:
                    for i in range(0,len(lineSplits)):
                        if i==2:
                            #Name
                            try:
                                row.append(str(lineSplits[i]+' '+lineSplits[i+1]))
                                    
                            except:
                                row.append(np.NaN)
    
                        elif i not in [2,3]:
                            #Position
                            try:
                                row.append(str(lineSplits[i]))
                            
                            except:
                                row.append(np.NaN)
                            
                                
                elif len(lineSplits)==7:
                    for i in range(0,len(lineSplits)):
                        if i==2:
                            #Name
                            if i==len(lineSplits)-5:
                                try:
                                    row.append(str(lineSplits[i]+' '+lineSplits[i+1]+' '+lineSplits[i+2]))
                                        
                                except:
                                    row.append(np.NaN)
        
                        elif i not in [2,3,4]:
                            #Position
                            try:
                                row.append(str(lineSplits[i]))
                            
                            except:
                                row.append(np.NaN)
                if(len(row)>2):
                    stats.append(row)
                                
                              
        #print(fileName)
                #stats.append(row)
        db = pd.DataFrame({'Player': [i[2] for i in stats],
                               'Pos': [i[0] for i in stats],
                               'Team': [i[1] for i in stats],
                               'Salary': [i[3] for i in stats],
                               'Score': [i[4] for i in stats]})
        
        renameC1B(db)
        db.to_csv(fileName)
    
    except:
        1 + 1
            
def getDateFromDN(dayNum):
    daysBetween = dayNum - 820
    openingDay = date(2018,10,16)
    dayNumDate = openingDay+timedelta(days=daysBetween)
    
    return dayNumDate
    
def getPerfYesterday():
    path_to_chromedriver = 'C:\ChromeDriver\chromedriver.exe' # Path to access a chrome driver
    browser = webdriver.Chrome(executable_path=path_to_chromedriver)
    
    dateToGet = date.today() - timedelta(days=1)
    
    fileName = (calendar.month_abbr[dateToGet.month]+"_"+str(dateToGet.day)+"_"+"2019.csv")
    
    url = getURLYesterday()
    browser.get(url)
    
    table = browser.find_element_by_xpath('//*[@id="table_FanDuel_0"]')
    
    stats = []
    
    for line_id, lines in enumerate(table.text.split('\n')):

        if line_id > 0:
            lineSplits = lines.split(' ')        
            row=[]
            
            #Helps account for players with very long names, Jr., III, etc.
            if len(lineSplits) == 6:
                for i in range(0,len(lineSplits)):
                    if i==2:
                        #Name
                        try:
                            row.append(str(lineSplits[i]+' '+lineSplits[i+1]))
                                
                        except:
                            row.append(np.NaN)

                    elif i not in [2,3]:
                        #Position
                        try:
                            row.append(str(lineSplits[i]))
                        
                        except:
                            row.append(np.NaN)
                        
                            
            elif len(lineSplits)==7:
                for i in range(0,len(lineSplits)):
                    if i==2:
                        #Name
                        if i==len(lineSplits)-5:
                            try:
                                row.append(str(lineSplits[i]+' '+lineSplits[i+1]+' '+lineSplits[i+2]))
                                    
                            except:
                                row.append(np.NaN)
    
                    elif i not in [2,3,4]:
                        #Position
                        try:
                            row.append(str(lineSplits[i]))
                        
                        except:
                            row.append(np.NaN)
            if(len(row)>2):
                stats.append(row)
                            
            #stats.append(row)
    
    db = pd.DataFrame({'Player': [i[2] for i in stats],
                           'Pos': [i[0] for i in stats],
                           'Team': [i[1] for i in stats],
                           'Salary': [i[3] for i in stats],
                           'Score': [i[4] for i in stats]})
    
    renameC1B(db)
    db.to_csv(fileName)
    browser.quit()

def getURLYesterday():
    os.chdir('C:\MLB_DFS\Perfect Lineups')

    yesterday = date.today() - timedelta(days=1)
    openingDay = date(2019,3,28)
        
    daysBetween = yesterday-openingDay
    
    pgInd = 1153+daysBetween.days
    url = 'https://www.linestarapp.com/Perfect/Sport/NBA/Site/FanDuel/PID/'
    url += str(pgInd)

    return url

def renameC1B(df):
    df.Pos = df.Pos.replace({'C/1B':'C1B'})

path_to_chromedriver = 'C:\ChromeDriver\chromedriver.exe' # Path to access a chrome driver
browser = webdriver.Chrome(executable_path=path_to_chromedriver) 
for i in range(820,1120):
    getPerf(i)
