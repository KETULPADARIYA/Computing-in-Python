message = "lol"
punct = "!"
num = 3

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Using the values of message, punct, and num, print
#a string that looks like the one below if message = "lol",
#punct = "!", and num = 3:
#
# !!!lol!!!lol!!!lol!!!
#
#Specifically, it should start by printing punct num
#times, then print message, repeat that entire process
#num times, and then print punct num times again.
#
#Here are a couple other examples:
#
# message = "bbl", punct = ":", num = 1 -> :bbl:
# message = "bbq", punct = "?", num = 2 -> ??bbq??bbq??
# message = "brb", punct = ".", num = 4 -> ....brb....brb....brb....brb....


#Add your code below!
print("message = {0}".format(num*(num*punct+message)+num*punct))






