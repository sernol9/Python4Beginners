#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05\Exercise 5.12.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch05
# Created Date: Saturday, June 6th 2020, 5:38:27 pm
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
lista =[('A','B','C'),('D','E','F'),('G','H','I'),('J','K','L'),('M','N','O'),('P','R','S'),('T','U','V'),('W','X','Y')]

def perm_with_repetition(lista,digits,n):
    if n == 1:
        return lista[digits[n-1]-2]
    else:
        matrix = perm_with_repetition(lista,digits[0:n-1],n-1)
        matrix =[x+y for x in matrix for y in lista[digits[n-1]-2]]
        return (matrix)

digits = list(input("Please give me the phone number: "))
if '1' in digits or '0' in digits:
    print("The number can't have 0's or 1's")
else:
    digits = [int(i) for i in digits if ord(i) in range(ord('2'),ord('9')+1)]
    if len(digits) != 7:
        print("Eres un imbecil, el numero tiene k ser de 7 digitos")
    else:
        permutations = perm_with_repetition(lista,digits,len(digits))
        print(permutations,'\n', len(permutations))

vanity_word = input("You don't like your vanity phone number options? Give me your word: ")
your_number = ''
for i in vanity_word.upper():
    found, j = False, 0
    while not found and j < len(lista):
        if i in lista[j]:
            found = True
        else:
            j+=1
    your_number += str(j+2)
print(f'Your number is {your_number}')
