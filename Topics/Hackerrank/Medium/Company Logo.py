from collections import Counter


# Get frequencies, sort them, and then print the front 3.
# Since frequencies are STRICTLY NON-NEGATIVE, we can negate the frequency to
# negative number so they will sort the non-negative in front (Magnitude matters)
# Use unpacking operator * to unpack the tuples of key value pair
def soln1():
    counter = Counter( input() )
    sort = sorted( counter.items(), key=lambda x: (-x[1], x[0] ) )
    [print( *x ) for x in sort ]