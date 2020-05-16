#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05\SelfCheck 187-4.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05
# Created Date: Thursday, May 7th 2020, 6:17:00 pm
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
integers1 = list(range(1,20))
integers2 = list(range(1,15))

suma = [s1+s2 for s1,s2 in zip(integers1, integers2)]

print (suma)