# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 12:10:59 2019

@author: nbatt
"""

import os

files = (os.listdir())

for i in files:
    if i[-1] == 'R' or i[-1] == 'y':
        print(i)