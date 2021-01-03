#   We often deal with Collections of data in programming. Arrays, Sets, Maps...
#   Now, problem arises when we are handling large datasets.
#
#   Imagine this situation: You have millions of records in the database and now
#   you want to iterate over it in client's program. How would you implement the program?
#
#   Perhaps you will fetch immediately that millions of dataset into your program,
#   store it in memory as an Array, and iterate over it?
#   NO! That is both time consuming (Downloading) and space consuming! (MILLIONS record in memory!)
#
#   The better approach, is to have some sort of implementation that keeps track of our progress
#   among the millions of dataset, and only fetch a small portion (Like 10 records) each time the
#   data is required! Solved
#
#   And that, ladies and gentlemen, is Iterators

#   Iterators in Python are Objects (OBJECTS, MADE BY CLASS), that implement 2 essential methods:
#   >   __iter__()          Returns an iterator
#   >   __next__()          Obtain the next value from the iterator
#
#   Without us knowing about it, we actually use iterators quite often! It is used by for loop under the hood.

#######################################
#   See in built iterators used by List
#######################################

def example1():
    my_list = [1, 3, 5, 7, 9]

    my_iter = iter(my_list)  # Calls the __iter__() method. We can actually directly use my_list.__iter__()

    while 1:
        try:
            print(next(my_iter))  # Calls the __next__() method. We can also use my_list.__next__()
        except StopIteration as e:  # When the iterator is finished, it raises StopIteration exception
            print("We've reached the end!")
            break


##############################################
#   Implementing our very own range() method!
##############################################

class MyRange:

    #   MyRange Constructor. Same as range( start, end, step )
    def __init__(self, start, end=None, step=None):
        self.start = 0 if end is None else start
        self.end = start if end is None else end
        self.step = 1 if step is None else step

    # Just an overloaded constructor
    def __init__(self, end):
        self.__init__(0, end, 1)

    # Initialize the iterator's value, and return this object instance as iterator
    def __iter__(self):
        self.curr_pos = self.start
        return self

    # Obtains the next value
    def __next__(self):
        value = self.curr_pos
        self.curr_pos += self.step

        if value >= self.end and self.step > 0 or value <= self.end and self.step < 0:
            raise StopIteration(f'End of iteration from {self.start} to {self.end}')

        return value


def example2():
    for i in MyRange(10, 0, -2):
        print(i)


#   Iterators surely are space saver! However, we can see perhaps the implementation can get quite complex quickly.
#   is there a more elegant way to create iterators?
#
#   Introducing: GENERATORS
#
#   Generators, unlike iterators, are FUNCTIONS, that returns the next value upon invoked.
#   >   IT is a FUNCTION, unlike Iterators which are objects
#   >   Instead of using 'return' to return stuff, it uses 'yield' keyword
#
#   What special with the 'yield' keyword? It behaves like 'return' to return a value, but imagine like this:
#           Instead of terminating the execution of the codes in the function, it essentially "pauses" the
#           execution, returns the value, and will resume FROM THE SAME POINT on next function call.
#           An generator hits the end when the function encounters 'return' or hit the end of function
#           Due to this, there can be many 'yield's in a generator

######################
#   1 to 5 Generator
######################
def one_to_five():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


def example3():
    it = one_to_five()  # Calling the function will return a GENERATOR

    print(next(it))
    print("Do some stuff. The generator doesn't forget its progress!")
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))  # Throws exception here


##############################################
#   Fibonacci Number Generator (Literally)
##############################################

def fib_gen():
    curr = 0
    next = 1

    while 1:
        yield curr
        curr, next = next, curr + next


def example4():
    fg = fib_gen()

    for f in fg:
        if f > 100:
            break
        print(f)
