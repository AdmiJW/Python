
class Infantry:
    def move_forward(self):
        print("Infantry moved!")
    def fire_rifle(self):
        print("Infantry fired their rifle!")

class Tank:
    def drive_forward(self):
        print("Tank drove forward")
    def fire_missle(self):
        print("Tank fired a missle!")


# A Generic Adapter class in Python, not specifically binded to this use case
class Adapter:
    def __init__(self, object, **adapted_methods):
        self._object = object
        self.__dict__.update(**adapted_methods)

    # When we access attributes that aren't in adapted methods, search the attribute in object
    def __getattr__(self, attr):
        return getattr(self._object, attr)




if __name__ == '__main__':
    tank = Tank()
    # Supply the adaption method here
    tank = Adapter( tank,
                    walk_forward=tank.drive_forward,
                    fire_rifle=tank.fire_missle)

    # Now we can both use Infantry's format, or Tank's format
    tank.drive_forward()
    tank.walk_forward()
    tank.fire_missle()
    tank.fire_rifle()
