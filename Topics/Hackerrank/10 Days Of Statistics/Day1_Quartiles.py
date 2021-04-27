from typing import *

# Pass in an array and give its range (INCLUSIVE), returns the median
def get_median(elem: List, cum_table: List, start: int, end: int) -> float:
    length: int = end - start + 1
    mid_point: int = start + (length - 1) // 2
    median: List = []

    idx: int = 0
    while cum_table[idx] < mid_point:
        idx += 1
    median.append( elem[idx] )

    if length % 2 == 0:
        median.append( elem[idx] if cum_table[idx] <= mid_point + 1 else elem[idx + 1] )

    return sum(median) / len(median)



# Obtain Input
N: int = int(input() )
elem: List = [ int(i) for i in input().split() ]
freq: List = [ int(i) for i in input().split() ]

# Remember for quartiles the numbers must be sorted
arr = sorted(arr)

# Find the midpoint, very useful when splitting quartiles
midPoint: int = N // 2

print( int( get_median(arr, 0, midPoint - 1) ) )    # First quartile
print( int( get_median(arr, 0, N - 1 ) ) )          # Find median
print( int( get_median(arr, midPoint if N % 2 == 0 else midPoint + 1, N - 1) ) )    # Third quartile


