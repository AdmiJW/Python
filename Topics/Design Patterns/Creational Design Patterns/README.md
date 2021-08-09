# ⚙️ Creational Design Patterns ⚙️

---
## 2.0 - __Factory__ 🏭

---

__Factory__ encapsulates object creation. Factory is an object specializing in creating other objects.

In Layman's term, Factory can be thought as functions that create and return objects based on user input, or internal program state. It can return object of different classes. Eg: it can create instances of both `Dog` and `Cat`

__Problem:__
* Uncertainties in types of objects
* Decisions to be made at runtime regarding which classes to use

__Example Case:__
* Originally, your pet shop sells only dogs. Now, you expanded your business to sell also cats. Your system must be able to handle dogs as well as cats, and show how each of them speak


<br><br>


---
## 2.1 - __Abstract Factory__ 🏭

---

__Abstract Factory__ is useful when the user expects to receive a family of related objects at a given time, but don't have to know which family it is until runtime.

Recall that __Factory__ is simply a function that create objects. Say if I am a animal products company that produces pets, pet foods, pet accessories for multiple type of animals (and each of these specific product, is an object). Do I need to create a factory for all of these? Eg:

```python
pet_factory = ...
pet_food_factory = ...
pet_accessory_factory = ...
...
```

__Abstract Factory__ can be thought as factory of factories. It will contain multiple factories that produce __closely related__ objects. For example, a `CatFactory` should contain `cat_factory`, `cat_food_factory`, and `cat_accessory_factory` and have abstract *"order forms"* that is able to use those factory to create what we wanted.

At the outermost layer, what we know is only __abstract factory__ and __abstract product__ only. (Eg: We know there is a `pet_factory` and it produces `pet`, `pet_food`, `pet_accessories`). During runtime, only then it is assigned __concrete factory__ and produces __concrete products__ (Eg: At runtime, the factory is set to `CatFactory`, which produces `cat`, `cat_food`, `cat_accessories`)

Due to this, __Polymorphism__ is heavily used (Although in `Python` duck-typing is used)


<br><br>


---
## 2.2 - __Singleton__ 🦠

---

A __Singleton__ is useful in providing global variables across multiple modules/scripts. 

Essentially, a singleton is simply the __ONLY INSTANCE__ that a class will ever create in the program lifecycle. The class will only create THAT SINGLE INSTANCE.

This is useful especially for __information cache__. 

If you've ever used `mongoose`, which is Javascript's library for working with `MongoDB` database, once the connection to the database is established via the singleton object itself, the connection remains when the module is required in other scripts.

If you are required to read data from a file and access it in multiple scripts, instead of reading the file over and over again in every script, use a singleton so that the file is only __READ ONCE__.

---

In Python, module itself is already a singleton. If we have:
* `test1.py` - which have `print("Hello World")`
* `test2.py` - which have `import test1`
* `test3.py` - which have `import test1` and `import test2`

By running `test3.py` you will only see `Hello World` printed once only. This is because modules in Python are singleton.

---

In other languages like Java, creating a Singleton may require the following steps:

* Creating a __static__ variable which holds an instance of itself, which is to be shared
* Making the constructor __private__ to prevent instantiating of the class
* Creating a public method to retrieve the singleton object

```java
class Singleton {
    int value = 123;
    String name = "Hi";

    // Singleton
    static Singleton obj = new Singleton();

    // Make constructor private
    private Singleton(){}

    // Method to retrieve singleton
    public static Singleton retrieve() {
        return obj;
    }
}
```


<br><br>


---
## 2.3 - __Builder__ 🏗

---

__Builder__ is a solution to a anti-pattern called *Telescoping constructor*. 

A *Telescoping constructor* is essentially a constructor of a class that is bloated: maybe it has 10 required parameters to initialize all the fields of the object, which is a lot. Maybe you will work around with having separate setters, but still that isn't very elegant.

A __Builder__'s job is to construct the complex object, but hiding away all the pesty details away from the user. Imagine the original object requires 10 parameters to construct, but using builders, you can choose 3 of them to fill only.

The __Builder__ design pattern usually consist of these main components:

|Components|Description|
|-|-|
|__Director__| In charge of actually building the object via Builders; The class using the builders |
|__Abstract Builder__|The base builder class which will be inherited by __Concrete Builders__ (Eg: `PhoneBuilder`)|
|__Concrete Builders__|The actual builders which will construct the object, making some default assumptions (Eg: `NokiaBuilder`, `SamsungBuilder`)|
|__Product__| The actual object being built (Eg: `Nokia`)|

One way to implement traditionally, is to have a __Abstract Builder__ that has a constructor, that builds the object with required parameters only (or inferred). Through providing setters, other optional fields can be set. Eg:

```java
Phone phone = new NokiaPhoneBuilder("3310").setPrice(100).setColor('blue').getPhone();

// The Abstract Builder will specify constructor, setPrice, setColor, getPhone etc and must be inherited by concrete builders
```

For `Javascript`, things can be done via Javascript Objects to set optional parameters.

```javascript
class Phone {
    constructor(name, { price, color } = {}) {
        ...
    }
}

const phone = new Phone('3310', {
    price: 100,
    color: 'blue'
})
```

<br><br>


---
## 2.4 - __Prototype__ 🧬

---

__Prototype__ clone objects according to a prototypical instance. It is useful when dealing with creating many identical objects individually, where we would prefer cloning instead.

For example, let's say in our forum system, each user comment is an object. Instead of creating each comment one by one from the database (which is expensive due to connection to database), we can instead apply __Prototype__ design pattern, fetch a bunch of comments from database, create one individual comment object, and clone it for other comments.

The implementation may be ambiguous, but the point remains
* Create a prototypical instance
* Clone it whenever we need a replica