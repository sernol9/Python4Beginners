# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:18:35 2019

@author: olivia
"""

string = input("Please provide digits:")
length = len (string)
numero = int(string)
times = length - 1
output = ''

while times >= 0:
    digito = numero // (10**times)
    numero = numero % (10** times)
    output = output + str(digito) + '   '
    times = times - 1

print (output)


    
