#Imagine you're writing the software for an inventory system for
#a store. Part of the software needs to check to see if inputted
#product codes are valid.
#
#A product code is valid if all of the following conditions are
#true:
#
# - The length of the product code is a multiple of 4. It could
#   be 4, 8, 12, 16, 20, etc. characters long.
# - Every character in the product code is either an uppercase
#   character or a numeral. No lowercase letters or punctuation
#   marks are permitted.
# - The character sequence "A1" appears somewhere in the
#   product code.
#
#Write a function called valid_product_code. valid_product_code
#should have one parameter, a string. It should return True if
#the string is a valid product code, and False if it is not.


#Add your code here!
def valid_product_code(a):
    for i in a:
        if (ord(str(i)) >= 65 and ord(str(i))<=90) or (ord(str(i)) >=48 and ord(str(i))<=57):
            K =1
        else:
            return False   
            
    if len(a)%4 == 0 and "A1"in a:
        #print(len(a)%4)
        return True
    else:
        return False
    return True

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, True, False, False, False
print(valid_product_code("A12B44BP"))
print(valid_product_code("BFDSAUSA98932RWEFOEWA9FEAA1DSFSF"))
print(valid_product_code("A1BBD5"))
print(valid_product_code("BDD5664S"))
print(valid_product_code("66aBSaA1fdsv"))



