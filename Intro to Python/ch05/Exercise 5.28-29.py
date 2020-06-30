#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05\Exercise 5.28.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05
# Created Date: Saturday, June 27th 2020, 7:41:12 pm
# Author: Olivia Serna
# Description: 
# -----
# Last Modified: Sat Jun 27 2020
# Modified By: Olivia Serna
# -----
# Copyright (c) 2020 OLI CO. LTD.
# 
# Know thy self, know thy enemy. A thousand battles, a thousand victories
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
###
import matplotlib.pyplot as plt, random, statistics, numpy as np, seaborn as sns

responses = [random.randrange(1,6) for i in range (20)]

values, frequencies = np.unique(responses,return_counts=True)

percentages = [i/20 for i in frequencies]

print (f"""The minimum response is: {min(values)} 
           The maximum response is: {max(values)}
           The population's range response is {max(values)-min(values)}
           The meean response is: {statistics.mean(values)}
           The median response is: {statistics.median(values)}
           The population's response variance is: {statistics.pvariance(values)}
           The population's response std deviation is: {statistics.pstdev(values)}""")

plt.cla()
title = "Response frequencies and percentages"
sns.set_style("whitegrid")
axes = sns.barplot(x = frequencies, y = percentages, palette = 'bright')
axes.set_title(title)
plt.show()