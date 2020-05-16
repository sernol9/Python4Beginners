#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch04\Exercise 4.5p.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch04
# Created Date: Sunday, April 19th 2020, 10:15:01 pm
# Author: Olivia Serna
# Description: 
# -----
# Last Modified: Sun Apr 19 2020
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

from datetime import timedelta, date

def seconds_since_midnight(*args):
    hour_in_seconds = timedelta(hours=args[0]).total_seconds()
    minute_in_seconds = timedelta(minutes=args[1]).total_seconds()
    return hour_in_seconds + minute_in_seconds + args[2]

print (seconds_since_midnight(13,30,45))
 

