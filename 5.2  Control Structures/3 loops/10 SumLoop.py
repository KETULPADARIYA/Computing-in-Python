mystery_int = 7
#Use a loop to find the sum of all numbers between 0 and
#mystery_int, including bounds (meaning that if
#mystery_int = 7, you add 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7).
#
#However, there's a twist: mystery_int might be negative.
#So, if mystery_int was -4, you would -4 + -3 + -2 + -1 + 0.
#
#There are a lot of different ways you can do this. Most of
#them will involve using a conditional to decide whether to
#add or subtract 1 from mystery_int.
#
#You may use either a for loopor a while loop to solve this,
#although we recommend using a while loop.
#Add your code here!
sum=0
if mystery_int >0:
    mystery_int += 1
    k = 1
elif mystery_int <0:
    mystery_int -= 1
    k =-1
for i in range(0,mystery_int,k):
        sum += i
        
print(sum)
