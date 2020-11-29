
# List Comprehension
#
#   List comprehension is an elegant to make lists (It returns a generator object which can be put in lists or tuples)
#
#   The syntax goes as following:
#       [   <expression>   <iterable>   <iterable2>?+   <boolean condition>     ]
#   Expression is the final value to be included in the list
#
#   Iterable is the original elements that has to be iterated to produce the final value
#   Nested iterable is also possible. It is equivalent to having 2 or more for loops
#   Boolean condition determines if the final value itself has to be included or not


if __name__ == '__main__':
    x, y, z, n = map(int, tuple(input() for i in range(4) ) )
    dimension = [ [i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i+j+k is not n ]
    print(dimension)
