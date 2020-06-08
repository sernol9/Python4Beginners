#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05\Exercise 5.3.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05
# Created Date: Monday, June 1st 2020, 5:32:50 pm
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
listc_meters = [(x*0.0254,x) for x in [69,77,54]]
print(listc_meters)

listl_meters = list(map(lambda x : (x*0.0254,x),[69,77,54]))
print(listl_meters)