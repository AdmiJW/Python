

# Produce a list with i number of elements each value of 'i'
# Map them so they become their 10 multiples of their index [3, 30, 300]
# Sum them up to get that 333
def soln1():
    for i in range(1, int(input() ) ):
        print( sum( map(lambda x, y: x * (10**y), [i] * i, range(i) ) ) )


# Official solution - Repunit numbers - Consisting of only 1's
# This is done by having powers of 10, divided by 9
# 10 / 9 = 1
# 100 / 9 = 11
# 1000 / 9 = 111
#
# Then just multiply it with row number
def soln2():
    for i in range(1, int(input())):
        print( 10**(i-1) // 9 * i )