
# Since it only requires to find out the max and min from 4 out of 5 values,
# I can simply find out
#       1. max
#       2. min
#       3. sum
# The maximum sum from 4 values is of course, to exclude only smallest integer
#       sum - min
# The minimum sum from 4 values is of course, to exclude only largest integer
#       sum - max


def miniMaxSum(arr):
    minN, maxN, sumN = min(arr), max(arr), sum(arr)
    print(sumN - minN, sumN - maxN)
