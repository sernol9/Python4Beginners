#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05\Exercise 5.32.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05
# Created Date: Sunday, June 28th 2020, 8:24:47 pm
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
import sys, matplotlib.pyplot as plt, random, statistics, numpy as np, seaborn as sns

if __name__ == "__main__":
    rolls= int(sys.argv[1])
    total_rolls = [random.randrange(1,7) + random.randrange(1,7) for i in range(rolls)]
    values, frequencies = np.unique(total_rolls,return_counts=True)
    sns.set_style("whitegrid")
    axes = sns.barplot(y = values, x = frequencies, orient='h',  palette = 'bright')
    axes.set_title(f"Tossing a coin {len(total_rolls):,} Times")
    axes.set(ylabel='Die Value', xlabel='Frequency')
    axes.set_xlim(right=max(frequencies)* 1.10)


    for bar,frequency in zip(axes.patches, frequencies):
        text_y = bar.get_y() + bar.get_height()
        text_x = bar.get_width()
        text = f'{frequency:,}\n{frequency/len(total_rolls):.3%}'
        axes.text(text_x, text_y, text, fontsize =10, ha='left', va='bottom')


    plt.show()