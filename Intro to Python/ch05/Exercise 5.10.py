#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05\Exercise 5.10.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05
# Created Date: Saturday, June 6th 2020, 1:28:35 pm
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

def perm(n,r):
    indeces = [str(x) for x in range(n)]
    if r == 1:
        return indeces
    else:
        matrix = perm(n,r-1)
        matrix =[x+y for x in matrix for y in indeces if y not in x]
        return (matrix)


word = list(input("Please type in your word: "))
lista =[]

for permutation in perm(len(word),len(word)):
    tupla = ""
    for i in permutation:
        tupla += (word[int(i)])
    if tupla not in lista:
        lista.append(tupla)
print(f'All possible permutations without repetition are: \n {lista}')


