
import numpy as np

#   Say we have 2 size-3 vectors - u and v
#
#   u and v both have size of 3x1.
#
#   Inner product of 2 vectors are defined as transpose(u) * t
#       Thus the size is (1x3)(3x1). This multiplication results in scalar
#
#   Outer product of 2 vectors are defined as u * transpose(t)
#       Thus the size is (3x1)(1x3). This multiplication results in a matrix of 3x3 (depend on size of vector)
#
#

def soln1():
    arr1 = np.array([ *map(int, input().split() ) ])
    arr2 = np.array([ *map(int, input().split() ) ])
    print(np.inner(arr1, arr2))
    print(np.outer(arr1, arr2))