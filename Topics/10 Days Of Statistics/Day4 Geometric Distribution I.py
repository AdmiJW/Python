
from typing import *

# Just obtain The P value given numerator and denominator
def obtain_p_from_numerator_denominator( numerator:int, denominator:int ) -> float:
    return numerator / denominator


# Calculates the geometric distribution, given number of trials and the probability of success
def geometric_dist( trials:int, p:float ) -> float:
    return ( 1 - p ) ** (trials - 1) * p


if __name__ == '__main__':
    num_deno: List = map( lambda x: int(x), input().split() )
    trial = int( input() )

    p = obtain_p_from_numerator_denominator( *num_deno )

    print( '{:.3f}'.format( geometric_dist( trial, p) ) )
