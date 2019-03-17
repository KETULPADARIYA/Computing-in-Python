def one_dimensional_booleans(bool_list, use_and):
    
    #There are a lot of different ways you could do this.
    #You could, for example, loop over each item in the
    #list and update a running result based on the new
    #value.
    #
    #Let's try it a simpler way, though. If use_and was
    #False, then our logic is pretty simple: we just
    #return whether 'True' is anywhere in the list:
    
    if not use_and:
        return True in bool_list
    
    #If use_and was True, our logic is just a little bit
    #more complicated. First, we want to find our whether
    #False is in the list. If it is, then we want to
    #return False; if it's not (meaning all the values
    #are True), then we want to return True. So, we want
    #to return the *opposite* of False in bool_list. We
    #can do that with the not operator:
    
    else:
        return not False in bool_list
    
    #Note that we could actually compress these four lines
    #down into only one, but it makes the logic a little
    #harder to follow:
    #
    #return (use_and and True in bool_list) or (not use_and and not False in bool_list)



print(one_dimensional_booleans([True, True, True], True))
print(one_dimensional_booleans([True, False, True], True))
print(one_dimensional_booleans([True, False, True], False))
print(one_dimensional_booleans([False, False, False], False))




