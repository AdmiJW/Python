
# To perform flooring, ceiling, and rounding to an numpy array,
# there is built in functions already provided through
# numpy module.
#
# np.ceil(x)
# np.floor(x)
# np.rint(x)


import numpy as np
np.set_printoptions(legacy='1.13')

def soln1():
    arr = np.array([*map(float, input().split())])
    print( np.floor(arr) )
    print( np.ceil(arr) )
    print( np.rint(arr) )


soln1()