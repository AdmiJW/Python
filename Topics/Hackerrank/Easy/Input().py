

#   The intuition is that the expression inputted, shall be evaluated and checked
#
#   Since the given expression is in terms of x, therefore we store the value of x
#   just in variable 'x'. When eval, Python knows that there is 'x' variable
#   and evaluate it normally

def soln1():
    x, k = map(int, input().split() )
    print( eval(input() ) == k )
