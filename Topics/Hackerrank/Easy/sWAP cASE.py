

# Before attempting to come up with any algorithm, there exists the built in function
#       s.swapcase()


# Recursive method - Base case of length 1. If not length 1, split string into length 1 substrings and apply function
def swap_case(s: str):
    if len(s) == 1:
        return s.upper() if s.islower() else s.lower()

    return ''.join( map(swap_case, s ) )


# Not recursive, but uses lambda in one line
def swap_case2(s: str):
    return ''.join( map(lambda x: x.upper() if x.islower() else x.lower(), s) )


# Built in function
def swap_case3(s: str):
    return s.swapcase()