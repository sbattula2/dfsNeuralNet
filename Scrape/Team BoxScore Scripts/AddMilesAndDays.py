# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 12:46:05 2018

@author: nbatt
"""

#matplotlib inline
import pandas as pd
import math as Math



def gatherLocationsCSV():
    locations=pd.read_csv("C:/YDFS Project/Data Prep/Locations.csv")    
    return locations

def deg2Rad(deg):
    return deg * (Math.pi/180)
       
def getDistance(team1,team2):
    
    print("davido")
    print(team1)
    print(team2)
    
    locations = gatherLocationsCSV()

    lat1=None
    lat2=None
    lon1=None
    lon2=None
    
    
    for i in range(0,locations.TEAM.size):
                
        if(locations.TEAM[i]==team1):
            lat1 = locations.LAT[i]
            lon1 = locations.LON[i]
        
        
        if(locations.TEAM[i]==team2):
            lat2 = locations.LAT[i]
            lon2 = locations.LON[i]
        
        
            
    if(lat1!=None and lat2!=None and lon1!=None and lon2!=None):
          r = 6371; 
          dLat = deg2Rad(lat2-lat1)  
          dLon = deg2Rad(lon2-lon1) 
          a = Math.sin(dLat/2) * Math.sin(dLat/2) +Math.cos(deg2Rad(lat1)) * Math.cos(deg2Rad(lat2)) * Math.sin(dLon/2) * Math.sin(dLon/2)
          c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)) 
          d = r * c*0.621371
          return d;
      
def getDaysInBetween(date1String,date2String):
    
    date1Year = date1String[0:4]
    date1Month = date1String[5:7]
    date1Day = date1String[8:]

    date2Year = date2String[0:4]
    date2Month = date2String[5:7]
    date2Day = date2String[8:]
    
    date1 = date(int(date1Year),int(date1Month),int(date1Day))
    date2 = date(int(date2Year),int(date2Month),int(date2Day))
        
    daysBetween = date2-date1

    #print("Date 2 "+str(date1Day))

    return daysBetween.days

from datetime import date

def formatTable():

    teamID = pd.read_csv("C:/YDFS Project/Data Prep/TeamID.csv")
    
    #Add Distance
    for i in (teamID.ABB):
      
      teamLogs = pd.read_csv("C:/YDFS Project/Data Prep/Team Boxscores/Cleaned/"+str(i)+"Cleaned.csv")
        
      teamLogs = teamLogs.sort_values('DATE',ascending=True)  
      
      prevOpponent = None
      milesTraveled = []
      days=[]
    
      for j in range(teamLogs.HOME.size):
          if not (bool(teamLogs.HOME[j])):
              if prevOpponent == None:
    
                  miles = getDistance(teamLogs.TEAM[j],teamLogs.OPP[j])
                  milesTraveled.append(miles)
                  
                  prevOpponent = teamLogs.OPP[j]
                  
              else:
                  pre=0
                  if(len(milesTraveled)>0):
                      pre = milesTraveled[-1]
    
                  miles = pre+getDistance(prevOpponent,teamLogs.OPP[j])
                  milesTraveled.append(miles)
                  
                  prevOpponent = teamLogs.OPP[j]    
          else:
              milesTraveled.append(0)
              prevOpponent=None
          
          if j==0:
              days.append(0)
              
          else:
              
             # print("New")
              day1=teamLogs.DATE[j- 1]
              day2=teamLogs.DATE[j]
              between = int(getDaysInBetween(day1,day2))
              days.append(between)
              
              #print(day1)
              #print(day2)
              #print(between)
        
      teamLogs['MILES'] = milesTraveled
      teamLogs['DAYSREST'] = days
        
      colNames = list(teamLogs)
      for ak in colNames:
          if ak[0:7]=='Unnamed':
              teamLogs=teamLogs.drop(ak,axis=1)
                 
      teamLogs.to_csv("C:/YDFS Project/Data Prep/Team Boxscores/Cleaned/"+str(i)+"Cleaned.csv",sep=',')
    
     #teamATL = pd.read_csv("C:/YDFS Project/Data Prep/Team Boxscores/Cleaned/ATLCleaned.csv")
    
    
