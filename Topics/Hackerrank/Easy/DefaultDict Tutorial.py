from collections import defaultdict

# Default dict is a specialized dictionary (Hash Map) which when trying to access a non-existance key value,
# will return a default value instead of throwing a KeyError at you
#
# In the constructor of the defaultdict, we pass in a constructor function for a value which when accessing a
# non existance key, will be called and set as the value before letting you to access it
#
#   Eg: defaultdict( list )
#
#       Then, when i access non existance key, it will construct a empty list and assign it as value of the key
#
#       defaultdict( int )
#
#       Default value is integer value 0


# Traditional, readibility method
def soln1():
    N, M = tuple( map(int, input().split() ) )
    ddict = defaultdict(list)

    for i in range(1, N+1 ):
        ddict[ input() ].append(i)

    for i in range(M):
        query = input()
        if len( ddict[query] ):
            print( *ddict[query] )
        else:
            print(-1)



# Compact solution. Using list comprehension as 1-line forEach method.
# In the fourth line, uses nested list comprehension trick
def soln2():
    N, M = tuple( map(int, input().split() ) )
    ddict = defaultdict(list)
    [ ddict[ input() ].append( x ) for x in range(1, N+1) ]
    [ print( *ddict[q] ) if len(ddict[q]) else print(-1) for q in [ input() for i in range(M) ] ]
