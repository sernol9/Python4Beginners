#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Projects\homeworks\lesson2\future.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Projects\homeworks\lesson2
# Created Date: Friday, April 3rd 2020, 3:35:50 pm
# Author: Olivia Serna
# Description: 
# -----
# Last Modified: Fri Apr 03 2020
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
from datetime import datetime, timedelta

diff = int(input("How many days into the future: "))

a = datetime.now() + timedelta(days = diff)
weekday = a.strftime("%A")

print(f"{diff} day into the future, the date will be {a} and it will be {weekday}")