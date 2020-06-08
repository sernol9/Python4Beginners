#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05\Exercise 5.7.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05
# Created Date: Tuesday, June 2nd 2020, 6:11:29 pm
# Author: Olivia Serna
# Description: 
# -----
# Last Modified: Tue Jun 02 2020
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
def unique(*args):
    lista = []
    for i in args:
        if i not in lista:
            lista.append(i) 
    return lista

print(unique(1,1,1,2,2,2,2,3,3,3,3,4,4,4,4))