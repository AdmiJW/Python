
class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


# Original function provided by Hackerrank
def print_from_stream(n, stream=EvenStream() ):
    if isinstance(stream, EvenStream):
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())


# Notice how the constructor only sets current value to 1 or 0
# therefore we can exploit that
def print_from_stream2(n, stream=EvenStream() ):
    stream.__init__()
    for _ in range(n):
        print(stream.get_next())