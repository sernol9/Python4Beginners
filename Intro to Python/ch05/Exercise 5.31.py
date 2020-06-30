#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05\Exercise 5.31.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05
# Created Date: Sunday, June 28th 2020, 8:14:47 pm
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

toss = [random.randrange(1,3) for i in range (200)]
values, frequencies = np.unique(toss,return_counts=True)
sns.set_style("whitegrid")
axes = sns.barplot(x = values, y = frequencies, palette = 'bright')
axes.set_title(f"Tossing a coin {len(toss):,} Times")
axes.set(xlabel='Die Value', ylabel='Frequency')

axes.set_ylim(top=max(frequencies)* 1.10)

for bar,frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency/len(rolls):.3%}'
    axes.text(text_x, text_y, text, fontsize =11, ha='center', va='bottom')
plt.show()