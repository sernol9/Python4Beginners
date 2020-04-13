#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch03\Exercise 3.20.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch03
# Created Date: Monday, April 13th 2020, 6:43:56 pm
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
import sys

binary_str = input("Please provide a binary number: ")
try:
    binary_num = int(binary_str)
except Exception as err:
    print (f"You did not enter a number: {err}")
    sys.exit

decimal_num = 0

for i in range(len(binary_str)-1,-1,-1):
    decimal_num += int(binary_str[i]) * 2**(len(binary_str)-i-1)
print ("The decimal number is: ",decimal_num)


