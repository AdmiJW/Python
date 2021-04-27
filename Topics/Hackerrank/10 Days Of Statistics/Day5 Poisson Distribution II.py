
import math


def poisson_dist( mean: float, value: float ) -> float:
    return ( mean ** value * math.e ** -mean ) / math.factorial(value)


def A_maintain(a:float ) -> float:
    return 160 + 40 * (a * (1 + a) )


def B_maintain(b:float ) -> float:
    return 128 + 40 * (b * (1 + b) )


if __name__ == '__main__':
    a, b = [ float(i) for i in input().split() ]

    print( '{:.3f}'.format(A_maintain(a) ) )
    print( '{:.3f}'.format(B_maintain(b) ) )
