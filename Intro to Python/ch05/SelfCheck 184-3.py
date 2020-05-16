#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05\SelfCheck 184-3.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05
# Created Date: Thursday, May 7th 2020, 5:56:16 pm
# Author: Olivia Serna
# Description: 
# -----
# Last Modified: Thu May 07 2020
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
numbers = list(range(1,16))

print(list(filter(lambda x: x % 2 == 0,numbers)))
print(list(map(lambda x: x**2,numbers)))
print(list(map(lambda x: x**2,list(filter(lambda x: x % 2 == 0,numbers)))))