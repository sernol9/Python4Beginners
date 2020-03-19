# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 22:27:13 2019

@author: olivia
"""

count = 0
total = 0
list=[]
while True:
    number = input("Enter a number:")
    try:
        total = float(number) + total
        count = count + 1
        list.append(number)
    except:
        if number == "done":
            break
        else:
            print("Invalid input")

if count == 0:
   average = 0
else:
   average = total/count
print ("Count:"+str(count))
print ("Total:"+str(total))
print ("Average:"+str(average))
print ("Min:"+str(min(list)))
print ("Max:"+str(max(list)))