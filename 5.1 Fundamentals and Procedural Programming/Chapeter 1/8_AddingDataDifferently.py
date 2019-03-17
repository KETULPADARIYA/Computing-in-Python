#Early feedback suggests the exercise immediately following this
#is a bit difficult. You've seen everything you need to know to do
#it, but it hasn't been the focus yet. So, this worked example shows
#the solution to a similar problem to help you figure out 2.2.9 Coding
#Exercise 1.
#
#Imagine you are trying to print a person's height in the imperial
#system. You have two variables: feet and inches. You want to print
#the height in the typical style -- for example, if feet was 5 and
#inches was 4, you'd want to print 5'4. We're leaving off the
#quotation mark at the end to keep things simple.

#How would we do that?

#First, let's create the variables.
feet = 5
inches = 4

#What happens if we just add them together?

print("Just adding them together:")
print(feet + inches)
print() #This just prints a blank line to make the output easy to read.

#Yikes! That's not what we want. It just added 5 and 4 and got 9. We
#don't want to add them as numbers, we want to add them as text, 
#putting them together.

#So, let's convert them to strings first. That will force Python to
#treat them like text instead of like numbers.

feetAsString = str(feet)
inchesAsString = str(inches)

#Now what happens if we add them?
print("Adding them as strings:")
print(feetAsString + inchesAsString)
print() #This just prints a blank line to make the output easy to read.

#We're getting closer! Instead of adding them as numbers, it put them
#alongside each other as text. Now we just need to add the apostrophe.

print("With the apostrophe:")
print(feetAsString + "'" + inchesAsString)
print()

#We're done! By converting feet and inches to strings, we can just add
#the numbers and the punctuation marks together as text.

#What would have happened, though, if we had tried that last line
#without converting feet and inches to strings? Uncomment the following
#line, then run it to find out:

#print(feet + "'" + inches)

#An error! feet and inches are both numbers, and Python doesn't know how
#to add those to strings. We have to convert them to strings to add them.

#We'll discuss this more in Chapters 2.4 and 4.2.
