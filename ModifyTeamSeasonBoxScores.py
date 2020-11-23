import pandas as pd
import os


#add home column to boxscores
teamID = pd.read_csv('TeamID.csv')
teamID.set_index('ABB_NBA',inplace=True)

os.chdir('C:/NBA DFS/Team Boxscores')
files = os.listdir('C:/NBA DFS/Team Boxscores')

for i in files:
    df = pd.read_csv(i)
    
    df['HOME'] = df['MATCHUP'].str[-4]!='@'
    df['OPP'] = df['MATCHUP'].str[-3:]
    df['OPP'] = df['OPP'].apply(lambda x:teamID.loc[x,'ABB_REF'])
    #df['DATE'] = df['DATE'].str[-4:]+'-'+df['DATE'].str[0:2]+'-'+df['DATE'].str[3:5]
    df['XPATH'] = [None]*len(df)
    
    df.loc[df['DATE'].str[0:4]=='2019','XPATH'] = '//*[@id="box_'+teamID.loc[i[:-4],'ABB_REF'].lower()+'_basic"]'
    #//*[@id="box_atl_basic"] 
    df.loc[df['DATE'].str[0:4]=='2018','XPATH'] = '//*[@id="box-'+teamID.loc[i[:-4],'ABB_REF']+'-game-basic"]'
    #//*[@id="box-ATL-game-basic"]
    
    df.to_csv(i,index=False)
    
for i in files:
    os.rename(i,teamID.loc[i[:-4],'ABB_REF']+'.csv')    