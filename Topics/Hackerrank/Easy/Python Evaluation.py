
#   Like Javascript, Python has also eval() function, which takes in a string
#   and the interpreter will run the string like normal code.
#
#   This feature is nice, but take caution when using it in server side code!
#   It might just be the security hole that expose server stuff to the client!


def soln1():
    eval( input() )
