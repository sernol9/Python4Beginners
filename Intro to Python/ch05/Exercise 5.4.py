#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05\Exercise 5.4.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05
# Created Date: Monday, June 1st 2020, 5:47:03 pm
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

order = 1

matrix = [[0]*3 for i in range(2)]

print('\t', end='')
for i in range(len(matrix[0])):
    print(i+1,end=' ')
print('\n')

for i in range(2):
    print (i+1,end='\t')
    for j in range (3):
        matrix [i][j] = order
        print(matrix[i][j], end=' ')
        order += 1
    print('\n')

print (matrix)
