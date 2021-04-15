
# https://www.hackerrank.com/challenges/diagonal-difference/problem
# To get the sum of diagonal difference is not hard:
#       In direction of \, observe their index is same. (0,0), (1,1), (2,2)...
#       In direction of /, their index is 'complementing', like (0,2), (1,1), (2,0)...

def diagonalDifference(arr):
    l, lsum, rsum = len(arr), 0, 0
    for i in range(l):
        lsum += arr[i][i]
        rsum += arr[i][l-i-1]           # Alternatively, since python can use negative indices,
                                        # you can use -i-1
    return abs(lsum - rsum)

