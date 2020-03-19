# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 17:14:28 2019

@author: olivia
"""

def space (lenght):
   space = 1
   espacio = ''
   while (space < (8-lenght)):
        espacio = espacio + ' '
        space = space + 1
   return espacio;
    
number = 1
print('number  square  cube    ')
for number in range(1,5):
    square = str( number ** 2)
    cube = str(number ** 3)
    base = str(number)
    base = base + space(len(base))
    square = square + space(len(square))
    cube = cube + space(len(cube))
    print (base, square, cube)

number = 1
print('number','\t\t','square','\t','cube')
for number in range(1,5):
    square = str( number ** 2)
    cube = str(number ** 3)
    base = str(number)
    base = base + space(len(base))
    square = square + space(len(square))
    cube = cube + space(len(cube))
    print (base,'\t',square,'\t',cube)
    
    