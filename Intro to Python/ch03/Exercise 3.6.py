#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch03\Exercise 3.6.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch03
# Created Date: Wednesday, March 25th 2020, 4:14:24 pm
# Author: Olivia Serna
# Description: Turing Test
# -----
# Last Modified: Wed Mar 25 2020
# Modified By: Olivia Serna
# -----
# Copyright (c) 2020 OLI CO. LTD.
# 
# Know thy self, know thy enemy. A thousand battles, a thousand victories
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
# 2020-03-25	OS  Final script version
###

print("What is your problem?")
answer = input ("Have you had this problem before (yes or no)? ")
print(("Well you have it again" if answer == "yes" else "well, you have it now"), end='...sucker!')
