#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05\Exercise 5.6.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05
# Created Date: Tuesday, June 2nd 2020, 6:05:32 pm
# Author: Olivia Serna
# Description: 
# -----
# Last Modified: Tue Jun 02 2020
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
def rotate(a,b,c):
    return c,a,b

a = 'Doug'
b = 22
c = 1984

for i in range(3):
    a, b, c = rotate(a,b,c)
    print (a,b,c)