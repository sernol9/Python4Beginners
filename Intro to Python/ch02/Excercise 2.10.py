# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:18:35 2019

@author: olivia
"""

string = str(input("Please provide three digits:"))
length = len (string)
numero = int (string)
times = 1
suma = 0

while times <= length:
    digito = numero % 10
    suma = suma + digito
    numero = numero // 10
    times = times + 1
print ("Max:",max(string),"Min:",min(string),"Sum:",suma,"Avg",suma/length)

    
