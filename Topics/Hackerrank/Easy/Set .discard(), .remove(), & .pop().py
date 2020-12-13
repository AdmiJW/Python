
# In python, sets has 3 element removal functions:
#
#   >   remove() - Remove specified element. Raise KeyError if non-existent
#   >   discard() - Remove specified element. Return None if non-existent
#   >   pop()     - Remove random element in the set


# Solving problem traditional way
def soln1():
    N = int(input() )
    set_A = set( map(int, input().split() ) )   # Set of integers

    M = int(input() )
    commands = tuple(input().split() for i in range(M) )    # Split comands

    for cmd in commands:
        if len(cmd) == 1:      # Pop
            set_A.pop()
        elif cmd[0] == 'remove':   # Remove
            set_A.remove( int(cmd[1] ) )
        elif cmd[0] == 'discard':   # Discard
            set_A.discard( int(cmd[1] ) )

    return sum(set_A)


#   Condensed version using list comprehension to execute codes
def soln2():
    _, set_A, M = input(), set( map(int, input().split() ) ), input()
    commands = tuple( input().split() for i in range( int(M) ) )

    [set_A.pop() if len(cmd) == 1 else set_A.remove( int(cmd[1]) ) if cmd[0] == 'remove'
     else set_A.discard( int(cmd[1]) ) for cmd in commands]
    return sum(set_A)

#   Using eval() to execute commands in one line
def soln3():
    _, set_A, M = input(), set(map(int, input().split())), input()
    commands = tuple(input().split() for i in range(int(M)))

    [eval(f'set_A.{cmd[0]}({cmd[1] if len(cmd) == 2 else ""})') for cmd in commands]

    print(sum(set_A))


if __name__ == '__main__':
