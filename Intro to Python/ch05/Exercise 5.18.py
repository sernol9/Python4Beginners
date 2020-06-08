#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05\Exercise 5.18.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05
# Created Date: Monday, June 8th 2020, 6:14:42 pm
# Author: Olivia Serna
# Description: 
# -----
# Last Modified: Mon Jun 08 2020
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
numbers =[2,3,4,5,6,7,8,9,10]
triples = sum(list(map(lambda number: number *3,filter(lambda number: number % 2 == 0, numbers))))
print(triples)

triples =[number * 3 for number in numbers if number % 2 == 0 ]

print(sum(triples))