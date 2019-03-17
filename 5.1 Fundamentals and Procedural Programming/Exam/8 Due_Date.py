current_hour = 6
current_minute = 37
current_section = "AM"
due_hour = 2
due_minute = 30
due_section = "PM"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Given the current time and deadline time represented by the
#variables above, determine if an assignment is still eligible
#for submission. An assignment is eligible if the time
#represented by current_hour, current_minute, and
#current_section is before the time represented by due_hour,
#due_minute, and due_section.


#Add your code here!
if current_section =="PM":
    current_hour +=12
    if current_hour > 24:
        current_hour -= 24
        current_section =="AM"
if current_section =="AM" :
    if current_hour >= 12:
        current_hour -= 12
    
if due_section =="PM":
    due_hour+=12
c = current_hour *60+current_minute
d =due_hour*60+due_minute
print(c<d)







