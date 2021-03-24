
import numpy as np

# For getting the min and max of a numpy array, we just use built in functions in numpy
#
# For max, we use np.max( arr ) and for min, we use np.min(arr).
# We can pass a keyword argument "axis" where default is None, which adds up every element in array and return a scalar.
#
#   For axis=0, it means the result is on a row, like:
#
#      [s1, s2, s3]
#       v    v   v
#      [e1, e2, e3]
#      [e4, e5, e6]
#      [e7, e8, e9]
#
#   Therefore s1 will be max/min(e1,e4,e7)
#
#   For axis=1, the result is on a column, like:
#
#    s1 >  [e1, e2, e3]
#    s2 >  [e4, e5, e6]
#    s3 >  [e7, e8, e9]
#
#   Therefore s1 is min/max(e1,e2,e3)
#


def soln1():
    N, M = map(int, input().split() )
    arr = np.array([ [*map(int, input().split() )] for i in range(N) ] )
    print( np.max( np.min(arr, axis=1) ) )