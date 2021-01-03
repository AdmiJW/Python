
# Python can handle large integers internally. The details are abstracted away from us
# Don't worry about large integers. No error will be thrown


# Traditional Readability solution
def soln1():
    a = int( input() )
    b = int( input() )
    c = int( input() )
    d = int( input() )

    print( a**b + c**d )


# Destructuring list using Tuples, and obtain input using list comprehension
def soln2():
    a,b,c,d = [int(input) for _ in range(4) ]
    print( a**b + c**d )


# Do computations all in print statement
def soln3():
    print( int(input() ) ** int( input() ) + int(input() ) ** int(input() ) )
