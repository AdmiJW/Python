
# pow(x,y, [m] ) is a function that performs power of x raised to y.
# Same as x**y
#
# If m is passed in, it then computes the result modulo m. If m is present, y cannot be negative
# Same as (x**y) % m


# Traditional, readability solution
def soln1():
    X = int(input() )
    Y = int(input() )
    Z = int(input() )

    print( pow(X, Y), pow(X, Y, Z), sep='\n')


# Compact, using list comprehension and string formatting, unpacking operator *
def soln2():
    n = [int(input() ) for _ in range(3) ]
    print( f'{pow( *n[:-1] )}\n{pow( *n )}' )