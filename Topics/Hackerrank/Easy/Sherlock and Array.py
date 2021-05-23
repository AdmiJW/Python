
# We want to know is there a position i in array such that sum of its left side is equal to sum of its right
# side, like:
#
#   [1, 2, 8, 3]
# In this case, index 2 (8) suffices because left = (1+2), right = (3), they equals.
#
# To do this efficiently, we first need some extra information about the array, that is, the sum of the array itself.
# In second loop, we do a running sum that helps us keep track of all the sums at the left side.
# With this, I can easily obtain the sum of left side from running sum, and sum of right side via formula
#       Right side sum = TOTAL - CURR ELEM - LEFT SIDE RUNNING SUM
#
# Time is O(N), space O(1)
def balancedSums(arr):
    total, left = sum(arr), 0
    for i in arr:
        right = total - i - left
        if left == right:
            return 'YES'
        left += i
    return 'NO'
