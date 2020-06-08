#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05\Exercise 5.8.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05
# Created Date: Tuesday, June 2nd 2020, 6:22:27 pm
# Author: Olivia Serna
# Description: 
# -----
# Last Modified: Wed Jun 03 2020
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
import math

primes = ['True' for i in range(1001)]
print (len(primes))

for i in range (2,int(math.sqrt(1000))+1):
    if primes[i] == 'True':
        for multiples in range(i**2,1001,i):
            primes[multiples]='False'


cuantos = 0 
for i in range(len(primes)):
    if primes[i] == 'True':
        cuantos += 1
        print(i, primes[i])
    
print ("Primos:", cuantos)