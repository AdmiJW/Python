
# To check for a palindrome in string can be done in several ways
#
# The most computer resource efficient way is to use two pointers to compare characters at both end,
# until middle, taking O(N/2) time
#
# The fastest and easy to code is however, just reverse the string and compare if both strings are the same
#
# Since the all() and any() doesn't take in a callback function, simply make a generator that evaluates if
# condition is true or not. Generator doesn't occupy memory in its entirety like list or tuple does, therefore
# is much space efficient


#   Line 1 - Input retrieval
#   Line 2 - all() and any()
def soln1():
    _, nums = input(), [ int(N) for N in input().split() ]
    print( all( N > 0 for N in nums ) and any( str(N) == str(N)[::-1] for N in nums ) )
