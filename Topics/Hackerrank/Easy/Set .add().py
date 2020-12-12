
#   Use set.add( e ) to add elements into the set
def soln1():
    N = int(input() )
    stamps = set()
    for i in range(N):
        stamps.add( int(input() ) )
    print( len(stamps) )


# 2 line solution
def soln2():
    N = int( input() )
    print( len( set( input() for i in range(N) ) ) )


# 1 line solution
# Remember that instead of using set() constructor, you can also use curly brackets {} literal notation
def soln3():
    print( len( { input() for i in range( int(input() ) ) } ) )
