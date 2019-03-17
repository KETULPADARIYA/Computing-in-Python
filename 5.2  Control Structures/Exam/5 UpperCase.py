the_string = "I'm a Ramblin' Wreck"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#Write some code that will capitalize and print the value of
#the_string. For example, for the initial value of the_string
#above, it should print "I'M A RAMBLIN' WRECK".
#
#You can capitalize a string by calling the_string.upper().
#This will return a capitalized version of the string. (Note
#that this will _not_ modified the_string, but rather just
#return the result if it were to be capitalized.)
#
#However, the_string might not actually be a string! It might
#be an integer, a float, or something else. If that happens,
#then calling the_string.upper() will cause an AttributeError
#to occur. Catch this error and print "The variable was not
#a string!"
#
#Note that you may not use any conditionals in your answer.
#Note also that you should not assume that every error that
#occurs is an Attribute Error! Any other errors should
#not be caught.


#Add your code here!
try:
    t=the_string.upper()
    print(t)
except AttributeError:
    print("The variable was not a string!")




