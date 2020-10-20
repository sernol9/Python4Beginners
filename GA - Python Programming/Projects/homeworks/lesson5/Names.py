#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Projects\homeworks\lesson5\Names.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Projects\homeworks\lesson5
# Created Date: Saturday, April 25th 2020, 9:41:20 am
# Author: Olivia Serna
# Description: 
# -----
# Last Modified: Sat Apr 25 2020
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

names = ['Alice', 'Bob', 'John', 'Tina']

with open("names.txt",'w') as file:
    for name in names:
        file.write(name + '\n')

