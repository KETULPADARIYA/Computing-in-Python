#Write a function called mock. mock should take one
#parameter, a string. You may assume that the string will
#have only lowercase letters and spaces.
#
#Your function should return the same string, but any letter
#at an even index should be converted to uppercase.
#
#For example: mock("abcd efgh ijkl") would return
#"AbCd eFgH IjKl".
#
#Remember, you can use the ordinal function ord() to get the
#number associated with a single letter. For example,
#ord("a") returns 97. The number associated with lowercase
#letters is always 32 larger than the number associated with
#the equivalent uppercase letter. ord("a") is 97, and
#ord("A") is 65. ord("z") is 122, and ord("Z") is 90.
#
#Remember, you can use the character function chr() to
#convert a number back to a letter. For example, chr(65) will
#return "A".
#
#HINT: Treat all characters the same initially, then worry
#about taking care of spaces afterwards.


#Write your function here!
def mock(a):
    k=''
    l="ACEGJL"
    m='acegjl'
    for i in a :
        if i in l:
            a=a.replace(i,i.lower())
        elif i in m:
            a=a.replace(i,i.upper())
    return a
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: "A square with side length 4 has an area of 16".

print(mock("www.gatech.edu"))



