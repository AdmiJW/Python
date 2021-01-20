from collections import deque

# As with all other languages that comes with basic Data structure classes,
# Python also has Deques
#
#   It is in collections class, deque
#
#   Key Methods:
#   deque.append(x) , deque.appendleft(x) for offer and push
#   deque.pop(), deque.popleft() for pop and poll
#   deque.extend(it), deque.extendleft(it) for appending items from iterable
#   deque.reverse(), deque.rotate() in O(N) time.


# Using exec()
def soln1():
    N, dq = int( input() ), deque()
    commands = [ input().split() for i in range(N) ]
    for cmd in commands:
        exec( f'dq.{cmd[0]}({cmd[1]})' if len(cmd) > 1 else f'dp.{cmd[0]}()')
    print(*dq)


# Using getattr()
def soln2():
    N, dq = int( input() ), deque()
    [ getattr(dq, cmd[0])(*cmd[1:]) for cmd in [input().split() for i in range(N) ] ]
    print(*dq)
