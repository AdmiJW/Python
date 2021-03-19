
# Identity matrices are square matrices which along its diagonal is all 1, and the other elements are 0.
# Eye matrix on the other hand, is similar to identity matrices, except that the matrix can be non-square in size.
# This means there may be columns or rows that are all zero.
#
# In numpy, creating a eye matrix through eye(), we can pass an optional k index, where positives shifts the
# diagonal to the right (refers to upper diagonal)
# and negative shifts the diagonal down (refers to lower diagonal)
#
#   Eg:
#       k = 1
#          [0, 1, 0]
#          [0, 0, 1]
#          [0, 0, 0]



import numpy as np
np.set_printoptions(legacy='1.13')

def soln1():
    print( np.eye( *map(int, input().split() ) ) )