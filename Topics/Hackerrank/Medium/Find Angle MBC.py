from math import *

# This is more of a mathematical problem rather than a coding problem

# Given the 2 sides of a triangle. By connecting the 90 deg corner to the midpoint of the hypotenuse,
# how do we find out the angle between the line connecting midpoint and corner and the base?

# One such way is to realize, by connecting the 90 deg corner to the midpoint of hypotenuse,
# The length of the sides of the separated triangle, must be HALF the length of sides of original triangle.
# Remember the formula of finding midpoint? The midpoint can be seperated into 2 components of x and y, which
# represents the sides are of half the length!
# However, when subbed into arctan formula, u realize that the 1/2 can be cancelled, leaving AB / BC

# Another proof is by drawing two identical triangles, joining them such that they become a rectangle. By
# connecting midpoint, you realize it form a cross X in the rectangle.
# Looking at the lower left triangle and lower right triangle, and you'll realize they are identical triangles,
# and the angle is simply just tan x = AB/BC

ab, bc = int(input() ), int( input() )
print( round( degrees(atan( (ab) / (bc) ) ) ) )