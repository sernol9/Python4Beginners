# -*- coding: utf-8 -*-
try:
    hrs = float (input('Please provide the # of hours worked:'))
    rate = float (input('Please provide the rate to be used:'))
    if (hrs > 40):
        pay = ((40)*rate) + ((hrs-40)*rate*1.5)
    else:
        pay = (hrs*rate) 
    print('The total payment is:',pay)
except:
    print('Please provide a number')

