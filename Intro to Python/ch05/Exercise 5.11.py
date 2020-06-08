#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05\Exercise 5.11.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05
# Created Date: Saturday, June 6th 2020, 2:16:41 pm
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
word = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def summarise_letter(word):
    word  = word.lower()
    array =[i for i in word if ord(i) in range(ord('a'),ord('z')+1)]
    lista =[]
    for l in range(ord('a'),ord('z')+1):
        n = 0
        for i in array:
            if i == chr(l):
               n += 1
        if n != 0:
            lista.append(tuple([chr(l),n]))
    return (lista)

frequency = summarise_letter(word)
all_abc =('All' if (len(frequency)) == 26 else 'Not All')

print(f"The letters in '{word}' with their frequencies are: \n {frequency} \nThis word has {all_abc} letters in the alphabet")