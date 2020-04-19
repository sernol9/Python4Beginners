#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Projects\homeworks\lesson4\passwords.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Projects\homeworks\lesson4
# Created Date: Friday, April 10th 2020, 11:05:58 pm
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
import ipdb

def read_file (file_pointer):
    with open( file_pointer) as file:
         read_data = file.read()
    return read_data

def convert_to_list (string):
    return string.split('\n')

def search_passwd (password_list, password):
    i = 0 
    found = False
    while i < len(password_list) and found == False:
        if password_list[i] ==  password:
            found = True
            print(f"Oh oh! {password} is at rank {i+1} of the most common passwords")
        i +=1
    if found == False:
        print("God job! your password is very uncommon!")
          

if __name__ == '__main__':
    password = sys.argv[2]
    password_list= read_file(sys.argv[1])
    password_list = convert_to_list (password_list)
    search_passwd(password_list, password)
   







