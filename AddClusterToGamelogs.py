# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 15:21:56 2019

@author: nbatt
"""

import pandas as pd

df = pd.read_csv('PlayerDirectory.csv',index_col=['Player','Tm'])
#df = pd.read_csv('PlayerDirectory.csv')
df2 = pd.read_csv('MegGameLogs.csv')

df2['Cluster'] = [None]*df2.shape[0]

#df2['Cluster'] = df2.apply(lambda x: print(x))
#df3 = df2.iloc[0:50]

def f(x):
    print('hopzplkd')
    return df.loc[x,'CLUSTER']

df3 = df2[['Player','Tm']].apply(f)['Player']

df2.set_index(['Player','Tm'],inplace=True)
df2['Cluster'] = df3 
df2[df2.columns[~df2.columns.str.contains('Unnamed:')]]
df2.to_csv('MegGameLogs.csv')

# =============================================================================
# for i,row in df2[['Player','Tm']].iterrows():
#     try:
#         print(df.loc[i,'CLUSTER'])
#     except:
#         print('ajpoake')
#         print(row)
# =============================================================================