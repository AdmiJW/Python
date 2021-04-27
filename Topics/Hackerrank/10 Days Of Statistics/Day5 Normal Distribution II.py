import math
import scipy.integrate as itg


def normal_dist_height_func_factory( mean: float, variance: float ) -> float:
    def normal_dist_height( x: float) -> float:
        e_pow = -(x - mean ** 2) / (2 * variance)
        return math.exp( e_pow ) / ( variance ** 0.5 * (2 * math.pi) ** 0.5 )

    return normal_dist_height


#   Calculates Area under graph of the Normal Distribution Graph such that x passed, P(X <= x) is find out
def cumulative_normal_dist( x: float, mean: float, std_dev: float ) -> float:
    # Function to be used in integration
    def itg_func( x: float ):
        return math.exp( -(x ** 2) )

    # Calculates the error function value
    def err_func( x: float ):
        return (2 / math.pi ** 0.5) * ( itg.quad( itg_func, 0, x )[0] )

    # Argument for the error function
    err_func_arg = (x - mean) / (std_dev * 2 ** 0.5)

    return 0.5 * ( 1 + err_func(err_func_arg) )


#   Since in Hackerrank doesn't support scipy, alternative is calculate error function through math.erf()
def inbuilt_cumulative_normal_dist( x:float, mean: float, std_dev: float) -> float:
    err_func_arg = (x - mean) / (std_dev * 2 ** 0.5)

    return 0.5 * (1 + math.erf(err_func_arg ) )




if __name__ == '__main__':
    mean, std_dev = ( float(i) for i in input().split() )
    q1_x = float( input() )
    q2_x = float( input() )

    ans_1 = 1 - cumulative_normal_dist( q1_x, mean, std_dev )
    ans_3 = cumulative_normal_dist( q2_x, mean, std_dev )
    ans_2 = 1 - ans_3

    print('{:.2f}'.format( ans_1 * 100 ) )
    print('{:.2f}'.format( ans_2 * 100 ) )
    print('{:.2f}'.format( ans_3 * 100 ) )


