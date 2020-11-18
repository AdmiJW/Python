import math


# A function which computes number Of Combinations, (nCr)
def combination(n: int,
                r: int) -> int:
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


# A function which computes the binomial distribution, b(x,n,p) where
#   x: Number of success
#   n: Number of trials
#   p: Probability of success
def binomial_dist(x: int,
                  n: int,
                  p: float) -> float:
    return combination(n, x) * (p ** x) * ((1 - p) ** (n - x))


# Given a pair of ratio, will calculate the p (probability) value of the left side of ratio
def get_p_from_ratio(x: float, y: float) -> float:
    return x / (x + y)



if __name__ == '__main__':
    x, y = map(lambda a: float(a), input().split())
    p: float = get_p_from_ratio(x, y)

    res: float = sum( binomial_dist(i, 6, p) for i in range(3,6 + 1) )

    print( '{:0.3f}'.format(res) )


