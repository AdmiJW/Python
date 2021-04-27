
from typing import *

def obtain_p_from_numerator_denominator( a:int, b:int ) -> float:
    return a / b


def geometric_dist( trials: int, p: float ) -> float:
    return (1 - p) ** (trials - 1) * p


def cumulative_geo_dist( maximum: int, p: float ) -> float:
    return 1 - (1 - p) ** maximum


if __name__ == '__main__':
    num_deno = [int(i) for i in input().split() ]
    maximum = int( input() )

    p = obtain_p_from_numerator_denominator( *num_deno )

    print( '{:.3f}'.format( cumulative_geo_dist(maximum, p) ) )

