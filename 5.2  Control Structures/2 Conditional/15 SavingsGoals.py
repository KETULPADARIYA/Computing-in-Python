principal = 5000
rate = 0.05
time = 5
goal = 7000
#Recall in problem 2.4.5 you wrote some code that calculated
#the amount of money in an account based on this formula:
#   amount = principal * e ^ (rate * time)
#Those three variables are given above again, as well as a
#fourth: goal. We want to see if the investment given by
#these values will exceed the goal. If it will, we want to
#print this message:
#  "You'll exceed your goal by [extra money]"
#
#If it will not, we want to print this message:
#
#  "You'll fall short of your goal by [needed money]"
#
#If the investor will meet their goal, [extra money] should
#be the final amount minus the goal. If the investor will
#not meet their goal, [needed money] will be the goal minus
#the final amount.
#
#To make the output more legible, though, we want to round
#the difference to two decimal places. If the difference is
#contained in a variable called 'difference', then we can
#do this to round it: rounded_diff = round(difference, 2)
#
#Working with new and unfamiliar functions or abilities is
#part of learning to code, so use this function in your
#answer!

import math

#Remember, you can access e with math.e.


#Add your code here! Feel free to copy your code from 
#problem 2.4.5.
amount=principal*math.e**(rate*time)
difference_1=amount-goal
difference_2=-amount+goal
rounded_diff_1 = round(difference_1, 2)
rounded_diff_2 = round(difference_2, 2)
if goal <= amount:
    print("You'll exceed your goal by",rounded_diff_1)
else:
    print("You'll fall short of your goal by",rounded_diff_2)
