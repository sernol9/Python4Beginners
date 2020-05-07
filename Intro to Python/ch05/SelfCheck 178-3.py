#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05\SelfCheck 178-3.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05
# Created Date: Friday, May 1st 2020, 5:26:40 pm
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

colours = ['green', 'orange', 'violet']
colours.insert(colours.index('violet'),'red')
print(colours)
colours.append('yellow')
colours.reverse()
print(colours)
colours.remove('orange')
print(colours)