from typing import *


# We have the issubset() function for sets!
#
#       setA.issubset( setB )
#
# It support operator too - use <=
#
#       setA <= setB


# Naive: Check One by one
def soln1( setA: Set, setB: Set) -> bool:
    for e in setA:
        if e not in setB:
            return False
    return True


# Use all() function
def soln2( setA: Set, setB: Set) -> bool:
    return all( e in setB for e in setA )


# Use difference set operation
def soln3( setA: Set, setB: Set) -> bool:
    return bool( setA.difference(setB) )


# Use difference set operation but with - operator
def soln4( setA: Set, setB: Set) -> bool:
    return bool( setA - setB )


# Use Built-in issubset function
def soln5( setA: Set, setB: Set) -> bool:
    return setA.issubset(setB)


# Use built in, but operator <=
def soln6( setA: Set, setB: Set) -> bool:
    return setA <= setB




if __name__ == '__main__':
    for i in range( int(input() ) ):
        _, setA, _, setB = input(), set(input().split() ), input(), set(input().split() )
        print( soln1(setA, setB) )
