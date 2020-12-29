from functools import *

# Key point to this problem: Repunit & Demlo Numbers

# Rejected solution - Using functional reduce() function
def soln1():
    for i in range(1, int(input()) + 1):
        print( reduce( lambda a,x: a * 10 + x, list(range(1, i+1)) + list(range(i-1,0,-1)), 0) )


# First obtain the list, [1,2,3,2,1]
# then zip it with indices 0 to n-1. [ (1,0), (2,1), (3,2), (2,3), (1, 4) ]
# Each index and value multiply by power of 10, [1, 20, 300, 2000, 10000 ]
# then sum
def soln2():
    for i in range(1, int(input()) + 1):
        print( sum(map(lambda x: x[0] * 10 ** x[1], zip(list(range(1, i+1) ) + list(range(i-1,0,-1) ), range(1, i+i) ) ) ) )


# Official solution
# 10/9 = 1
# 100/9 = 11
# 1000/9 = 111
#
# then,
# 11^2 = 121
# 111^2 = 12321...
def soln3():
    for i in range(1, int(input()) + 1):
        print( (10**i//9)**2 )