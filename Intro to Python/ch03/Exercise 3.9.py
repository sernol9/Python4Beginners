#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch03\Exercise 3.9.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch03
# Created Date: Thursday, April 2nd 2020, 11:31:32 am
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
string = input("Please provide the integer: ")
length = len (string)
numero = int(string)
times = length - 1

while times >= 0:
    digito = numero // (10**times)
    numero = numero % (10** times)
    print (f'Digit {times +1} is {digito}')
    times = times - 1

