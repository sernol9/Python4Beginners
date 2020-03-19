Celsius = input ("Please provide the Celsius degree to convert\n")
try: 
    Farenheit = float (Celsius)*1.8 + 32
    print (str(Farenheit)+"o")
except:
    print ("Please provide a float number\n")


