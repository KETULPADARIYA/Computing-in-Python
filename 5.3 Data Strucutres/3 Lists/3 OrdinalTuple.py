#Remember asciitable.com from an earlier exercise? We're
#going to use it again. Remember, ordinal values for
#characters are given in the 'Dec' column of asciitable.com.
#
#Write a function called character_info. character_info will
#take as input a string with only one character. It should
#return a 3-tuple with three pieces of information:
#
# - In the first spot, the character itself.
# - In the second spot, the ordinal value of the character,
#   obtained using the ord() function (e.g. ord("a") -> 97).
# - In the third spot, what type of character it is: either
#   "letter", "number", or "punctuation".
#
#You may assume that anything that is not a letter (either
#upper or lower case) or a number is punctuation. You may
#also assume the ordinal will be between 32 (" ") and 126
#("~").


#Write your function here!
def character_info(s):
    k=ord(s)
    if k >= 48 and k <= 57:
        return (s,k,"number")
    if (k >40 and k < 91 )or (k >96 and k <123)or k==42 or k ==43 or k==45 or k ==47:
        return (s,k,"letter")
    else:
        return (s,k,"punctuation")
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#('q', 113, 'letter')
#('7', 55, 'number')
#('`', 96, 'punctuation')
print(character_info("q"))
print(character_info("7"))
print(character_info("`"))




