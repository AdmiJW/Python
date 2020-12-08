from typing import *


def average( arr: List ) -> float:
    distinct = set(arr)
    return sum(distinct) / len(distinct)


if __name__ == '__main__':
    N, arr = input(), list( map(int, input().split() ) )
    print( average( arr ) )

