#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Projects\homeworks\deaths.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Projects\homeworks
# Created Date: Saturday, April 11th 2020, 9:09:22 am
# Author: Olivia Serna
# Description: 
# -----
# Last Modified: Sat Apr 11 2020
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
import sys
import csv

def read_file (file_pointer):
    with open (file_pointer, newline = '') as csvfile:
         return list(csv.DictReader(csvfile))

def disease_type (list_disease):
    unique_disease = set ("")
    for row in list_disease:
        unique_disease.add(row['disease_condition']) 
    list_disease = list(unique_disease)
    list_disease.sort()
    return (list_disease)

if __name__ == '__main__':
   dictionary  = read_file(sys.argv[1])
   list_disease = disease_type(dictionary)
   for i, row in enumerate(list_disease):
       print (list_disease[i])