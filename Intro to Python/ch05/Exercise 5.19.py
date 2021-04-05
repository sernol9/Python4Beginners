#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05\Exercise 5.20.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05
# Created Date: Monday, June 8th 2020, 6:23:26 pm
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
names =[('Olivia','Jones'),('Rafa','Mayoral'),('Van','Jones'),('Nano','Mayoral'),('John','White'),('John','Black')]

Jones = list(filter(lambda tuple: tuple[1] == 'Jones',names))
print(Jones)