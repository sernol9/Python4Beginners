#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05\Exercise 5.5.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05
# Created Date: Monday, June 1st 2020, 6:50:13 pm
# Author: Olivia Serna
# Description: 
# -----
# Last Modified: Mon Jun 01 2020
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
alphabet = 'abcdefghijklmnopqrstuvwxyz'

print (alphabet[0:int(len(alphabet)/2)])
print (alphabet[:int(len(alphabet)/2)])
print (alphabet[int(len(alphabet)/2)+1:len(alphabet)])
print (alphabet[int(len(alphabet)/2)+1:])
print(alphabet[::2])
print(alphabet[::-1])
print(alphabet[::-3])