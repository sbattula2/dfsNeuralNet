# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 13:03:31 2019

@author: nbatt
"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv('PlayerDirectory.csv')
df2 = df.loc[df['G']>20]
fitDF = df2.loc[:,['G','STD','FPTS','BOOMFREQ']]


kmeans = KMeans(n_clusters=10).fit(fitDF)
centroids = kmeans.cluster_centers_
print(centroids)

plt.scatter(fitDF['STD'], fitDF['FPTS'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)

df['CLUSTER'] = kmeans.predict(df.loc[:,['G','STD','FPTS','BOOMFREQ']])
df.set_index('Player',inplace=True)
df.to_csv('PlayerDirectory.csv')
#fitDF['BF'] = fitDF['BOOMFREQ']/fitDF['FPTS']