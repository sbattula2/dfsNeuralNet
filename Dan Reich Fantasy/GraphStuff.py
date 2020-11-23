# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 18:09:25 2019

@author: nbatt
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.lines as mlines
import matplotlib.transforms as mtransforms

def getImage(path):
    return OffsetImage(plt.imread(path))

df = pd.read_csv('LeagueDraft.csv')
draftOrder = pd.DataFrame({'Pick':[i for i in range(1,13)]
,'Name':['Aditya','Will','Sai','Arbaz','Taeho','Shum','Anand','Dan',
         'Joel','Mike','Utkarsh','Salman']})
draftOrder.set_index('Pick',inplace=True)

df['Owner'] = df['Conscripter'].apply(lambda x: draftOrder.loc[x,'Name'])

df['ImgPath'] = df['Owner'].str.lower()+'.png'
df['Deviation'] = df['Draft Position'] - df['Average Rank'] 

df.groupby('Owner').mean()
#for i in range(1,13):
#    print(np.mean(df.loc[df['Conscripter']==i,'Draft Position']))

fig,ax = plt.subplots()
ax.scatter(df['Average Rank'],df['Draft Position']) 

fig.set_figheight(35)
fig.set_figwidth(35)

for x0, y0, path in zip(df['Average Rank'],df['Draft Position'],df['ImgPath']):
    ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
    ax.add_artist(ab)

#mainGraph = plt.figure(figsize=(10,10))

#plt.scatter(, c='r', alpha=0.5)
plt.title('Player\'s Projected Pick vs Player\'s Actual Pick')
plt.xlabel('Player\'s Projected Pick')
plt.ylabel('Player\'s Actual Pick')
line = mlines.Line2D([-200, 200], [-200, 200], color='red')
#plt.margins(0)
#transform = ax.transAxes
#line.set_transform(transform)
ax.add_line(line)

plt.show()
plt.savefig('draftVsRanking.png')
