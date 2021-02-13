
# Remember str.split()? str.split() only allows you to specify one type of delimiter to split
# the string
# With re.split(), you can specify the delimiter using regex, then any pattern that fully matches
# the regex will become delimiter, then the string will be split accordingly!


import re


def soln1():
    print( *re.split( r"\.|,", input() ), sep='\n' )    # Or if no escape chars, [.,]

