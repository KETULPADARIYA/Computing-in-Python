mystery_list = ["Taylor Swift", "Twenty Two", "Georgia Tech"]
#Above is a list of strings. Don't worry if this syntax is a
#little unfamiliar, we'll talk you through it and then cover
#it more in chapter 4.3.
#Write some code that will count the number of instances of
#the letter 't' in the list of strings. Count both capital
#'T' and lower-case 't'. Then, print the number of instances
#of the letter 't'.
#For example, with the list declared above, you would print
#6: two in the first string, three in the second, one in the
#third.
#
#Because we haven't used lists very extensively, we've
#gotten you started. The loop below will iterate through each
#string in the list. Next, you want to iterate through each
#letter in the current string, check if it's a t, and
#increment a counter if so.


#You'll want to add some code before the loop here.
sum = 0
for string in mystery_list:
    #Add your code to read through the string and count the
    #t's and T's here!
    for i in string:
        if i=="t":
            sum+=1
        if i=="T":
            sum+=1

#Add some code here to print the final tally!
print(sum)




