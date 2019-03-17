temperature = -3.7
celsius = True

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Above are given two variables. temperature is a float that
#holds a temperature. celsius is a boolean that represents
#whether the temperature is in Celsius; if it's False, then
#the given temperature is actually in Fahrenheit.
#
#Add some code below that prints "Freezing" if the values
#above represent a freezing temperature, and "Not freezing"
#if they don't.
#
#In Celsius, freezing is less than or equal to 0 degrees.
#In Fahrenheit, freezing is less than or equal to 32 degrees.


#Add your code here!
if (temperature*celsius != 0) and (temperature*celsius<=0):
    print("Freezing")
elif (temperature*celsius == 0) and (temperature<=32):
   print("Freezing")
else :
    print("Not freezing")

