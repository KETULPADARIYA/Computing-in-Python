hungry = True
coworkers_going = False
brought_lunch = False

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Imagine you're deciding whether or not to go out to lunch.
#You only want to go if you're hungry. If you're hungry, even
#then you only want to go if you didn't bring lunch or if
#your coworkers are going. If your coworkers are going, you
#still want to go to be social even if you brought your lunch.
#
#Write some code that will use the three boolean variables
#defined above to print whether or not to go out to lunch.
#It should print True if hungry is True, and either
#coworkers_going is True or brought_lunch is False.
#Otherwise, it should print False.


#Write your code here!
print(hungry and ((not brought_lunch)  or coworkers_going) )
