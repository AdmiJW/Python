
import numpy as np


# Using in-place reshaping by changing the value of nparray.shape
def soln1():
    ls = np.array(list(map(int, input().split())))
    ls.shape = (3, 3)
    print(ls)


# Return a newly reshaped array by using nparray.reshape() function
def soln2():
    ls = np.array(list(map(int, input().split())))
    print(ls.reshape((3, 3)))


soln2()