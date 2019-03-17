cost = 150000
rate = 0.0415
years = 15

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#When taking out a mortgage (a type of loan) for a house, the
#mortgage is defined by three variables: the total cost of the
#house, the interest rate at which you will pay back the
#mortgage, and how many months you have to pay back the
#mortgage.
#
#The formula to find the total amount of money that will be
#paid over that time is:
#
#  Cost * Number of Months * Monthly Rate /
#  1 - ((1 + Monthly Rate) ^ -Number of Months))
#
#Note that both time and rate are based on months: to find the
#monhtly rate, divide the annual rate by 12. To find the number
#of months, multiply the number of years by 12.
#
#Write some code that prints out a sentence like the following
#based on the original cost, interest rate, and number of years
#given above:
#
# The total cost of the house will be $201751.36
#
#You should round the total cost to two decimal places. You can
#do this with this line, assuming the actual value of the
#mortgage is stored in final_cost: final_cost = round(final_cost, 2)


#Add your code here!
rate /= 12
print("The total cost of the house will be ${0}".format(round(cost*years*12*rate/(1-((1+rate)**(-years*12))),2)))





