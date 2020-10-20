#Python class first program

#imports the ipython debugging module
import ipdb

def test():
    result = 5 * 4
    return result

#set a trace point
ipdb.set_trace()

name = input("What is your name:")
print ("Hello", name)
print ("Let's learn Python!")
result = 5 % 2
another_result = result * 100
print (another_result)
test_result = test()
print (test_result)