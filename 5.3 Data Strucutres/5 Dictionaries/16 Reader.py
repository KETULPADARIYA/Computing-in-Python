#Recall in coding problem 4.4.3 that you wrote a function
#
# {"exam_1": {"number": 1, "grade": 90, "total": 100, "weight": 0.6},
#  "exam_2": {"number": 2, "grade": 95, "total": 100, "weight": 0.4}}
#
#Hint: Although the end result is pretty different, this
#should only dictate a minor change to your original
#Problem 4.4.3 code!


#Write your function here!
def reader(a):
    k=open(a+".txt")
    dic={}
    d={}
    for i in k:
        l=i.strip("\n").split()
        d['numner']=int(l[0])
        d['grade']=int(l[2])
        d['total']=int(l[3])
        d['weight']=float(l[4])
        
        dic[l[1]]=d
    return dic

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print (although the order of the keys may vary):
#{'assignment_1': {'total': 100, 'number': 1, 'grade': 85, 'weight': 0.25}, 'test_1': {'total': 100, 'number': 2, 'grade': 90, 'weight': 0.25}, 'exam_1': {'total': 100, 'number': 3, 'grade': 95, 'weight': 0.5}} 
print(reader("sample.cs1301"))


