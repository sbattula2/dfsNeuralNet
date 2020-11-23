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



def getSalaries(dayNum):
    os.chdir('C:\MLB_DFS\Ownerships')

    path_to_chromedriver = 'C:\ChromeDriver\chromedriver.exe' # Path to access a chrome driver
    browser = webdriver.Chrome(executable_path=path_to_chromedriver)
    
    dateToGet = getDateFromDN(dayNum)
    
    fileName = (calendar.month_abbr[dateToGet.month]+"_"+str(dateToGet.day)+"_"+"2019.csv")
    
    url = 'https://www.linestarapp.com/Ownership/Sport/MLB/Site/FanDuel/PID/'
    url += str(dayNum)
    
    browser.get(url)

    table = browser.find_element_by_xpath('//*[@id="tableTournament"]')
    
    stats = []
    
    for line_id, lines in enumerate(table.text.split('\n')):
        if line_id > 0:
            
                
            lineSplits = lines.split(' ')
            row = []
            
            #Helps account for players with very long names, Jr., III, etc.
            for i in range(len(lineSplits)-5,len(lineSplits)):
                if i<len(lineSplits)-2:
                    #Name
                    if i==len(lineSplits)-5:
                        try:
                            row.append(str(lineSplits[0]+' '+lineSplits[i]))
                                
                        except:
                            row.append(np.NaN)

                    #Pos, Team
                    else:
                        try:
                            row.append(str(lineSplits[i]))
                                
                        except:
                            row.append(np.NaN)

                else:
                    #ownership
                    if i==len(lineSplits)-1:
                        try:
                            row.append(float(lineSplits[i][0:-1]))
                        
                        except:
                            row.append(np.NaN)
                    
                    #salary
                    else:
                        try:
                            row.append(float(lineSplits[i][1:]))
                        except:
                            row.append(np.NaN)
                            
            stats.append(row)
    db = pd.DataFrame({'Player': [i[0] for i in stats],
                           'Pos': [i[1] for i in stats],
                           'Team': [i[2] for i in stats],
                           'Salary': [i[3] for i in stats],
                           'Ownership': [i[4] for i in stats]})
    
    renameC1B(db)
    db.to_csv(fileName)
    browser.quit()
    return db
            
def getDateFromDN(dayNum):
    daysBetween = dayNum - 1153
    openingDay = date(2019,3,28)
    dayNumDate = openingDay+timedelta(days=daysBetween)
    
    return dayNumDate
    
def getSalariesYesterday():
    path_to_chromedriver = 'C:\ChromeDriver\chromedriver.exe' # Path to access a chrome driver
    browser = webdriver.Chrome(executable_path=path_to_chromedriver)
    
    dateToGet = date.today() - timedelta(days=1)
    
    fileName = (calendar.month_abbr[dateToGet.month]+"_"+str(dateToGet.day)+"_"+"2019.csv")
    
    url = getURLYesterday()
    browser.get(url)
    
    table = browser.find_element_by_xpath('//*[@id="tableTournament"]')
    
    stats = []
    
    for line_id, lines in enumerate(table.text.split('\n')):
        if line_id > 0:
            
                
            lineSplits = lines.split(' ')
            row = []
            
            #Helps account for players with very long names, Jr., III, etc.
            for i in range(len(lineSplits)-5,len(lineSplits)):
                if i<len(lineSplits)-2:
                    #Name
                    if i==len(lineSplits)-5:
                        try:
                            row.append(str(lineSplits[0]+' '+lineSplits[i]))
                                
                        except:
                            row.append(np.NaN)

                    #Pos, Team
                    else:
                        try:
                            row.append(str(lineSplits[i]))
                                
                        except:
                            row.append(np.NaN)

                else:
                    #ownership
                    if i==len(lineSplits)-1:
                        try:
                            row.append(float(lineSplits[i][0:-1]))
                        
                        except:
                            row.append(np.NaN)
                    
                    #salary
                    else:
                        try:
                            row.append(float(lineSplits[i][1:]))
                        except:
                            row.append(np.NaN)
                            
            stats.append(row)
    db = pd.DataFrame({'Player': [i[0] for i in stats],
                           'Pos': [i[1] for i in stats],
                           'Team': [i[2] for i in stats],
                           'Salary': [i[3] for i in stats],
                           'Ownership': [i[4] for i in stats]})
    
    renameC1B(db)
    db.to_csv(fileName)
    browser.quit()

def getURLYesterday():
    os.chdir('C:\MLB_DFS\Ownerships')

        
    yesterday = date.today() - timedelta(days=1)
    openingDay = date(2019,3,28)
        
    daysBetween = yesterday-openingDay
    
    pgInd = 1153+daysBetween.days
    url = 'https://www.linestarapp.com/Ownership/Sport/MLB/Site/FanDuel/PID/'
    url += str(pgInd)

    return url

def renameC1B(df):
    df.Pos = df.Pos.replace({'C':'C1B','1B':'C1B'})
    
#getSalariesYesterday()
for i in range(1195,1219):
    getSalaries(i)
#getSalariesToday()
