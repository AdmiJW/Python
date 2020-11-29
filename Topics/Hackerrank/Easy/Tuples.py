
# Tuples
#   There is a misconception that a tuple is formed by a bracket (). In reality, IT IS THE
#   COMMA SIGN , THAT DEFINES A TUPLE
#
#   When a tuple is used on the left side of a operator, every element in the tuple is treated one by one.
#
#   Eg:     b,a = a,b           <= Assignment operator. b is assigned to a, while a is assigned to b
#   Eg:     (1,2) > (3,4)       <= It is equivalent to any() function in this case
#   Eg:     (1,2,3) == (2,3,4)  <= Also equivalent to any()

#   Common mistake:      1,2 == (1,2)   <= Might seem legit, but what is done is that it forms a tuple
#                                          1 is treated as one element, the 2 == (1,2) is another..


if __name__ == '__main__':
    N = int(input() )
    tup = tuple(int(x) for x in input().split() )
    print( hash(tup) )
