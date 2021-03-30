
import numpy as np

# Numpy has some built in functions to deal with polynomials! Let' see them
#
# poly( roots )
#      Given the roots of the polynomial, it returns the coefficients of the original polynomial
#      Eg: np.poly([-1,1,1,10])         ==> x=-1, x=1, x=1, x=10
#      Output: [1, -11, 9, 11, -10]    <== x^4 - 11x^3 + 9x^2 + 11x - 10
#
# roots( coefficients )
#       Given the coefficients of a polynomial, returns the roots of it
#       Eg: np.roots([1, 0, -1])        ==> x^2 + -1
#       Output: [-1, 1]                 ==> x=-1, x=1
#
# polyint(coefficients)
#       Given the coefficients of polynomial, returns the coefficients of
#       the antiderivative (indefinite integration) for it
#       Eg: np.polyint([1,1,1])         ==> ∫(x^2 +x+ 1)
#       Output: [0.33333, 0.5, 1, 0]    ==> (1/3)x^3 + (1/2)x^2 + x + C
#
# polyder(coefficients)
#       Given the coefficients of polynomial, returns the coefficients of
#       the derivative of it
#       Eg: np.polyder([1,1,1,1])       ==> d/dx(x^3 + x^2 + x + 1)
#       Output: [3,2,1]                 ==> 3x^2 + 2x + 1
#
# polyval(coefficients, x)
#       Given coefficients of polynomial and x value, return y value for it
#       Eg: np.polyval([1,-2,0,2], 4)   ==> f(4) = x^3 - 2x^2 + 2
#       Output: 34
#
# polyfit( x, y, deg)
#       Least squares polynomial fit.
#       Eg: np.polyfit([0,1,-1, 2, -2], [0,1,1, 4, 4], 2)
#       Output : [  1.00000000e+00   0.00000000e+00  -3.97205465e-16]
#


print( np.polyval( [*map(float, input().split() ) ], float(input() ) ) )