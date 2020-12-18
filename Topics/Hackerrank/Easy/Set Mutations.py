


def soln1():
    _, setA = input(), set(input().split() )
    for i in range( int(input() ) ):
        command = input().split()[0]

        if command == 'intersection_update':
            setA.intersection_update( input().split() )
        elif command == 'update':
            setA.update( input().split() )
        elif command == 'symmetric_difference_update':
            setA.symmetric_difference_update( input().split() )
        else:
            setA.difference_update( input().split() )

    print( sum( map(int, setA) ) )


# Traditional method, but using assignment operators.
# Note that to use these operators, RHS must also be of type set
def soln2():
    _, setA = input(), set(input().split())
    for i in range(int(input())):
        command = input().split()[0]

        if command == 'intersection_update':
            setA &= set(input().split())
        elif command == 'update':
            setA |= set(input().split())
        elif command == 'symmetric_difference_update':
            setA ^= set(input().split())
        else:
            setA -= set(input().split())

    print(sum(map(int, setA) ) )


# Compressed version using eval() function
def soln3():
    _, setA = input(), set(input().split() )
    for i in range(int(input() ) ):
        eval( f"setA.{ input().split()[0] }(input().split() )")
    print( sum(map(int, setA) ) )


# Compressed version using getattr() function
# Since Python all data types are objects, get the attribute
# of the object (The respective function) and execute it
def soln4():
    _, setA = input(), set(input().split() )
    for i in range(int(input() ) ):
        getattr(setA, input().split()[0] )(input().split() )
    print( sum(map(int, setA) ) )

