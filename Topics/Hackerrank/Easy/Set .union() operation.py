import sys
# SET .union() Operation
#
# Two sets can be union easily by several methods:
#
#   set_A = {1,2,3,4,5}
#
#   1. .union
#           >   On strings:    set_A.union('ABC')
#           >   On sets:       set_A.union( set(['A','B','C']) )
#                              set_A.union( {'A', 'B', 'C'} )
#           >   On lists:      set_A.union( ['A', 'B', 'C'] )
#                              set_A.union( enumerate(['A', 'B', 'C']) )    => { 1,2,3,4,5,(1,'b'),(2,'c'),(0,'a') }
#           >   On dict:       set_A.union( {'A':1} } )                     => { 1,2,3,4,5, 'A' }
#
#   Note that we can use the pipeline operator | for the same job!
#
#           set_A.union(set_B)      =       set_A | set_B


# More lengthy solution, easy to read
def soln1():
    N = input()
    set_A = set( input().split() )  # Don't care if it is int. For strings, it's same nevertheless unless you
                                    # really care about performance
    M = input()
    set_B = set( input().split() )

    print( len(set_A | set_B))


# Concentrated solution
def soln2():
    _, setA, _, setB = [ set( input().split() ) for i in range(4)]
    print( len( setA | setB ) )
