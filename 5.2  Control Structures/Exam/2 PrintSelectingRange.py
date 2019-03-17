minimum = 5
maximum = 14
even = True

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#Write a loop (we suggest a for loop) that prints the numbers
#from minimum to maximum, including minimum and maximum
#themselves. If even is True, print only the even numbers.
#If even is False, print only the odd numbers. You may assume
#minimum will always be less than maximum.
#
#With the initial values for minimum, maximum, and even above,
#this should print 6, 8, 10, 12, 14 -- each number would be on
#its own line, no commas.


#Add your code here!
k=""
for i in range(minimum,maximum+1,1):
    if even :
        if i %2 ==0 :
            print(i)
    else:
        if i %2 ==1:
            print(i)
