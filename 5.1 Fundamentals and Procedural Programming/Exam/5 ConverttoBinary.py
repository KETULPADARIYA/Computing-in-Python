number = 4
#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#The number above is given in base 10. Let's convert it to
#base 2 and print it in binary. For example, 215 can be written
#in binary as 11010111.
#
#Each digit of that string corresponds to a power of 2. The far

#Add your code here
n=number
k = ""
while number > 0:
    #print(number)
    if number // 2 != 0:
        k += "{}".format(round(int(number%2),1))
        number -= number%2
        #print(number)
        number /= 2
        #print(k[::-1])
    else :
        k +="{}".format(round(int(number%2),1))
        number -= number%2
        number /= 2
        #if number == 0:
         #   k +="0"
if n < 128:
    k +="0"
if n < 64:
    k +="0"
if n < 32:
    k +="0"
if n < 16:
    k +="0"
if n < 8:
    k +="0"
if n < 4:
    k +="0"

if n < 2:
    k +="0"
print(k[::-1])
if n < 64:
    k +="0"
if n < 32:
    k +="0"
if n < 16:
    k +="0"
if n < 8:
    k +="0"
if n < 4:
    k +="0"

if n < 2:
    k +="0"        


