#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch04\snippets_py\Exercise 4.10.py
# Project: c:\Users\olivi.000\Dropbox\Public\My Library\IT\SW Programming\sego\Intro to Python\ch04\snippets_py
# Created Date: Sunday, April 26th 2020, 4:02:41 pm
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
import random

def game (number):
    choice, tries = 0, 0
    w2p = True
    print ("Random number: ",number)
    while choice != number and w2p:
        try:
            choice = int(input("Guess my number between 1 and 10 with the fewest guesses: "))
            tries +=1
        except ValueError as err:
            print("You did not enter an integer try again: %s" % err)
            continue
        if choice != number:
            if choice > number+2:
               print("Too high. Try again")
            elif choice < number-2:
               print("Too low. Try again")
            else:
               print("Close but not enough")
            w2p = (False if (input("Do you want to try again (Y/N)? ") == "N") else True)
        else:
             print("Congratulations. You guessed the number!")
             if tries <=5:
                 print("Either you know the secret or you got lucky!")
             else:
                print("You should be able to do better next time!")
    return

w2p = True
while w2p:
    game(random.randint(1,10))
    w2p = (False if input("Do you want to play again (Y/N)? ") == "N" else True)

    
        
