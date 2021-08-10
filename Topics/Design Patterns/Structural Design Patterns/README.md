# ⚙️ Structual Design Patterns ⚙️

---
## 3.0 - __Decorator__ 🎀

---

__Reference [HERE](https://www.youtube.com/watch?v=GCraGHx6gso)__

__Decorator__ is a design pattern that is defined as:

> Decorator attachs a additional responsibility to an object __dynamically__ (without changing source code). It is an flexible alternative to subclassing for extending functionality

To put in another way, an decorator will manipulate the returning value or any parameters sent to the object, at __runtime__ without changing the code itself.

Traditionally (like __Java__), this is done by wrapping an object with a *Decorator* class, which *(this may sound confusing)*, should be also the subclass of the base class itself.

---

### Problem:

In the book __Head First Design Pattern__, the example provided is that we have a Cafe shop that will have `Beverages` (abstract class) like `Espresso` and `Mocha`.

These `Beverages` will have methods like `getCost` and `description`.

 However, problem arises when we need a way to have optional toppings like `Soy Milk`, `Chocolate`, or `WhippedCream` for those beverages. Initially, we may have some ideas of the implementation:

 * Subclassing for the combinations. Say `ChocolateMocha` or `WhippedCreamEspresso`. However, what if toppings can be mixed? Like `SoyChocolateMocha`? How many combinations will it result in?

 * Implementing boolean/integer variables in the `Beverage` itself, like variables `hasSoy` or `chocolateCount`. However, this will pose a potential __Interface Segregation__ issue. Say we started selling `Tea`. `Tea` should never use `hasChocolate` because it is a absurd combination!

 ---

 ### Solution:

 Instead, the idea is that we first start with two interfaces:

 * `Beverage` - Having `getCost` and `describe` method
 * `BeverageDecorator` - __Extends `Beverage` class__. Also, each `BeverageDecorator` should have an attribute `Beverage` acting as inner object which it decorates.

*(Over here, you can see the Decorator, `BeverageDecorator`, __is a Beverage__ and __has a Beverage__). A decorator should be the same type with the object it is decorating, and has the same type  with the object it is decorating*

Then we can go ahead and create concrete classes of `Beverage` like `Espresso` and `Mocha`, as well as concrete classes of `BeverageDecorator` like `Soy MilkDecorator` and `ChocolateDecorator`.

As you might see where this is going, when we want to add Chocolate to our Mocha, we simply create a `ChocolateDecorator` decorator and pass in our original `Mocha` inside, like:

```java
Beverage myBeverage = new ChocolateDecorator( new Mocha() );
myBeverage.getCost();
```

As we are calling the `getCost()` method, the `ChocolateDecorator` will return the __base price__ of whatever the beverage it is having as attribute (In this case, `Mocha`), and add an additional price to it, if that is what your intention.

You can see, this pattern is similar to recursion - Decorator will recurse until it hits the base case, in this case it's `getCost()` of `Mocha`

---

In Python, using decorator is fairly simple because it is already built in.

For example, using decorators, we can easily create a new function that extends the original function by running code before and after the execution, or modify the return value of the original function.

The subsequent design patterns such as __Adapter__, __Composite__ and __Strategy__, are all related to __Decorator__.

<br><br>


---
## 3.1 - __Proxy__ ⏱️

---

__Proxy__ solves the problem of having to instantiating a resource intensive object by only creating it when absolutely necessary. 

In other words, it provides a class which will limit access to instantiation of another class

This design pattern is mainly used for security reasons, or object instantiation is expensive, or because it is accessed from a remote location.

For example, you may want only one user to be able to access a particular ATM machine at a time. In this situation, a proxy class may be useful to check whether the particular ATM machine is occupied and does it allow other party to access it.


<br><br>

---
## 3.2 - __Adapter__ 🔌

---

__Adapter__, exactly what you think it is. Adapter solves the problem of incompatible interfaces (Different expectation of method names or attributes).

For example, when developing a war based game, we have a `Infantry` class that has `walk_forward()` and `fire_rifle()` method. Now, we added a `Tank` class that has `drive_forward()` and `fire_missle()` method. However, the commander wants to use the `Tank` classes with the same method names as those of `Infantry`'s, which is `walk_forward()` and `fire_rifle()`. A adapter design pattern needs to be used to "translate" the method calls!



<br><br>

---
## 3.3 - __Composite__ 🗂

---

A __Composite__ Design pattern uses a tree data structure to represent part-whole relationships. The tree data structure used will usually involve recursion algorithms.

For example, we want to implement a `Menu` (Interface). Inside, it may have `MenuGroup` (Composite class) which may contain other `MenuGroup`s or simply `MenuItem`.

Then, when we want to print out the menu, we call `print_menu()` on the top level menu, and it will print the name of itself, and recurse on its children.