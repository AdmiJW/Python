
# Set .symmetric_difference() operation
#
# With String
#       setA.symmetric_difference("ABCD")
#
# With Sets
#       setA.symmetric_difference( set([1,2,3]) )
#       setA.symmetric_difference( {1,2,3} )
#
# With lists
#       setA.symmetric_difference( [1,2,3] )
#
# With Dictionaries (Only key)
#       setA.symmetric_difference( enumerate([1,2,3] ) )
#       setA.symmetric_difference( {1:"A", 2:"B"} )
#
# Using the XOR ^ operator
#       setA ^ setB


# Traditional solution
def soln1():
    N = int( input() )
    set_A = set( input().split() )
    M = int( input() )
    set_B = set( input().split() )

    print( len( set_A.symmetric_difference(set_B) ) )


# Compressed Solution
def soln2():
    _, set_A, _, set_B = [set(input().split() ) for i in range(4) ]
    print( len(set_A.symmetric_difference(set_B) ) )


# Compressed Solution using ^ operator (XOR)
def soln3():
    _, set_A, _, set_B = [set(input().split() ) for i in range(4) ]
    print( len( set_A ^ set_B ) )