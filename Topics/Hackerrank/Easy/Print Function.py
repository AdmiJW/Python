
if __name__ == '__main__':
    n = int(input() )

    # Use of destructuring syntax as a way to pass multiple arguments into print()
    print( *(i for i in range(1, n+1) ), sep='' )

    # Use of print() in list comprehension
    [print(i, end='') for i in range(1, n+1) ]
