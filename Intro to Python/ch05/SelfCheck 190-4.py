#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05\SelfCheck 190-4.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05
# Created Date: Thursday, May 7th 2020, 6:21:42 pm
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
t = [[10,7,3],[20,4,17]]
suma, counter = 0, 0


for i in t:
    for j in i:
        suma += j
        counter += 1

avg = suma / counter

print (suma, avg)

suma, counter = 0, 0

for i in t:
    suma += sum(i)
    counter += len(i)

print (suma, suma/counter)