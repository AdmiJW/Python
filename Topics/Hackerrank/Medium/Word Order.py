from collections import OrderedDict, Counter

# We essentially have to implement a Counter, but with the ordering of input remained
# Therefore OrderedDict is useful here.


# Traditional, readable solution
def soln1():
    N = int(input() )
    freq = OrderedDict()

    for i in range(N):
        s = input()
        freq[s] = freq[s] + 1 if s in freq else 1

    print( len(freq) )
    print( *freq.values() )


# Compressed solution. Using list comprehension and freq.update method to execute the updating
def soln2():
    strs, freq = [input() for i in range(int(input()))], OrderedDict()
    list( map(lambda s: freq.update({s: freq[s] + 1}) if s in freq else freq.update({s: 1}), strs) )
    print(len(freq), ' '.join( map(str,freq.values() ) ), sep='\n')


# This one is very special solution. We created a OrderedCounter just by using Multiple Inheritance!
#
# For constructor, the Counter()'s constructor is prioritized. However since Counter class will call
# for insertion function, the insertion of OrderedDict will be called instead of the normal dict's
# insertion function
def soln3():
    class OrderedCounter(Counter, OrderedDict):
        pass
    freq = OrderedCounter( input() for i in range(int(input())))
    print( len(freq), ' '.join( map(str, freq.values() ) ), sep='\n')