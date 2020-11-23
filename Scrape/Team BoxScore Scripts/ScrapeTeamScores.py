# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 15:28:20 2019

@author: nbatt
"""

import GetSchaftBoxScores as s1
import PrepSchaftBoxScores as s2
import AddMilesAndDays as s3
import AddOffDefRatings as s4
import AddTeamPerformanceStats as s5
import AddDOR as s6
import AddSeasonPPGStat as s7


s1.getTeamBoxScores()
s2.formatTable()
s3.formatTable()
s4.formatTable()
s5.formatTable()
s6.formatTable()
s7.formatTable()


