
# Text wrapping seems easy. However, like in HTML, text wrapping can be done prematurely
# when there is a whitespace separating the words and the next word, if included, will
# cause the string to exceed the limited width.
#
# Say the limit is 5, and our string is 'Hey Boo"
# You might say the wrapped text is "Hey B" and "oo", but that's not how text wrapping works
# It tries to preserve complete words so the readibility is still preserved.
# So it actually is "Hey" and "Boo"
#
# Luckily for us, there is already a prebuilt module 'textwrap' that will aid us in this process
#
# textwrap.wrap( str, limit ) -> List of wrapped strings
# textwrap.fill( str, limit ) -> Like above, but instead of list of strings, it wraps into newline separated paragraph


import textwrap

# Use fill()
def soln1():
    string, limit = input(), int(input() )
    print(textwrap.fill(string, limit) )


# Use wrap, which we need to manually join
def soln2():
    string, limit = input(), int(input() )
    print('\n'.join(textwrap.wrap(string, limit)))
