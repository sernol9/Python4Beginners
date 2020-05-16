#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch04\snippets_py\Exercise 4.9.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch04\snippets_py
# Created Date: Tuesday, April 21st 2020, 11:13:14 pm
# Author: Olivia Serna
# Description: 
# -----
# Last Modified: Thu Apr 23 2020
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

def C2F (c_degrees):
    return (c_degrees * (9/5)) + 32 

print ("Farenheit  Celcius")
print ("------------------")
for i in range (101):
    print (f'{i:>9.1f}  {C2F(i):>7.1f}')
