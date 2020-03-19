# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 17:29:40 2019

@author: olivia
"""

# name = input("Enter your name\n")
# print (name)
try:
    hours = float(input ("Enter Hours:"))
    rate = float(input("Enter Rate:"))
    print ("Pay"+str(hours*rate))
except:
    print("Enter float numbers\n")