# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 12:23:27 2019

@author: nbatt
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 20:08:47 2019

@author: nbatt
"""
# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
#read player directory
#for each cluster number, besides like cluster 1 and 2 (the elite players) 
#use this script
#create first layer with nodes equal to number of variables
#pass in variables
#second layer is essentially a probability categorization into below, at or above average
#similar to classifying clothes problem

class_names = ['Shit', 'Bad', 'Meh', 'Good', 'Great','KaBoom']

directory = pd.read_csv('MegGameLogs.csv')

gameLogs = pd.read_csv('MegGameLogs.csv')
gameLogs['Playtype'] = np.around(gameLogs['PTS'].astype(int)/10)
gameLogs.loc[gameLogs['Playtype']>4,'Playtype'] = 4

gameLogs['ExpectedGame'] = [None]*len(gameLogs)
gameLogs.set_index(['Player','Age'],inplace=True)
pred = pd.Series([])

acc = pd.DataFrame({'Cluster':[],'Acc':[],'Loss':[]})

for i in range(0,10):
  
# ['OFE','USG','USGMIN','USGMIN_COURT','STREAK']
    inputCols = ['OFE','USG','USGMIN','USGMIN_COURT','STREAK']
    
    filteredLog = gameLogs.loc[gameLogs['Cluster']==i]
    
    msk = np.random.rand(len(filteredLog)) < 0.8
          
    train = filteredLog[msk]
    test = filteredLog[~msk]
    
    inputTrain = train.loc[:,inputCols]
    outputTrain = train.loc[:,'Playtype']
    
    inputTest = test.loc[:,inputCols]
    outputTest = test.loc[:,'Playtype']
    
    model = tf.keras.Sequential([tf.keras.layers.Dense(units=5,input_shape=[5]),
        tf.keras.layers.Dense(100, activation=tf.nn.sigmoid),
        tf.keras.layers.Dense(50, activation=tf.nn.selu),
        tf.keras.layers.Dense(25, activation=tf.nn.relu),
        tf.keras.layers.Dense(5,  activation=tf.nn.softmax)
    ])
        
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
        
    model.fit(inputTrain, outputTrain, epochs=5)
    test_loss, test_acc = model.evaluate(inputTest, outputTest)
    
    acc = acc.append({'Cluster':i,'Acc':test_acc,'Loss':test_loss},ignore_index=True)
    
    pred2= []
    predictions = model.predict(filteredLog.loc[:,inputCols])
    
    for ij in range(0,len(predictions)):
        expectedGame = 0
        for j in range(0,5):
            expectedGame += predictions[ij][j]*j
        
        pred2.append(expectedGame)
    
    gameLogs.loc[gameLogs['Cluster']==i,'ExpectedGame'] = pred2

    #pred = pred.append(pd.Series(pred2))    
        
gameLogs.to_csv('MegGameLogs.csv')