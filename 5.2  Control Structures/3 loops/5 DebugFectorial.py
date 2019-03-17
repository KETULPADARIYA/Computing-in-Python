num = 5

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#Write some code below that will print the factorial of num.
#Remember to remove any debug statements when you're ready
#to submit for credit.

result = 1
for i in range(num,0,-1):
    result *= i
print(result)
