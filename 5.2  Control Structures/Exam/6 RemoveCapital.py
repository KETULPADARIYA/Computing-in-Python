#Write a function called remove_capitals. remove_capitals
#should accept one parameter, a string. It should return a
#string containing the original string with all the capital
#letters removed. Everything else should be in the same
#place and order as before.
#
#For example:
#
# remove_capitals("A1B2C3D") -> "123"
# remove_capitals("WHAT") -> ""
# remove_capitals("what") -> "what"
#
#Remember, capital letters have ordinal numbers between 65
#("A") and 90 ("Z"). You may use the ord() function to get
#a letter's ordinal number.
#
#Your function should be able to handle strings with no
#capitals (return the original string) and strings with all
#capitals (return an empty string). You may assume we'll
#only use regular characters (no emojis, formatting
#characters, etc.).


#Write your function here!
def remove_capitals(a):
    m = ""
    for i in a:
        if ord(i)< 65 or ord(i) > 90:
            m += str(i)
            
    return m


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#123
#eorgia nstitute of echnology
print(remove_capitals("A1B2C3D"))
print(remove_capitals("Georgia Institute of Technology"))






