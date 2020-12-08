

# Using Map of size 26 to check if exists (Can use set as well)
def reduce_to_single( string: str ) -> str:
    is_seen = [False] * 26
    res = ''
    for c in string:
        if not is_seen[c - ord('A')]:
            res += c
            is_seen[c - ord('A') ] = True
    return res


# Shorter using list comprehension to execute loop. O(26N) as res is at most 26 in size
def reduce_to_single2( string: str ) -> str:
    res = []
    [ res.append(c) for c in string if not res.count(c)]
    return ''.join(res)


# First split by using slice method [:] on every multiple of k index
# Then map each string to be reduced so every alphabet occurs once only
def merge_the_tools(string: str, k: int) -> None:
    res = [ string[i: i+k] for i in range(0, len(string), k) ]
    [ print(segment) for segment in map( reduce_to_single, res ) ]


# Insane solution
# First, [iter(string)] * k will create a list consisting of k number of string iterators (SAME OBJECT)
# All of these is destructured into zip() function, so if k = 3, then zip(it, it, it)
# WHat zip does is take in any number of iterable, and essentially keep doing passes through the argument list
# and aggregate them into one tuple
# When iterator is used, it moves forward by one space.
# Since there are k iterators, it will extract the string in the segment which we exactly want
#
# Then using a dictionary and setdefault(k,v) which returns the key that we set, we can print them in one line
def merge_the_tools2(string:str, k: int) -> None:
    for segment in zip(*[iter(string)] * k):
        exists = dict()
        print(''.join( [ exists.setdefault(c, c) for c in string if c not in exists ] ) )


if __name__ == '__main__':
    string, k = input(), int( input() )
    merge_the_tools2(string, k)
