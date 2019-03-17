#Write a function called num_factors. num_factors should
#have one parameter, an integer. num_factors should count
#how many factors the number has and return that count as
#an integer
#
#A number is a factor of another number if it divides
#evenly into that number. For example, 3 is a factor of 6,
#but 4 is not. As such, all factors will be less than the
#number itself.
#
#Do not count 1 or the number itself in your factor count.
#For example, 6 should have 2 factors: 2 and 3. Do not
#count 1 and 6. You may assume the number will be less than
#1000.


#Add your code here!
def num_factors(s):
    k=0
    for i in range(2,999):
        if s %i==0 and s != i:
            k += 1
    return k

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 0, 2, 0, 6, 6, each on their own line.
print(num_factors(5))
print(num_factors(6))
print(num_factors(97))
print(num_factors(105))
print(num_factors(999))






