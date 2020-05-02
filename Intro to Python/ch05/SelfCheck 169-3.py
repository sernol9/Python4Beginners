#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05\SelfCheck 169-3.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05
# Created Date: Friday, May 1st 2020, 4:05:53 pm
# Author: Olivia Serna
# Description: 
# -----
# Last Modified: Fri May 01 2020
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

list = list(range(1,16))
print(list[1::2])

list[5:10]= [0] * len(list[5:10])
print(list)

list [5:] = []
print(list)

list[:] = []
print(list)