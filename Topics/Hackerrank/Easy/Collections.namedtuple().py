import collections

# Named Tuples are simply just tuples - immutable, can be accessed by indices of element starting from 0
#                                       except one fact: Each element can also be accessed by field names
#
# Think of it as ordered, immutable fixed sized dictionary.
#
# To use it, first we need to obtain the factory function which has the constructor for the desired tuple for us
#
# Import collections, and the function signature:
#
#           namedtuple( typename, fieldnames )
#
# typename is simply the class name for the tuple object. Name it meaningful like 'Student' etc
# fieldnames can be:
#       -   Iterable of strings
#       -   string consisting of field names seperated by space or comma
#
# Eg:
#       StudFactory = namedtuple( 'Student', 'id, name, age, class' )
#       stud = StudFactory( 1, 'Alex', 19, '3A1' )
#
#       stud[1]             // Alex
#       stud.name           // Alex
#


# Traditional, very readable method
def soln1():
    N = int( input() )
    StudFactory = collections.namedtuple('Student', input().split() )
    students = []

    for i in range(N):
        students.append( StudFactory( *input().split() ) )

    print( sum( int(stud.MARKS) for stud in students) / N )


# Compact version.
# First line - Retrieves N, and the second row is the column names. Use that to set up Factory function for named
#              tuple
# Second Line - Retrieve all students info and make all students into NamedTuple using list compresion and unpacking
#               operator
# Third line - Print sum of stud / N = average
def soln2():
    N, StudFactory = int(input() ), collections.namedtuple('Student', input().split() )
    students = [ StudFactory( *input().split() ) for i in range(N) ]
    print( sum( int(stud.MARKS) for stud in students) / N )


# Not using named tuple. Simple summing by determining the column number of marks
def soln3():
    N, index = int(input() ), input().split().index('MARKS')
    total = sum( int(input().split()[index] ) for i in range(N) )
    print( total / N )