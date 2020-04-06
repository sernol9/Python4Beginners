#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch03\Exercise 3.12.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch03
# Created Date: Thursday, April 2nd 2020, 4:57:16 pm
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
palindrome = input ("Pls give me the integer number: ")
integer = int (palindrome)
power = len (palindrome) - 1

while  (power > 0) and ((integer // (10 ** power)) == (integer % 10)):
     integer = (integer % (10 ** power)) // 10
     power -= 2

if power <= 0:
   print ("It is a palindrome")
else:
    print ("It is not a palindrome")
