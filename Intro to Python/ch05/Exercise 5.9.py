#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05\Exercise 5.9.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05
# Created Date: Wednesday, June 3rd 2020, 6:10:51 pm
# Author: Olivia Serna
# Description: 
# -----
# Last Modified: Sat Jun 06 2020
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
word = 'Anitalava %$^ la tina'

def palindrome(word):
    found = True
    word = word.lower()
    array=[i for i in word if ord(i) in range(ord('a'),ord('z')+1)]
    index = 0
    while index < len(array) and palindrome:
        if array[index] != array.pop():
            found = False
        else:
            index += 1
    return found

print(f"{word} is palindrome? {palindrome(word)}")