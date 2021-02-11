
from fractions import Fraction
from functools import reduce

# Remember that map() and filter(), all is based on the concept of reduce()! Reduce is a functional
# programming function that iterates over elements one by one, process data based on current element
# and previous result, then finally return once all elements are processed.


# 3 Lines solution. Get input as Fraction objects, then reduce them by multiplying, then print the
# result!
def soln1():
    fracs = [ Fraction( *map(int, input().split() )   ) for i in range(int(input() ) ) ]
    res = reduce( lambda f1, f2: f1 * f2, fracs, 1)
    print( res.numerator, res.denominator )

soln1()