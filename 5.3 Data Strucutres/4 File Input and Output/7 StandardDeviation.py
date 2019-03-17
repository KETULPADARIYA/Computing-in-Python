#Write a function called st_dev. st_dev should have one
#parameter, a filename. The file will contain one integer on
#each line. The function should return the population standard
#deviation of those numbers.
#
#The formula for population standard deviation can be found here:
#edge.edx.org/asset-v1:GTx+gt-mooc-staging1+2018_T1+type@asset+block@stdev.PNG
#
#The formula is a bit complex, though, and since this is a
#CS class and not a math class, here are the steps you would
#take to calculate it manually:
#
# 1. Find the mean of the list.
# 2. For each data point, find the difference between that
#    point and the mean. Square that difference, and add it
#    to a running sum of differences.
# 4. Divide the sum of differences by the length of the
#    list.
# 5. Take the square root of the result.
#
#You may assume for this problem that the file will contain
#only integers -- you don't need to worry about invalid
#files or lines. The easiest way to take the square root is
#to raise it to the 0.5 power (e.g. 2 ** 0.5 will give the
#square root of 2).
#
#HINT: You might find this easier if you load all of the
#numbers into a list before trying to calculate the average.
#Either way, you're going to need to loop over the numbers
#at least twice: once to calculate the mean, once to
#calculate the sum of the differences.


#Add your function here!
def st_dev(f):
    try:
        k =open(f,"r")
        l=0
        p=0
        o=0
        for i in k :
            m=int(i)
            l+=m
            p+=1
        average =l/p
        k =open(f,"r")
        for i in k:
            w=int(i)
            o +=(w-average)**2
        return (o/p)**0.5
    
    except:
        return "Error reading file!"
    finally:
        k.close()
    


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print 27.796382658340438 (or something around there).
print(st_dev("some_numbers.txt"))


