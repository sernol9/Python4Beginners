#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch03\Exercise 3.8.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch03
# Created Date: Thursday, April 2nd 2020, 11:05:53 am
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

list = []

for iteration in range(4):
    list.append(float(input("Please provide a number: ")))

suma = sum(list)
print ("Min:",min(list),"Max:",max(list),"Sum:",suma,"Avg",suma/iteration)