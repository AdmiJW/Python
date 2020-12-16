
# Sets .intersection() method
#
# Intersection with Strings
#   setA.intersection('STRING')
#
# Intersection with set
#   setA.intersection( set([1,2,3]) )
#
# Intersection with list
#   setA.intersection( set[1,2,3] )
#
# Intersection with dictionaries (keys)
#   setA.intersection( enumerate([1,2,3]) )
#   setA.intersection( {'a':1 } )
#
# Using & operator for intersection
#   setA & setB


# Normal way of solving
def soln1():
    N = int(input() )
    set_A = set( input().split() )
    M = int(input() )
    set_B = set( input().split() )

    print( len(set_A.intersection(set_B) ) )


# Compressed
def soln2():
    _, set_A, _, set_B = [set(input().split()) for i in range(4) ]
    print( len( set_A.intersection(set_B) ) )


# Using & operator
def soln3():
    _, set_A, _, set_B = [set(input().split() ) for i in range(4)]
    print( len( set_A & set_B) )


if __name__ == '__main__':
    pass