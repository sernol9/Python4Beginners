#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch03\Exercise 3.7.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch03
# Created Date: Thursday, April 2nd 2020, 10:51:14 am
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

print('number  square  cube')

for number in range(6):
    print (f"{number:>6}{number**2:>8}{number**3:>6}")