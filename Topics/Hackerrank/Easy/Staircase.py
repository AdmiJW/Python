

# In traditional way, you have to know the row number.
# At nth row (Assume start at 1), print n-1 spaces then n '#'s
#
# In Python, there is already built in method for you to use


# Traditional method
def staircase(n):
    for rn in range(1,n+1):
        print(' ' * (n-rn), '#' * rn, sep='')

# Built in method
def staircase2(n):
    for rn in range(1, n+1):
        print( ('#' * rn).rjust(n) )
