
import re

# We don't want to validate a regex ourselves. Simply use the built in module to check the validity of a regex string


# Initial solution. Just try to match the input regex with a dummy string. If regex is invalid, error will be thrown
def soln1():
    for i in range( int(input() ) ):
        try:
            re.match( input(), '' )
            print(True)
        except Exception:
            print(False)


# More precise solution is to use re.compile() method. The error raised is in re.error
def soln2():
    for i in range( int(input() ) ):
        try:
            re.compile( input() )
            print(True)
        except re.error:
            print(False)