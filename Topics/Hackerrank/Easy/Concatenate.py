
import numpy as np

# Numpy arrays can easily be concatenated.
# For matrices, we should specify the axis to concatenate in.
#   The default is axis=0, which concatenates in rows:
#           [ [], [] ] + [ [] ] ===> [ [], [], [] ]
#   If axis is axis=1, each row will be concatenated:
#           [ [1,2] ] + [ [3] ] ===> [ [1,2,3] ]

def soln1():
    N, M, P = map(int, input().split() )
    N_arr = np.array( [ list(map(int, input.split() ) ) for i in range(N) ] )
    M_arr = np.array( [ list(map(int, input.split() ) ) for i in range(M) ] )

    print( np.concatenate(N_arr, M_arr) )

