from cmath import *

# complex() either takes in 2 arguments, each one is float value representing x and y in z=x+yi, or
# a string representing the complex number

# polar() takes in a complex number object, and returns a tuple containing two values
#   First is the r value (distance from O)
#   Second is the phi value (phase angle - radian from quadrant I)
print( *polar( complex(input() ) ), sep='\n')