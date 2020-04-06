"""
Created on Fri Mar  6 18:54:31 2020

@author: olivia
"""
# fig03_03.py
"""Using nested control statements to analyze examination results."""

# initialize variables
passes = 0  # number of passes

# process 10 students
for student in range(10):
    # get one exam result
    result = int(input('Enter result (1=pass, 2=fail): '))
    counter = 0
    while (result != 1) and (result != 2):
          counter += 1
          result = int(input('You have not entered the correct number\nEnter result (1=pass, 2=fail): '))
    if result == 1:
        passes = passes + 1
    

# termination phase
print('Passed:', passes)
print('Failed:', 10 - passes)

if passes > 8:
    print('Bonus to instructor')

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
