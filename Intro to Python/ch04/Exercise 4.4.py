#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch04\Exercise 4.4.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch04
# Created Date: Sunday, April 19th 2020, 10:01:08 pm
# Author: Olivia Serna
# Description: 
# -----
# Last Modified: Sun Apr 19 2020
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

def mystery (x):
    y = 0
    for value in x:
        y += value ** 2
    return y

print (mystery([1,2,3,4,5]))
