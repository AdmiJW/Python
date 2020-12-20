from collections import Counter


# Pythony way to do it. However it results in O(N^2) time and thus timeout
def soln1():
    _, members = input(), set( input().split() )
    print( [x for x in members if members.count(x) == 1][0] )


# Using 2 sets - ExistedOnce and ExistedMany
def soln2():
    _, members, existedOnce, existedMany = input(), input().split(), set(), set()
    for m in members:
        if m in existedOnce:
            existedOnce.discard(m)
            existedMany.add(m)
        elif m not in existedMany:
            existedOnce.add(m)

    print( existedOnce.pop() )


# Official answer - Using Mathematics
def soln3():
    K, members = int(input()), list(map(int, input().split()))
    total, setM = sum(members), set(members)
    total -= sum([K * x for x in setM])
    print(total // (1 - K))



# Using dictionary as frequency table
def soln4():
    _, members, freq = input(), input().split(), dict()
    [freq.update({x: freq.get(x) + 1 if freq.get(x) else 1}) for x in members]
    [print(x) for x in freq if freq[x] == 1]

# Using built in Counter from collectins module
def soln5():
    _, members = input(), Counter( input().split() )
    [ print(x) for x in members if members[x] == 1]
