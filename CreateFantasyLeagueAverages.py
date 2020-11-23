# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 01:47:05 2019

@author: nbatt
"""

import pandas as pd


df = pd.read_csv('PlayerDirectory.csv',index_col='Player')
df['LeagueFPTS'] = -0.5*(df.FGA-df.FG)+-0.25*(df.FTA-df.FT)+df.ORB*1.25+df.DRB+df.AST*1.5+df.STL*2.75+df.BLK*2.75 - df.TOV + df.PTS
df['LeaguePrevRules'] = -0.5*(df.FGA-df.FG)+-0.5*(df.FTA-df.FT)+df.ORB*1.5+df.DRB+df.AST*1.25+df.STL*2.75+df.BLK*2.75 - df.TOV + df.PTS
