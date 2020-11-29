# Python List
#   append( elem )
#   extend( iterable )       -Combine another list into end of the list
#   insert( idx, elem )      -After insert, elem will in index idx, the original is pushed idx+1
#   remove( elem )           -Removes only first occurrence
#   pop()
#   index( elem )            -Index of first occurrence
#   count( elem )
#   sort()
#   reverse()


if __name__ == '__main__':
    N = int(input())

    # Read input all together first using List Comprehension
    commands = [input().split() for i in range(N)]

    # List
    li = []

    # Read each command the traditional way
    for command in commands:
        if command[0] == 'insert':
            li.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(li)
        elif command[0] == 'remove':
            li.remove(int(command[1]))
        elif command[0] == 'append':
            li.append(int(command[1]))
        elif command[0] == 'sort':
            li.sort()
        elif command[0] == 'pop':
            li.pop()
        else:
            li.reverse()

    # More automation and less hardcoding: Introducing eval() function
    # Notice all commands are methods associated with the list object
    # except the print() part
    for command in commands:
        if command[0] == 'print':
            print(li)
        else:
            eval(f'li.{ command[0] }({ ",".join(command[1:]) } )')  # f-strings. Python 3.6+

    # Instead of eval() which evaluates the entire string as code, it is
    # recommended to use getattr() function which calls the method of an
    # object
    # If it is a object property, it will return the value of property.
    # If it is a method, it will return the function object itself, which
    # we can then proceed to execute it
    for command in commands:
        if command[0] == 'print':
            print(li)
        else:
            arguments = [int(x) for x in command[1:]]
            getattr(li, command[0])(*arguments)