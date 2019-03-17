#Write a function called write_movie_info. write_movie_info
#will take as input two parameters: a string and a
#dictionary.
#
#The string will represent the filename to which to write.
#
#The keys in the dictionary will be strings representing
#movie titles. The values in the dictionary will be lists
#of strings representing performers in the corresponding
#movie.
#
#write_movie_info should write the list of movies to the file
#given by the filename using the following format:
#
# Title: Actor 1, Actor 2, Actor 3, etc.
#
#The movies and the actor names should be sorted
#alphabetically.
#
#So, for this dictionary:
#
# {"Chocolat": ["Juliette Binoche", "Judi Dench", "Johnny Depp", "Alfred Molina"],
#  "Skyfall": ["Judi Dench", "Daniel Craig", "Javier Bardem", "Naomie Harris"]}
#
#The file printed would look like this:
#
# Chocolat: Alfred Molina, Johnny Depp, Judi Dench, Juliette Binoche
# Skyfall: Daniel Craig, Javier Bardem, Judi Dench, Naomie Harris
#
#HINT: the keys() method of a Dictionary will return a list
#of the dictionary's keys. So, to get a sorted list of a_dict's
#keys, you could call key_list = a_dict.keys(), then call 
#key_list.sort().


#Write your function here!
def write_movie_info(filename,dic):
    
    for keys , values in dic.items():
        values.sort()
        
    #print (dic)
    kl =open(filename,"w")
    l=""
    k=[]
    for i,j in dic.items():
        k+=[i]
        k.sort()
        
    #    l += str(i) +":"
        
    #    for jj in j:
    #        l += jj+", "
            
    #    l=l.strip(", ")
    #    l += "\n"
    #l =l.strip("\n")
    for i in k:
        l += i+":"
        for artist in dic[i]:
            l += artist+", "
        l=l.strip(", ")
        l += "\n"
    l =l.strip("\n")
        
        
        
    
    #print(l)

    kl.write(l)
    kl.close()
    print(l)
    #return l
            

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print nothing -- however, it should write the same contents
#as Sample.txt to Test.txt.
movie_dict = {'Cocktail': ['Tom Cruise', 'Bryan Brown', 'Elizabeth Shue'], 'Back to the Future Part III': ['Michael J. Fox', 'Michael J. Fox', 'Christopher Lord', 'Mary Steenburgen'], 'Good Will Hunting': ['Matt Damon', 'Robin Wiiliams', 'Minnie Driver', 'Ben Affleck', 'Stellan Skarsgaard', 'Casey Affleck'], 'Beauty and the Beast': ['Paige OHara', 'Robby Benson', 'Richard White', 'Angela Lansbury', 'Kathleen Turner', 'Jerry Ohrbach', 'David Ogden Stears', 'Jo Anne Worley'], 'Born on the Fourth of July': ['Tom Cruise', 'Kyra Sedgewick', 'Willem Dafoe', 'Ron Kovic', 'Paul Abbott']}
movies = {"Chocolat": ["Juliette Binoche", "Judi Dench", "Johnny Depp", "Alfred Molina"], "Skyfall": ["Judi Dench", "Daniel Craig", "Javier Bardem", "Naomie Harris"]}
movie_dict = {'Air Force One': ['Harrison Ford', 'Gary Oldman', 'Jena Malone'], 'La Bamba': ['Lou Diamond Phillips', 'Esai Morales', 'Rosana deSoto', 'Danielle vonZerneck', 'Joe Pantoliano', 'Elizabeth Pena']}
write_movie_info("AutomatedTest-jkAmxk.txt", movie_dict)



