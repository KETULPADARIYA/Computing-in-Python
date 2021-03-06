mystery_string = "my cat your cat"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Add some code below that will count and print how many
#times the character sequence "cat" appears in mystery_string.
#For example, for the string above, it would print 2.
#
#This one is tricky! Think carefully about for-each loops,
#conditionals, and booleans. How can you track what character
#you're currently looking for? We expect you'll use a loop
#and a single big conditional, but there are other approaches
#as well. Try to stick with the topics we've covered so far.


#Add your code here!
#l=0
#m=""
#for i in mystery_string:
#    m += i
#    if "cat" in m:
#        l +=1
#        m = m.replace("cat","1")

mystery_string = "my cat your cat"

#Later on, we'll cover lots of other ways to do this, using
#more sophisticated approaches to using substrings and other
#concepts. We can still do this using just what we know now,
#though!
#
#First, we know we need a counter since the problem says to
#count something:

count = 0

#Next, we need to keep track of what letter we're currently
#searching for. The first letter in "cat" is "c", so by
#default, we'll set this to "c":
current_search_letter = "c"

#Then, we loop over all the letters in the string:
for letter in mystery_string:
    
    #For each letter, we want to see if it's the letter
    #we're looking for.
    #
    #If it's a 'c' and we're looking for 'c', great! Now
    #we're looking for 'a':
    if letter == "c" and current_search_letter == "c":
        current_search_letter = "a"
        
    #If it's an 'a' and we're looking for 'a', great! Now
    #we're looking for 't':
    elif letter == "a" and current_search_letter == "a":
        current_search_letter = "t"
        
    #If it's a 't' and we're looking for 't', then we've
    #found the word 'cat'! So, we add one to the counter,
    #and start over looking for 'c' again:
    elif letter == "t" and current_search_letter == "t":
        count += 1
        current_search_letter = "c"
     
    #Here's the trick: if we find any letter other than the
    #one we were looking for, then we need to start over!
    #If we've found "ca" but the next letter is "b", then
    #it doesn't matter if the one after it is "t": "cabt"
    #isn't the same as "cat":
    else:
        current_search_letter = "c"
print(count)






            
                
