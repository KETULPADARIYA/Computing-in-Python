mystery_int = 50

#Add some code below that will find and print the sum of
#every odd number between 0 and mystery_int. This time,
#exclude the bounds (e.g. if mystery_int was 51, add the odds
#from 1 to 49, but not 51).
#
#Hint: There are multiple ways to do this!

sum=0
#Add your code here!
for i in range(0,mystery_int):
    if i %2 != 0:
        sum += i
        
print(sum)

