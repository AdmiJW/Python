import math

# A function which computes number Of Combinations, (nCr)
def combination(n: int, r: int) -> int:
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


# Given percentage, convert to its probability value such that 0 <= x <= 1
def get_p_from_percentage(percent: int) -> float:
    return percent / 100


# A function which computes the binomial distribution, b(x,n,p) where
#   x: Number of success
#   n: Number of trials
#   p: Probability of success
def binomial_dist(x: int, n: int, p: float) -> float:
    return combination(n, x) * (p ** x) * ((1 - p) ** (n - x))


if __name__ == '__main__':
    percent, n = input().split()

    n = int(n)
    p = 1 - get_p_from_percentage( int(percent) )       # Probability that one piston is not rejected

    # To get no more than 2 rejects, we calculate reject = 0, 1, 2
    no_more_2_reject = sum( binomial_dist(i, n, 1 - p ) for i in range(0, 2 + 1) )
    print( '{:.3f}'.format(no_more_2_reject) )

    # To get at least 2 rejects, we take reject = 0, 1, 2 and complement it. So now reject = 3, 4, 5... 10
    # Then we add reject = 2 to result
    at_least_2_reject = 1 - no_more_2_reject + binomial_dist(2, n, 1 - p)
    print( '{:.3f}'.format(at_least_2_reject) )

