#Write a function called has_a_vowel. has_a_vowel should have
#one parameter, a string. It should return True if the string
#has any vowels in it, False if it does not.

def has_a_vowel(a_str):
    k=0
    for letter in a_str:
        
        if letter in "aeiou":
            k +=1
    if k>= 1:
        return True

    else:
        return False
    print("Done!")
    
    
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, then True, then False, then False, each on
#its own line.
print(has_a_vowel("abba"))
print(has_a_vowel("beeswax"))
print(has_a_vowel("syzygy"))
print(has_a_vowel(""))


