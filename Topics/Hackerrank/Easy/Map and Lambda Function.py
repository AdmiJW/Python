
# Lambda functions in Python are one liner expression that is an anonymous function and commonly used as
# discardable functions
#
# To create fibonacci numbers, the most efficient way is to use Dynamic Programming, instead of using recursion
# which takes up O(2^N) time


# DP method
def make_fibonacci(N):
    fb = [0, 1]
    for i in range(2, N):
        fb.append( fb[i-1] + fb[i-2] )
    return fb[0:N]


cube = lambda x: x**3


def soln1():
    print( list(map(cube, make_fibonacci(int(input() ) ) ) ) )


# DP method but it is a generator
def fib_generator(N):
    x, y = 0,1
    for i in range(N):
        yield x
        x, y = y, x+y


def soln2():
    print( list(map(cube, fib_generator( int(input() ) ) ) ) )