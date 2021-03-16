
import numpy as np


# First create a List first, then only create numpy array. This is because numpy array is not dynamic array
# and we can't append into it
#
# Use np.transpose( nparray ) for transposing, and
# nparray.flatten() for flattening the array
def soln1():
    N, M = map(int, input().split() )
    mat = []
    for row in range(N):
        mat.append( [*map(int, input().split() ) ] )

    arr = np.array(mat)
    print( np.transpose(arr) )
    print( arr.flatten() )



# More compressed using list comprehension and destructuring
def soln2():
    mat = [ [*map(int, input().split() ) ] for n in range( int(input.split()[0] ) ) ]
    arr = np.array(mat)
    print(np.transpose(arr))
    print(arr.flatten())