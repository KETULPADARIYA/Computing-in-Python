busy = False
hungry = False
tired = False
stressed = False

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Logical operators get more complex when we start using them
#with the results of other logical operators. So, let's try
#it out!
#
#Using the variables above, we want to assess whether the
#person is happy, sad, bored, confused, or anxious.
#
# - The person is happy if they're busy but not stressed.
# - The person is sad if they're either hungry or tired.
# - The person is confused if they're both happy and sad.
# - The person is bored if they're neither happy, sad,
#   nor busy.
# - The person is anxious if they're neither happy nor sad,
#   but they are stressed.
#
#Add code below whose output will list whether each of these
#emotions is true or false. For example, with the original
#values of the variables above, this would print:
#
#Happy: True
#Sad: True
#Confused: True
#Bored: False
#Anxious: False


#Add your code here!
Happy = busy & (not stressed)
Sad = hungry | tired
Confused = Happy & Sad
Bored = (Happy | Sad) |(not busy)
Anxious = Happy & stressed

print("Happy:",Happy)
print("Sad:",Sad)
print("Confused:",Confused)
print("Bored:",Bored)
print("Anxious:",Anxious)
