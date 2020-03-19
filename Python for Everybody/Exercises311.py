# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 20:53:57 2019

@author: olivia
"""
#try:
 #   hours = float(input("Enter Hours:"))
 #   rate = float(input("Enter Rate:"))
 #   if hours < 40:
 #       pay = (hours * rate)
 #   else:
 #       pay = (rate*40) + ((rate*1.5)*(hours -40))
 #   print("Pay:"+str(pay))
#except:
 #   print("Please enter float values\n")
 
try:
   score = float(input("Enter Score:"))
   if score >= 0.9:
       grade = "A"
   elif score < 0.8:
          if score < 0.7:
              if score >= 0.6:
                  grade = "D"
              else:
                  grade = "F"
          else:
               grade = "C"
   else:
            grade = "B"
       
   print (grade)
except:
   print("Bad score\n")