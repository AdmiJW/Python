
# Split, Capitalize, Join solution. Remember that split() without argument will eliminate multiple spaces,
# but with an explicit space character passed as delimiter, it will essentially preserve the white spaces.
def solve(s: str) -> str:
    return ' '.join( ( i.capitalize() for i in s.split(' ') ) )


# StringBuilder-like solution
def solve2(s: str) -> str:
    chars = []
    for c in s:
        if not len(chars) or chars[len(chars) - 1] == ' ':
            chars.append(c.upper())
        else:
            chars.append(c)
    return ''.join(chars)


# Shortened StringBuilder-like solution using Generator function
def solve3(s: str) -> str:
    return ''.join( (c.upper() if not j or s[j - 1] == ' ' else c for c,j in enumerate(s) ) )
