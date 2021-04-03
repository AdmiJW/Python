
def print_full_name(first, last):
    print("Hello", first, last + "! You just delved into python.")


# Old string formatting with %
def print_full_name2(first, last):
    print("Hello %s %s! You just delved into python." % (first, last) )


# Newer string formatting
def print_full_name3(first, last):
    print("Hello {} {}! You just delved into python.".format(first, last) )


# String.format() with positional arguments. Remember them as it may came in handy later
def print_full_name4(first, last):
    print("Hello {1} {0}! You just delved into python.".format(last, first) )


# Newest with f string
def print_full_name5(first, last):
    print( f"Hello {first} {last}! You just delved into python.")