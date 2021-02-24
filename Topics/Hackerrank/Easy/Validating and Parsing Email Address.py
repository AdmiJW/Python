
# An email address require the following format:
#       username@domain.extension
#   username can consist of alphanumeric, _, . and -
#   extension and domain can only contain english alphabets
#   extension can only be 1-3 in length

#   ^   -            Starts with
#   [a-zA-Z]         First char must be alphabet
#   [a-zA-Z0-9-._]*  Followed by alphanumeric and ._- char, as many as you like
#   @                @ seperates to domain
#   [a-zA-Z]+        Domain
#   \.               dot . seperates the extension
#   [a-zA-Z]{1,3}    extension must only be alphabets and only 1-3 in length
#   $                Ends


# email.utils.parseaddr -> For a string in format "NAME <Email>", parse to tuple, removing <>
# email.utils.formataddr -> Does the reverse of above by taking in tuple of 2 of (NAME, Addr)

import re
import email.utils

def soln1():
    pattern = re.compile( r"^[a-zA-Z][a-zA-Z0-9-._]*?@[a-zA-Z]+\.[a-zA-Z]{1,3}$" )

    for i in range(int(input() ) ):
        name, mail = email.utils.parseaddr( input() )
        if re.match(pattern, mail):
            print( email.utils.formataddr( (name,mail) ) )

soln1()