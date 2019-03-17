story = "A"
text = "B"
role = "C"
director = "D"
cast = "F"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#In Bryan Cranston's autobiography, he describes how after
#his success on Breaking Bad, he developed a scoring system
#for evaluating new scripts that he received.
#
#First, he would assign the script a grade -- A, B, C, D, or
#F -- in each of five categories: Story, Text, Role, Director,
#and Cast.
#
#Then, he would tally those grades into a total score for the
#script, according to the following chart:
#
#            A   B   C   D   F
# Story     +6  +5  +4  +2  +0
# Text      +5  +4  +3  +1  +0
# Role      +4  +3  +2  +1  +0
# Director  +3  +2  +1  +0  +0
# Cast/Misc +2  +1  +0  +0  +0
#
#For example: an A story, B text, C role, D directory, and
#F cast would get a score of 12: +6 for the story, +4 for the
#text, +2 for the role, +0 for the director, and +0 for the
#cast.
#
#Then, based on that score, the script would be assigned a
#category (note these are slightly different from the image
#because we've excluded the time variable):
#
# 20: Perfect score
# 17 to 19: Must do
# 14 to 16: Seriously consider
# 12 to 13: On the bubble
# 11 or below: Pass
#
#The variables above give the letter grades assigned to each
#of the five components. Write a program that calculates the
#total score he would assign to the script represented by
#these variables. Then on the next line, print the category
#he would assign to that script. For example, for the values
#above, this program would print:
#
#12
#Pass
#
#HINT: This is a *long* program. It's not particularly
#complex -- you're doing the same thing over and over, However,
#that 'same thing' required 4-8 lines each time you do it. Our
#answer is 46 lines long! So, don't think you're off-track just
#because you're writing a lot of lines.


#Add your code here!

t  = 0
if story == "A":
    t += 6
if story == "B":
    t += 5
if story == "C":
    t += 4
if story == "D":
    t += 2
if story == "F":
    t += 0
    
if text == "A":
    t += 5
if text == "B":
    t += 4
if text == "C":
    t += 3
if text == "D":
    t += 1
if text == "F":
    t += 0
if role == "A":
    t += 4

if role == "B":
    t += 3
if role == "C":
    t += 2
if role == "D":
    t += 1
if role == "F":
    t += 0

if director == "A":
    t += 3
if director == "B":
    t += 2
if director == "C":
    t += 1
if cast =="A":
    t+=2
if cast == "B":
    t += 1
print(t)
if t == 20:
    print("Perfect score")

if t ==19 or t ==18 or t == 17:
    print("Must do")

if t == 14 or t == 15 or t ==16:
    print('Seriously consider')

if t == 13 or t ==12:
    print("On the bubble")

if t ==11 or t < 11 :
    print('Pass')




