import itertools

# Cartesian product of 2 sets is basically all possible ordered pairs formed
# Similar is ( (x,y) for x in A for y in B )
#
# itertools module comes with a product() function that does exactly that, except it is an Iterator!


# Traditional, readability method. Use of unpack operator here *
def soln1():
    l1 = set( map(int, input().split() ) )
    l2 = set( map(int, input().split() ) )

    res = itertools.product(l1, l2)
    print(*res)


# Very short version
def soln2():
    print( *itertools.product( *(set(map(int, input().split() ) ) for _ in '12' ) ) )
