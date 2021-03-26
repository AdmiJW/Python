
import numpy as np

# As usual, we might want to find out the mean, standard deviation and variances of a numpy array.
# This is done by arr.mean(), arr.var() and arr.std()
#
# The rule about the axis is the same:
#
#   For axis=0, it means the result is on a row, like:
#
#      [s1, s2, s3]
#       v    v   v
#      [e1, e2, e3]
#      [e4, e5, e6]
#      [e7, e8, e9]
#
#   Therefore s1 will be computed via e1, e4 and e7
#
#   For axis=1, the result is on a column, like:
#
#    s1 >  [e1, e2, e3]
#    s2 >  [e4, e5, e6]
#    s3 >  [e7, e8, e9]
#
#   Therefore s1 is computed via e1, e2 and e3


def soln1():
    M, N = map(int, input().split() )
    arr = np.array([ [*map(int, input().split() ) ] for i in range(M) ])
    print( arr.mean(axis=1) )
    print( arr.var(axis=0) )
    print( round(arr.std(), 11 ) )      # The testcase only want until 11 precision
