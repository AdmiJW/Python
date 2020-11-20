
import numpy as np

np.set_printoptions(suppress=True)




if __name__ == '__main__':

    # Declaration of the container list
    independent_N, entries = ( int(i) for i in input().split() )
    dv_values = []
    iv_values = []

    # Obtain the input
    for i in range(entries):
        *iv, dv = ( float(i) for i in input().split() )

        dv_values.append(dv)
        iv_values.append(iv)

    # Convert input into numpy arrays
    dv_values = np.array( dv_values , dtype=np.float32 )
    ones = np.ones( (entries, independent_N + 1), dtype=np.float32 )
    ones[:, 1:] = iv_values
    iv_values = ones

    # Obtain the B matrix
    # B = (Xᵀ X)⁻¹ Xᵀ Y
    B = np.linalg.inv( (iv_values.T @ iv_values) ) @ iv_values.T @ dv_values


    # Obtain the inputs, then calculate the query result out
    # Y = q x B
    # where q is the ( 1 x Q+1 ) matrix where first element is 1 and others are the x1, x2 .... xQ values
    N = int( input() )
    for i in range(N):
        x_vals = np.array( [ float(i) for i in input().split() ], dtype=np.float32 )
        x_vals = np.insert( x_vals, 0, 1, axis=0 )

        print( '{:.3f}'.format( x_vals @ B) )




