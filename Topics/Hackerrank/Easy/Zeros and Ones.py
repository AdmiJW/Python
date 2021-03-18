import numpy as np


# For shape parsing, to extend map object into tuple, use * (extend operator) and bracket comma (,) for tuple notation
# Then, print numpy zeros and ones. Remember dtype or it'll default to float32 dtype
def soln1():
    shape = (*map(int, input().split()),)
    print(np.zeros(shape, dtype=int), np.ones(shape, dtype=int), sep='\n')


soln1()
