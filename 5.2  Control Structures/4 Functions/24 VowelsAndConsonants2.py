def count_letters(a_string, find_consonants):
    
    #And we still need a counter:
    count = 0
    
    #But this time, we'll check what we're looking for
    #first. If we're looking for consonants...
    if find_consonants:
        
        #...then we loop through looking for consonants:
        for character in a_string:
            if character in "bcdfghjklmnpqrstvwxyz":
                count += 1
        
    #If we weren't looking for consonants:
    else:
        
        #...then we loop through looking for vowels:
        for character in a_string:
            if character in "aeiou":
                count += 1

    #Either way, we return the result when we're done:
    return count
a_string = "up with the white and gold"

print(count_letters(a_string, True))
print(count_letters(a_string, False))
