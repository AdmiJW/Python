import itertools


# Generating combinations, and finding out how many combinations involve the alphabet 'a'
#
# The probability will be
#
#       No of combinations with 'a'
#       --------------------------
#        No of total combinations
def soln1():
    N, alpha, K = int(input() ), input().split(), int(input() )
    combs = tuple( itertools.combinations( alpha ) )
    print( sum( [ 'a' in comb for comb in combs] ) / len(combs) )


# Probability solution. Much efficient since O(K) only
#
# For each N from 1 to K, calculate:
#       Getting 'a' on the Nth try.
# Also calculate the probability of failing to get 'a'. Then on N+1, we would use that failure probability
# to get probability to obtain 'a'
#
# Eg: K = 2, countOfA = C = 2, Length = 5
#
#      Prob = ( 2 / 5 )                 Getting 'a' on K = 1
#               +
#             ( 3 / 5 )( 2 / 4 )        Getting 'a' on K = 2
def soln2():
    N, count, K = int(input() ), sum( 1 for c in input() if c == 'a' ), int(input() )
    probability = 0
    failure = 1
    for attempt in range(K):
        success = count / N
        probability += failure * success
        failure *= (N-count) / N
        N -= 1

    print(probability)