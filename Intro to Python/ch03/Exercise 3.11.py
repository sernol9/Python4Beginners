#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch03\Exercise 3.11.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch03
# Created Date: Thursday, April 2nd 2020, 12:03:41 pm
# Author: Olivia Serna
# Description: 
# -----
# Last Modified: Thu Apr 02 2020
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
flag = 0
c_miles = c_gallons = 0

while flag == 0:
    gallons = float(input("Enter the gallons used (-1 to end): "))
    if (gallons != -1.0):
       c_gallons += gallons
       miles = float(input("Enter the miles driven: "))
       c_miles += miles
       print("The miles/gallon for this tank was: ",miles/gallons)
    else:
       flag = -1

if c_gallons != 0: 
    print("The overall average miles/gallon was",c_miles/c_gallons)

