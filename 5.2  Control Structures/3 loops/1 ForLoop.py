mystery_int = 5

#In math, factorial is a mathematical operation where an
#integer is multipled by every number between itself and 1.
#For example, 5 factorial is 5 * 4 * 3 * 2 * 1, or 120.
#Factorial is represented by an exclamation point: 5!
#
#Use a for loop to calculate the factorial of the number
#given by mystery_int above. Then, print the result.
#
#Hint: Running a loop from 1 to mystery_int will give you
#all the integers you need to multiply together. You'll need
#to track the total product using a variable declared before
#starting the loop, though!


#Add your code here!
multiplication=1
for i in range(1,mystery_int+1):
    multiplication=i*multiplication
print(multiplication)
mystery_string = "CS1301"

#Write a for-each loop that lists each character in
#mystery_string with its index. For example, if the string
#was "abc", the output would be:
#0 a
#1 b
#2 c
#
#Note that the first item is #0, the second is #1, and so
#on! We'll talk about why that is in Unit 4.
#
#Hint: You'll need a separate variable to keep track of how
#many letters you've printed! You may not use the range
#function on this problem.


#Add your code here!
n=-1
for i in mystery_string:
    if i != "":
        n+=1
    print(n,i)
