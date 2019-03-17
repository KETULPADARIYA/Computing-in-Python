#We've given you a file called "top500.txt" which contains
#the name and lifetime gross revenue of the top 500
#films at the time this question was written. 
#
#Each line of the given file is formatted like so:
# <name>\t<gross revenue in dollars>
#
#In other words, you should call .split("\t") to split
#the line into the movie name (the first item) and the
#gross (the second item).
#
#Unfortunately, these movies are not in order. Write a 
#function called "sort_films" that accepts two parameters:
#a string of a source filename and a string of a
#destination filename. Your function should open the
#source file and sort the contents from greatest gross
#revenue to least gross revenue, and write the sorted
#contents to the destination filename. You may assume the
#source file is correctly formatted.
#
#Hint: one common issue on this problem is that every line
#in the input file ends with a line break except the last
#one. If the autograder gives you an index error, open
#top500result.txt and make sure there are 500 lines in your
#output file!


#Write your function here!
def sort_films(xlist, xresult):
    a=[]
    inputFile=open(xlist, "r")
    for line in inputFile:
        b=line.split("\t")
        c=b[1].strip("\n")
        a.append(c)
        a.sort(reverse=True)
        #print(a)
    inputFile=open(xlist, "r")
    num_lines = sum(1 for line in open(xlist))
    print(num_lines)
    i=0
    for i in range(len(a)):
        outputFile=open(xresult, "a")
        for line in open(xlist):
            b=line.split("\t")
            c=b[1].strip("\n")
            if a[i]==c:
                print(b[0]+"\t",c,file=outputFile)
                i+=1
                break
            else:
                pass
    inputFile.close()
 
#The line of code below will test your function and put
#your results in top500result.txt. Then, it will print
#"Done!"
sort_films("top500.txt", "top500result.txt")
print("Done!")





