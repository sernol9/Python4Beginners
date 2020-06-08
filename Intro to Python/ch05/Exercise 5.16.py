#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05\Exercise 5.16.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05
# Created Date: Monday, June 8th 2020, 5:39:25 pm
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

random_list = list(filter(lambda item: ord(item) in range(ord('a'),ord('z')+1),list(input("Please provide 20 random letters between a and f: "))))

print(sorted(random_list),'\n', sorted(random_list,reverse=True))

unique_list =[]
for item in random_list:
    if item not in unique_list:
        unique_list.append(item)
print (unique_list)