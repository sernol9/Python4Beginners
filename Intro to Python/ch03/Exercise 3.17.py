#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch03\Exercise 3.17.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch03
# Created Date: Sunday, April 12th 2020, 9:34:43 pm
# Author: Olivia Serna
# Description: 
# -----
# Last Modified: Mon Apr 13 2020
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

for i in range (1,5):
    for j in range(10):
        if i % 2 == 1:
            counter1 = j
            counter2 = 9 -j
        else:
            counter1 = 9 - j
            counter2 = j
        if i < 3:
            char1 = "*"
            char2 = " "
        else:
            char1 = " "
            char2 = "*"
        for l in range(counter1):
            print(char1, end='')
        for k in range(counter2):
            print(char2, end='')
        print('\n')
    print('\n')