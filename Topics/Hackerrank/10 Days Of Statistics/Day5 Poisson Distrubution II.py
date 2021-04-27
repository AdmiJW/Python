
import math


def poisson_dist( mean:float, value:float ) -> float:
    return ( mean ** value * math.e ** -mean ) / math.factorial( value )


if __name__ == '__main__':
    mean = float( input() )
    value = float( input() )

    print( '{:.3f}'.format( poisson_dist(mean, value) ) )

