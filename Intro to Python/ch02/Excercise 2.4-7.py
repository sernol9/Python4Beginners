# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:30:02 2020

@author: olivia
"""
"""Exercise 2.5"""
pi = 3.1416
r = 2
print ('Diameter =', 2*r,'\nCircumference =',2*pi*r,'\nArea=',pi*r**2)

"""Exercise 2.6"""
integer = int(input('Please provide and integer: '))
if integer % 2 == 0 :
    print ('The integer is even')
else:
    print ('The integer is odd')
    

"""Exercise 2.7"""
if 1024 % 4 == 0 :
    print ('4 is a multiple of 1024')
else:
    print('4 is not a multiple of 1024')
    
if 10 % 2 == 0 :
    print ('2 is a multiple of 10')
else:
    print('2 is not a multiple of 10')