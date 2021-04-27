
import math
from typing import *


# Pass in a list of values and find out the mean of it
def mean( x:Union[List, Tuple] ) -> float:
    return sum(x) / len(x)


# Given a list of values, return the standard deviation
def std_dev( x:Union[List, Tuple] ) -> float:
    u = mean( x )
    dist_squared = sum( (i - u) ** 2 for i in x )
    return ( dist_squared / len(x) ) ** 0.5


# Given a list of values, calculates and return the pearson correlation coefficient
def pearson_correlation_coefficient( x: Union[List, Tuple], y: Union[List, Tuple] ) -> float:
    x_mean = mean(x)
    y_mean = mean(y)
    x_std_dev = std_dev(x)
    y_std_dev = std_dev(y)

    covariance = (1/ len(x) ) * sum( (i - x_mean)*(j - y_mean) for i, j in zip(x, y) )

    return covariance / (x_std_dev * y_std_dev)


# Given m, x and c of a linear equation, return y value
def linear_equation( m: float, x: float, c: float ) -> float:
    return m * x + c


# Given m, x and y of a linear equation, return c value
def find_y_intercept( m:float, x: float, y: float ) -> float:
    return y - m * x


if __name__ == '__main__':
    x_val, y_val = [], []

    for i in range(5):
        x, y = (int(v) for v in input().split() )
        x_val.append(x)
        y_val.append(y)

    x_mean = mean(x_val)
    y_mean = mean(y_val)
    x_std_dev = std_dev(x_val)
    y_std_dev = std_dev(y_val)
    r = pearson_correlation_coefficient(x_val, y_val)
    m = r * (y_std_dev / x_std_dev)

    c = find_y_intercept( m, x_mean, y_mean )

    print( '{:.3f}'.format( linear_equation( m, 80, c ) ) )
