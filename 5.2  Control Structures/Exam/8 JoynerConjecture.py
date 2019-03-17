#The Joyner Conjecture is a not-at-all famous mathematical
#series inspired by the Collatz Conjecture for use in this
#class.
#
#The Joyner Conjecture proceeds as follows:
#
#Start with any number. If the number is divisible by 3,
#divide it by 3. Otherwise, add 2 to the number. Eventually,
#no matter what number you begin with, this series will run
#into 1 or 2. If it runs into 1, it will repeat 1-3 forever.
#If it runs into 2, it will repeat 2-4-6 forever.
#
#For example, imagine we started with the number 5:
#5 is not divisible by 3, so 5 + 2 = 7
#7 is not divisible by 3, so 7 + 2 = 9
#9 is divisible by 3, so 9 / 3 = 3
#3 is divisible by 3, so 3 / 3 = 1
#
#Start with 5, this sequence converges on 1 in 4 iterations:
#5 -> 7, 7 -> 9, 9 -> 3, 3 -> 1.
#
#Write a function called joyner. joyner should have one
#parameter, an integer. It should return the number of
#iterations required to reach either 1 or 2 for the first
#time.


#Add your code here!
def joyner(a):
    l=0
    while a != 1 or a !=1.0 :
        #print(a)
        if  a % 3 != 0:
            a+=2
            l +=1
        elif a/3 !=1:
            a =a/3
            l+=1
        else:
            a =a/3
            l +=1
    return l
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 4, 5, and 10, each on their own lines.
print(joyner(5))
print(joyner(15))
print(joyner(29))




