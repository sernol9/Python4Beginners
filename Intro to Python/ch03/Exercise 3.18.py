#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch03\Exercise 3.18.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch03
# Created Date: Sunday, April 12th 2020, 10:17:49 pm
# Author: Olivia Serna
# Description: 
# -----
# Last Modified: Sun Apr 12 2020
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
for i in range(10):
    for m in range(4):
        if m == 0:
            counter1 = i + 1
            counter2 = 9 - i
        elif m == 1:
            counter1 = 10 - i
            counter2 = i
        elif m == 2:
            counter2 = 10 - i
            counter1 = i
        else:
            counter2 = i + 1
            counter1 = 9 - i
        if m < 2:
            char1 = "*"
            char2 = " " 
        else:
            char1 = " "
            char2 = "*"  
        for j in range(counter1):
            print (char1, end='')
        for k in  range(counter2):
            print (char2, end='')
        print ("   ",end='')
    print('\n')

