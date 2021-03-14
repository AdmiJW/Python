
import numpy as np

# When dealing with arrays, Python's built in List turns out to be not as efficient, because the items are
# not stored in continuous memory locations due to everything being Object. using numpy, data are stored in
# their primitive types and thus the memory allocation are continuous, and accessing are much faster
#
# Always remember the most native way of reversing an array in python, using [ start: stop: skip ]. The skip
# can be negative so the result will be fron right to left. Thus skip=-1 means to reverse the array

def soln1():
    input_arr = input().split()
    arr = np.array(input_arr, dtype=np.float32)
    print(arr[::-1])