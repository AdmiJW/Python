
# One useful functionality of numpy is, it has operator overloading implemented.
# The operators will be able to perform element-wise operations by action known as
# 'broadcasting' on single array
#
# Not only that, it can perform operations on two operands too. See:
#   np.add(x,y)             or use +
#   np.subtract(x,y)        or use -
#   np.multiply(x,y)        or use *
#   np.floor_divide(x,y)    or use //
#   np.mod(x,y)             or use %
#   np.power(x,y)           or use **
#
# They are not limited to those only. Explore!

import numpy as np


def soln1():
    N, M = map(int, input().split() )
    arr_A = np.array( [ [ *map(int, input().split() ) ] for i in range(N) ] )
    arr_B = np.array( [ [ *map(int, input().split() ) ] for i in range(N) ] )

    print( arr_A + arr_B )      # Alt: np.add( arr_A, arr_B )
    print( arr_A - arr_B )      # Alt: np.subtract( arr_A, arr_B )
    print( arr_A * arr_B )      # Alt: np.multiply( arr_A, arr_B )
    print( arr_A // arr_B )     # Alt: np.floor_divide( arr_A, arr_B )
    print( arr_A % arr_B )      # Alt: np.mod( arr_A, arr_B )
    print( arr_A ** arr_B )     # Alt: np.power( arr_A, arr_B )

