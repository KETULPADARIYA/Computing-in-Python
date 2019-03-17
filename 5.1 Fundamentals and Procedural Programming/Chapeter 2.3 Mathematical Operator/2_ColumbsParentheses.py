q1 = 5
q2 = -10
r = 5

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#Below is some code that calculates electric potential energy
#based on Coulomb's law. However, it's presently broken, and
#can be fixed solely by fixing the parentheses.
#
#Fix this code. When it's correct, it should print:
#The electric potential energy is -89877424379.88

from math import pi
e = 8.854 * 10 ** -12

val_1 = (1 / (4 * pi * e))
val_2 = (q1 * q2) / r

print("The electric potential energy is", round((val_1 * val_2), 2))

