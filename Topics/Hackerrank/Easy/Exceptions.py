

# General Exception handling using Exception only
def soln1():
    for i in range( int(input() ) ):
        try:
            i, j = map(int, input().split() )
            print(i // j)
        except Exception as e:
            print("Error Code:", e)


# More Specific Exception Handling
def soln2():
    for i in range( int(input() ) ):
        try:
            i, j = map(int, input().split() )
            print(i // j)
        except (ZeroDivisionError, ValueError) as e:
            print("Error Code:", e)

