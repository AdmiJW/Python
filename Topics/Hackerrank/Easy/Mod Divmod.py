
# divmod( x,y ) is a function that performs the combination of division and modulus
# It returns a tuple consisting of two elements
#   First element is x//y
#   Second element is x%y


# Traditional, very readable method
def soln1():
    N = int(input() )
    M = int(input() )
    res = divmod( N, M )

    print(res[0], res[1], res, sep='\n')


# Compressed solution. Using unpacking operator * in print argument
def soln2():
    res = divmod( map(int, input().split() ) )
    print( *res, res, sep='\n' )


# String formatting solution. Using substitution labels
def soln3():
    print( '{0}\n{1}\n({0}, {1})'.format( *divmod(int(input() ), int(input() ) ) ) )