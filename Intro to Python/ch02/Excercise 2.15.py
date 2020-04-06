# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:18:35 2019

@author: olivia

First time making changes to the file and using GitHub
"""

numero1 = float(input('Please provvide a float number:'))
numero2 = float(input('Please provvide a float number:'))
numero3 = float(input('Please provvide a float number:'))

small = numero1
mid = numero1
big = numero1

if big <= numero2:
    big = numero2
    if big <= numero3:
        big = numero3
        if numero2 <= small:
            small = numero2
        else:
            mid = numero2
    else:
        if numero3 < small:
            small = numero3
        else:
            mid = numero3
else:
    if numero2 < numero3:
        small = numero2
        mid = numero3
    else:
        mid = numero2
        small = numero3
        
print (big,mid,small)
        
    
    




    

    
