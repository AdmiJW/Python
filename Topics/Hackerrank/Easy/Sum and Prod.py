
import numpy as np

# For getting the sum and product of a numpy array, we just use built in functions in numpy
#
# For summing, we use np.sum( arr ). We can pass a keyword argument "axis" where default is
# None, which adds up every element in array and return a scalar.
# The same goes for product. Use np.prod( arr ). Likewise, it has keyword argument "axis" too
#
#   For axis=0, it means the sum result is on a row, like:
#
#      [s1, s2, s3]
#       v    v   v
#      [e1, e2, e3]
#      [e4, e5, e6]
#      [e7, e8, e9]
#
#   Therefore s1 will be e1+e4+e7
#
#   For axis=1, the sum result is on a column, like:
#
#    s1 >  [e1, e2, e3]
#    s2 >  [e4, e5, e6]
#    s3 >  [e7, e8, e9]
#
#   Therefore s1 is e1 + e2 + e3
#


def soln1():
    N, M = map(int, input().split() )
    arr = np.array( [ [*map(int, input().split() ) ] for i in range(N) ] )
    print( np.prod( np.sum(arr, axis=0 ) ) )
