rating = "R"
age = 15
#The United States has a movie rating system that rates
#movies with one of five ratings: G, PG, PG-13, R, and NC-17.
#Although some of the ratings are not binding, imagine that
#you are a parent who decides on the following rules:
# - Any child can see a G-rated movie.
# - To see a PG-rated movie, your child must be 8 or older.
# - To see a PG-13-rated movie, your child must be 13 or older.
# - To see an R-rated movie, your child must be 17 or older.
# - Your child may never see an NC-17 movie.
#The variables above give a rating and a child's age. Use
#these variables to select and print one of these two
#messages based on the criteria above:
# - "You may see that movie!"
# - "You may not see that movie!"
#However, there's one trick: you may not use the 'and' operator
#anywhere in this code!
#Add your code here!
if rating== "G":
    print("You may see that movie!") 
    
elif rating== "PG":
    if age >= 8 :
        print("You may see that movie!") 
    else:
        print("You may not see that movie!")
        
elif rating== "PG-13":
    if age > 12:
        print("You may see that movie!")
    else:
        print("You may not see that movie!")
elif rating== "R":
    if age > 16:
        print("You may see that movie!")
    else:
        print("You may not see that movie!")    
elif rating== "NC-17":
    if age < 18:
        print("You may not see that movie!")
    else :
        print("You may not see that movie!")        
else:
    print("You may not see that movie!")    