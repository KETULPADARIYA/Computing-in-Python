
#Write your function here!
def two_dimensional_booleans(bool_superlist,boolean):
    a=[]
    for i in bool_superlist:
        if boolean :
            a.append(not False in i)
        else:
            a.append(True in i)
    return a
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#[True, False, False]
#[True, True, False]
bool_superlist = [[True, True, True], [True, False, True], [False, False, False]]
print(two_dimensional_booleans(bool_superlist, True))
print(two_dimensional_booleans(bool_superlist, False))



