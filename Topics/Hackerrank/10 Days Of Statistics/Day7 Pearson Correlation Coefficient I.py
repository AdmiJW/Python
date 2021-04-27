from typing import *


# Calculates the mean for a list or tuple of values
def mean(li: Union[List, Tuple] ) -> float:
    return sum(li) / len(li)


# Calculates the standard deviation for a list or tuple of values
def std_dev(li: Union[List, Tuple] ) -> float:
    u = mean( li )
    return ( sum( (i - u) ** 2 for i in li ) / len(li) ) ** 0.5


# Calculates the covariance for two given list or tuple of values
# Formula
#       1
#       - Σ( xi - ui )( yi - uy )           where ui = mean of x, uy = mean of y. n = sample size
#       n
#
def covariance( x: Union[List, Tuple], y: Union[List, Tuple] ):
    ux = mean( x )
    uy = mean( y )

    return (1 / len(x) ) * sum( (x[i] - ux) * (y[i] - uy) for i in range(len(x) ) )

# Calculates the covariance for two given list or tuple of values
# Formula
#       Covariance( x, y )
#       ------------------          where σx = standard deviation of x, σy = standard deviation of y
#           σx, σy
def pearson_correlation_coefficient(x: Iterable, y: Iterable) -> float:
    std_x = std_dev(x)
    std_y = std_dev(y)

    return covariance(x, y) / (std_x * std_y)


if __name__ == '__main__':
    N = int( input() )
    x = [ float(i) for i in input().split() ]
    y = [ float(i) for i in input().split() ]

    result = pearson_correlation_coefficient( x, y )

    print( '{:.3f}'.format( result ) )
