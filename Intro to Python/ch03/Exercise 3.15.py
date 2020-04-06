#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch03\Exercise 3.15.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch03
# Created Date: Friday, April 3rd 2020, 1:43:55 am
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
iteration = int(input("Please give me the number of terms to calculate (>1): "))
e = 1
for index in range(2, iteration+1):
    factorial = 1
    for i in range (1,index):
        factorial *= i
    e += 1/factorial

print("El valor de e es: ",e)