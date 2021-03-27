
import numpy as np

# When working with matrices, we cannot forget about matrix multiplications
#   >   np.dot( arr1, arr2 )
#   >   np.cross(arr1, arr2 )

def soln1():
    N = int(input() )
    arr1 = np.array([ [*map(int, input().split() )] for i in range(N)] )
    arr2 = np.array([ [*map(int, input().split() )] for i in range(N)] )
    print( arr1.dot(arr2) )