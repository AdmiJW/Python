

class myClass:
    static = 69

    def __init__(self, name):
        self.name = name

    def increment(self):
        self.static += 1

class1 = myClass('a')
class2 = myClass('b')

class1.increment()

print(myClass.static)
print(class1.static)
print(class2.static)



