#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch03\Exercise 3.16.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch03
# Created Date: Friday, April 3rd 2020, 6:34:07 pm
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
nstring = input("Please give me 10 numbers (no spaces): ")
max1 = int(nstring[0])
max2 = int(nstring[0])
for i in range (1, len(nstring)):
    if int(nstring[i]) > max1:
        max2 = max1
        max1 = int(nstring[i])
print ("Maximo 1: ", max1, "Maximo 2: ", max2)
