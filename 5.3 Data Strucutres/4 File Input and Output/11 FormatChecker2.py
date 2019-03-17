#This is a long problem, but it's made out of a bunch of
#things we know how to do. So, let's break it up.

def format_checker(filename):
    
    #First, we need to open the file, of course.
    
	file_reader = open(filename)
	
    #Next, we know we're going to need to add up all the
    #weights. So, let's go ahead and create that counter
    #and set it to 0.
    
	total_weight = 0
    
    #Now, we want to iterate through all the lines in the
    #file and check them one by one.
    
	for line in file_reader:
        
        #First, let's split it up into its parts. We know
        #that spaces mark different pieces.
        
		parts = line.split(" ")
        
        #The first requirement in our file format is that
        #there by 5 parts on each line. If this line does
        #not have exactly 5 parts, we're done! This isn't
        #a valid line, and only one invalid line makes the
        #entire file invalid.
        
        if len(parts) != 5:
            
            file_writer.close()
			return False
        
        #Next, let's check to make sure each individual
        #part is of the right type. The first, third, and
        #fourth parts should be integers, and the 5th part
        #should be a float. If any of those conversions
        #cause an error, we're done!
        
		try:
			int(parts[0])
			int(parts[2])
			int(parts[3])
			float(parts[4])
            
            #Assuming all those conversions work, we now
            #want to add the fourth part to our running
            #total_weight variable.
            
			total_weight += float(parts[4])
		except:
            
            #If any of those conversions caused an error,
            #we're done. One error means this line is
            #invalid, and if this line is invalid, the
            #entire file is invalid.
            
            file_writer.close()
			return False
            
	
    #We're now done reading the file, so we can close it:
    file_writer.close()
    
    #If we reach this part of the function, it means that
    #none of the previous 'return False' lines ran. So,
    #that means we know that each line has 5 parts, and each
    #part of each line is the right type. The only thing we
    #have left to check is whether or not all those total
    #weights added to 1. If they don't, we return False.
    
    if total_weight != 1:
		return False
	
    #The only way this next line is reached is if all previous
    #checks were valid: five items per line, correct data
    #types, and weights that add to 1. If any of those were
    #not true, then a 'return False' line would have run. So,
    #we can safely return True.
    
	return True


print(format_checker("sample.cs1301"))
print(format_checker("test.cs1301"))




