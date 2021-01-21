from collections import deque

# This is simply a Greedy Deque problem.
# From the bottom to the top of the stack, it shall be the larger block at base, and smallest block at top
#
# Thus looking at both sides of the deque, always pick the largest one, but not larger than the already set base


# Readibility Deque solution
def soln1():
    T = int( input() )

    for i in range(T):
        _, blocks = input(), map(int, input().split() )


def determineStack( blocks ):
    curr, dq = float("inf"), deque(blocks)
    while len(deque):
        if deque[0] > deque[-1] and deque[0] >= curr:
            curr = deque.popleft()
        elif deque[-1] >= curr:
            curr = deque.pop()
        else:
            print("NO")
            return
    print("YES")


# Solution without using Deque --- Using Two pointers!
def soln2():
    for T in range( int(input() ) ):
        curr, N, blocks = float('inf'), int(input() ), list( map(int, input().split() ) )
        left, right = 0, N - 1

        while left <= right:
            if blocks[right] < blocks[left] <= curr:
                curr = blocks[left]
                left += 1
            elif blocks[right] <= curr:
                curr = blocks[right]
                right -= 1
            else:
                break

        print( "Yes" if left > right else "No" )


# Observe that the pattern of the blocks must be in DECREASING ORDER, THEN INCREASING ORDER LIKE
#       5,4,3,2,1,2,3,4,5   OR
#       5,4,3,2,1           OR
#       1,2,3,4,5
# So we can check for that using single pass of two loops
def soln3():
    for T in range( int(input() ) ):
        N, blocks = int( input() ), list( map(int, input().split() ) )
        i = 0

        while i < len(blocks) - 1 and blocks[i] >= blocks[i+1]:
            i += 1
        while i <  len(blocks) - 1 and blocks[i] <= blocks[i+1]:
            i += 1

        print("Yes" if i == len(blocks) - 1 else "No" )

