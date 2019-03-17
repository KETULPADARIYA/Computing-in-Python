steak = False
pork = True
guacamole = False
queso = False

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#Imagine you're writing code for a cash register at a
#restaurant. This restaurant serves burritoes. The base price
#of a burrito is $5. If the customer wants steak or pork, it
#adds $0.50. If they want quacamole, it adds $1.00. If they
#want queso, it adds $1.00. The customer may only select one
#meat, but they may have both queso and guacamole, neither,
#or just one.
#
#Write some code below that will print the cost of the
#burrito based on the variables above. You do not need to
#print the dollar sign or extra 0s. Remember, your final answer
#should only print out the price: comment out any debug
#statements once you have the right answer.

price = 5.00
if steak or pork:
    price += 0.50
if guacamole:
    price += 1.00
elif steak or pork:
    price += 0.00    
elif queso:
    price += 1.00
else:
    price +=0 
if queso:
    price += 1.00
print(price)




