#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch04\snippets_py\Exercise 4.12.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch04\snippets_py
# Created Date: Sunday, April 26th 2020, 5:13:51 pm
# Author: Olivia Serna
# Description: 
# -----
# Last Modified: Sun Apr 26 2020
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
import time, sys, random

ERASE_LINE = '\x1b[2K'

def hare ():
    step = random.randint(1,10)
    if step <= 5:
        return 3
    elif step <= 7:
        return -6
    else:
        return 1

def tortoise ():
    step = random.randint(1,10)
    if step <= 2:
        return 0
    elif step <= 4:
        return 9
    elif step <= 5:
        return -12
    elif step <=8:
        return 1
    else:
        return 2

def game():
    hp, tp = 1, 1

    print(""" BANG !!!!!
              AND THEY'RE OFF !!!!!""")
    print ("\nS", end = "")
    for i in range (1,69):
        print(" ", end ="")
    print ("F")

    while hp < 70 and tp < 70:
        hp += hare()
        tp += tortoise()
        if hp < 1:
            hp = 1
        if tp < 1:
            tp = 1
        if hp > tp:
            counter1 = tp
            counter2 = hp
            loser = "T"
            winner = "H"
        else:
            counter1 = hp
            counter2 = tp
            loser = "H"
            winner = "T"
        
        if hp == tp:
            print(f'{"OUCH!!!":>{counter1-1}}', end="\r")
        else:    
            print(f'{loser:>{counter1-1}}{winner:>{counter2-counter1-1}}', end="\r")

        time.sleep(.5)
        sys.stdout.write(ERASE_LINE)

    if hp >= 70 and tp >= 70:
        print("It's a tie")
    elif hp >= 70:
        print("\nHare wins. Yuch")
    else:
        print("\nTORTOISE WINS!!! YAY !!! ")
    
game()