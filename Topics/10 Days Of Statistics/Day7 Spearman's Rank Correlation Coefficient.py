from typing import *


# Given 2 sets of data, will essentially assign each value with a rank (through sorting), and
# find out the sum of all the ranking pairs difference squared
#       Σ( r1 - r2 )^2                  where r1 = ranking of value1, r2 = ranking of value2
def obtain_rank_diff_squared( x:Union[Tuple, List], y:Union[Tuple, List] ) -> float:
    pairs = list( zip(x, y) )
    res = 0

    pairs = sorted( pairs, key=lambda e: e[0] )
    y = sorted(y)

    for rank1, pair in enumerate(pairs, start=1):
        rank2 = binary_search( y, pair[1] ) + 1

        res += (rank1 - rank2) ** 2

    print(res)
    return res


# Performs binary search on a sorted list to find index of given target element
def binary_search( li:Union[Tuple, List], target:float ) -> int:
    left, right = 0, len(li) - 1

    while left is not right:
        mid = left + (right - left) // 2
        if li[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    N = int( input() )
    x = [ float(i) for i in input().split() ]
    y = [ float(i) for i in input().split() ]

    d_squared = obtain_rank_diff_squared(x, y)

    res = 1 - ( (6 * d_squared) / ( len(x) * (len(x) ** 2 - 1) ) )
    print('{:.3f}'.format( res ) )
