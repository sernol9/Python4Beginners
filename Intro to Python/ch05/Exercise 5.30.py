#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05\Exercise 5.30.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05
# Created Date: Sunday, June 28th 2020, 5:53:50 pm
# Author: Olivia Serna
# Description: 
# -----
# Last Modified: Sun Jun 28 2020
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

rolls = [random.randrange(1,7) for i in range (600)]
values, frequencies = np.unique(rolls,return_counts=True)
sns.set_style("whitegrid")
axes = sns.barplot(x = values, y = frequencies, palette = 'bright')
axes.set_title(f"Rolling a Six-Sided Die {len(rolls):,} Times")
axes.set(xlabel='Die Value', ylabel='Frequency')
plt.show()