#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Projects\homeworks\lesson1\debugging.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Projects\homeworks\lesson1
# Created Date: Friday, March 27th 2020, 6:23:30 pm
# Author: Olivia Serna
# Description: 
# -----
# Last Modified: Fri Mar 27 2020
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
import ipdb; 

ipdb.set_trace()
today = datetime.now()
future = today + timedelta(seconds=100000)
difference = future - today
print (difference)