# SetA is strict superset if
#       |setB - setA| == 0, and
#       |setA| != |setB|
#
# Built in method: issuperset() or operator > or <


# Traditional solution
def soln1():
    setA = set( input().split() )
    for i in range( int(input() ) ):
        setB = set( input().split() )
        # It is not a subset if setB - setA still has element, or they are exact same set
        if len(setB.difference(setA) ) or len(setA) <= len(setB):
            return False
    return True


# Compressed solution, using - operator and any() method (Although you should be checking length)
def soln2():
    setA = set(input().split() )
    return not any( len( set(input().split() ) - setA ) for i in range( int(input() ) ) )


# Instead, use issubset() or its operator < (Although you should be checking length)
def soln3():
    setA = set(input().split() )
    return all( set(input().split() ) <= setA for i in range(int(input())) )


# Real solution: using issuperset() method, or operator > or <
def soln4():
    setA = set(input().split() )
    return all( set(input().split() ) < setA for i in range(int(input())) )


if __name__ == '__main__':
    print( soln1() )