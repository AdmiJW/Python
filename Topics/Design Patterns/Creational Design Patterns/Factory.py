
# Dog Class
class Dog:
    def __init__(self, name):
        self._name = name

    def speak(self):
        print(f"Woof! (I am {self._name})")

# Cat Class
class Cat:
    def __init__(self, name):
        self._name = name

    def speak(self):
        print(f"Meow! (I am {self._name})")



# This is where factory design pattern applies:
# A function which helps you to construct objects
def get_pet(name, type='dog'):
    if type == 'dog':
        return Dog(name)
    elif type == 'cat':
        return Cat(name)



if __name__ == '__main__':
    pet1 = get_pet("Alexander", 'dog')
    pet2 = get_pet("Milly", 'cat')

    pet1.speak()
    pet2.speak()
