#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05\Exercise 5.15.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05
# Created Date: Monday, June 8th 2020, 4:28:00 pm
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

invoice = [(83,'Electrical sander',7,57.98),(24,'Power Saw',18,99.98),
           (7,'Sledge Hammer',11,21.50),(77,'Hamer',76,11.99),(39,'Jig Saw',3,75.90)]

from operator import itemgetter

invoice_sorted = sorted (invoice,key = itemgetter(1))
print(invoice_sorted)

invoice_sorted = sorted (invoice,key = itemgetter(3))
print(invoice_sorted)

invoice_sorted = sorted(list(map(lambda tuple: tuple[1:3],invoice)),key = itemgetter(1))
print(invoice_sorted)

invoice_sorted = sorted(list(map(lambda tuple: tuple[1:4:2],invoice)),key = itemgetter(1))
print(invoice_sorted)

invoice_sorted = sorted(list(filter (lambda range: range[1]>= 20 and range[1] <= 70,map(lambda tuple: tuple[1:4:2],invoice))),key = itemgetter(1))
print(invoice_sorted)

total_invoice = 0
for item in invoice:
    total_invoice += item[3]

print (total_invoice)