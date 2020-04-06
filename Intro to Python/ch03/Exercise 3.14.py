#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch03\Exercise 3.14.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch03
# Created Date: Friday, April 3rd 2020, 12:56:09 am
# Author: Olivia Serna
# Description: 
# -----
# Last Modified: Fri Apr 03 2020
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
term = int(input("Please give me the number of terms to use in the calculation (>1): "))
pi = 4
iteration = 2

print ("Term  Value of PI")
print ("-----------------")

for index in range(3, term * 2, 2):
    if (iteration % 2) == 0 :
        pi -= (4 / index)
    else:
        pi += (4 / index)
    print (f'{(iteration):>4}{pi:>13.4f}')
    iteration += 1