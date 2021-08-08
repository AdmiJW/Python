
# As you can see, these objects are kinda similar - They have pet itself (Cat/Dog) and pet food (CatFood / DogFood)
# and also accessories (CatAccessory / DogAccessory)

#################
# Cats
#################
class Cat:
    def __init__(self, name):
        self._name = name
    def speak(self):
        print(f"Meow! (I am {self._name})")

class CatFood:
    def __init__(self, brand):
        self._brand = brand
    def __str__(self):
        return f"Cat food brand {self._brand}"

class CatAccessory:
    def __init__(self, brand):
        self._brand = brand
    def __str__(self):
        return f"Cat accessory brand {self._brand}"

##################
# Dogs
##################
class Dog:
    def __init__(self, name):
        self._name = name
    def speak(self):
        print(f"Woof! (I am {self._name})")

class DogFood:
    def __init__(self, brand):
        self._brand = brand

    def __str__(self):
        return f"Dog food brand {self._brand}"

class DogAccessory:
    def __init__(self, brand):
        self._brand = brand
    def __str__(self):
        return f"Dog accessory brand {self._brand}"

#########################################################################################
# Concrete Factories - They must have common method to create objects like produce_pet()
#########################################################################################
class CatFactory:
    def produce_all(self, pet_name, food_brand, accessory_brand):
        return Cat(pet_name), CatFood(food_brand), CatAccessory(accessory_brand)
    def produce_pet(self, pet_name):
        return Cat(pet_name)
    def produce_food(self, food_brand):
        return CatFood(food_brand)
    def produce_accessory(self, accessory_brand):
        return CatAccessory(accessory_brand)


class DogFactory:
    def produce_all(self, pet_name, food_brand, accessory_brand):
        return Dog(pet_name), DogFood(food_brand), DogAccessory(accessory_brand)
    def produce_pet(self, pet_name):
        return Dog(pet_name)
    def produce_food(self, food_brand):
        return DogFood(food_brand)
    def produce_accessory(self, accessory_brand):
        return DogAccessory(accessory_brand)

#######################################################################################
# Here is where Abstraction Take Place (Where Abstract Factory, self._factory resides)
#######################################################################################
class PetShop:
    def __init__(self):
        self._factory = CatFactory()
    def change_factory(self, factoryType='cat'):
        if factoryType == 'cat':
            self._factory = CatFactory()
        else:
            self._factory = DogFactory()

    def make_order(self, order_type='all', *args):
        pet, food, accessory = None, None, None

        # Check order type and produce corresponding goods
        if order_type == 'all':
            pet, food, accessory = self._factory.produce_all(*args)
        elif order_type == 'pet':
            pet = self._factory.produce_pet(*args)
        elif order_type == 'food':
            food = self._factory.produce_food(*args)
        elif order_type == 'accessory':
            accessory = self._factory.produce_accessory(*args)

        # Output
        if pet is not None:
            pet.speak()
        if food is not None:
            print(food)
        if accessory is not None:
            print(accessory)


# Main
if __name__ == '__main__':
    pet_shop = PetShop()
    pet_shop.make_order('all', 'Mimi', 'Cateats', 'Wool')
    pet_shop.change_factory('dog')
    pet_shop.make_order('all', 'Alexander', 'Dogeats', 'Ball')