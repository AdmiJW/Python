import itertools

# Generating permutations require backtracking. However, itertools module in Python already
# comes with handy function for that purpose!
#
#   itertools.permutation( Iterables, [r] )
#
# The r means the r in nPr - How many element out of all of them in the iterables are selected


# Semi Traditional method. Obtain input, Permutation with sorted string, using unpacking operator * to pass into
# the print() function, where each permutation must be mapped to a string first
def soln1():
    str, r = input().split()
    perms = itertools.permutations( sorted(str), int(r) )
    print( *map(lambda x: ''.join(x), perms), sep='\n')


# Compacter version. Without map() function
def soln2():
    str, r = input().split()
    [print( ''.join(x) ) for x in itertools.permutations(sorted(str), int(r) ) ]
