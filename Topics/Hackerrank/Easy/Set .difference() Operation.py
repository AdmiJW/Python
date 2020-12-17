

# Set .difference() operation
#
# Difference on String
#   set.difference("ABCD")
#
# Difference on Set
#   set.difference( set([1,2,3]) )
#   set.difference( {1,2,3} )
#
# Difference on List
#   set.difference( [1,2,3] )
#
# Difference on Dictionary (Using key)
#   set.difference( {'a':1} )
#
# Difference using - operator
#   set_A - set_B


# Traditional way
def soln1():
    N = int( input() )
    set_A = set( input().split() )
    M = int( input() )
    set_B = set( input().split() )

    print( len(set_A.difference(set_B) ) )


# Compressed version using list comprehension
def soln2():
    _, set_A, _, set_B = [ set(input().split() ) for i in range(4) ]
    print( len(set_A.difference(set_B) ) )


# Compressed (Difference using Operator -)
def soln3():
    _, set_A, _, set_B = [ set(input().split() ) for i in range(4) ]
    print( len( set_A - set_B ) )