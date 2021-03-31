import numpy as np

# Numpy deals with matrices and vectors, and therefore has built in linear algebra algorithms
#
# np.linalg.det( u )        - Determinant
# np.linalg.eig( u )        - Returns a tuple size 2 of eigenvalues and right eigenvectors
# np.linalg.inv( u )        - Inverse of matrix


def soln1():
    arr = np.array([[*map(float, input().split())] for i in range(int(input()))])
    print(round(np.linalg.det(arr), 2))


soln1()