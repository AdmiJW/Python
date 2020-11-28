
if __name__ == '__main__':
    # Use of join method on iterables
    print( '\n'.join( str(i**2) for i in range( int(input() ) ) ) )

    # Use of list comprehension to do the printing
    [print(i**2) for i in range(int(input() ) ) ]

    # Use destructuring of iterables to pass into print()
    print( *(i**2 for i in range(int(input() ) ) ), sep='\n')

