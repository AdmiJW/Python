
# This problem is solved by dynamic programming
#
# First, notice how that no matter what, you'll only end up in leftmost or rightmost position
# This opens up the possibility to model using Finite State Machines
#
# There are 2 states: You are in leftmost, and you are in rightmost
# From a state:
#       >   You transition to yourself by simply not moving, or go to middle of array and returning back
#       >   You transiiton to opposite state by, simply going thru the park
#
# For going to middle, try to be greedy. Find out until which part of array yields the maximum score, thus
# that'll be the place to stop
#
#
# Therefore, create 2 DP arrays representing leftmost and rightmost state. At i, it will represent the maximum
# score so far until tht day. Update respectively.


test_cases = int(input() )

for i in range( test_cases):
    days, trees = map(int, input().split() )

    left_state = 0
    right_state = float('-inf')

    for d in range(days):
        trees = map(int, input().split() )

        tree_sum = sum(trees)

        left_max = 0
        left_sum = 0
        for t in trees:
            left_sum += t
            left_max = max(left_max, left_sum)

        right_max = 0
        right_sum = 0
        for t in trees[::-1]:
            right_sum += t
            right_max = max(right_sum, right_max)


        updated_left = max( left_state, right_state + tree_sum, left_state + left_max )
        updated_right = max( right_state, left_state + tree_sum, right_state + right_max )

        left_state, right_state = updated_left, updated_right

    print( max(left_state, right_state ) )

