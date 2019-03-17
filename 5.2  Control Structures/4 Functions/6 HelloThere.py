#Write a function called greeting. greeting should have one
#parameter, a string representing a name. It should return
#a string with the message "Hi [name]!", where the value of
#the parameter is used in place of [name].
#
#For example:
#
# greeting("David") -> "Hi David!"


def greeting(input_name):
    return "Hi " + input_name + "!"


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "Hi David!"
a_name = "David"
message = greeting(a_name)
print(message)



