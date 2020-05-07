#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch04\Exercise 4.6.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch04
# Created Date: Sunday, April 19th 2020, 11:07:00 pm
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


def average (*args):
    if len(args) == 0:
        print ("average() missing 1 required positional argument")
        return
    else:
        return sum(args) / len (args)

print("Average: ",average())