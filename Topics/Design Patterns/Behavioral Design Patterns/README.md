# 🤹 Behavioral Design Patterns 🤹

---
## 1.0 - __Strategy__ 🗺

---

> __Reference [__HERE__](https://www.youtube.com/watch?v=v9ejT8FO-7I)__

__Strategy__ design pattern, by formal definition, goes as follows:

> Strategy design pattern defines a family of algorithm, encapsulates them and make them interchangable.

Makes no sense right? Let's see an example use case:

---

### Problem:

We have learnt about inheritances. Let's say we have a `Duck` abstract class, which will have 2 methods: `quack()` and `fly()`.

Now, we will have 2 child classes inheriting from this `Duck` class: `CityDuck` and `WildDuck`.

Let's imagine some problem here:

* What if both ducks share the same `quack()` behavior? We shouldn't implement the function into the base class `Duck` because maybe there are more type of `Duck` that doesn't share the same `quack()` behavior.

* Let's say that `CityDuck` doesn't know how to fly. We are still having to implement the `fly()` method regardless due to inheriting from the `Duck` class.

The inheritance way of solving this problem, especially case 1, is to __use more inheritance__. For the `Ducks` that will have certain `quack()` behavior, we may make a `NormalQuackingDuck` class, that will be in turn inherited by the `CityDuck` and `WildDuck`.

However, as the program grows and more ducks are introduced, the inheritance tree quickly expands, and complexity goes out of hand (Inheritance forms a tree, and common behaviors cannot be shared __Horizontally__ - Like how `CityDuck` and `WildDuck` cannot share the same `quack`)

---

### Solution:

You may describe __Strategy__ pattern as *"using composition instead of inheritance"*. What if each of these methods (Eg: `quack`), can be an object and assigned to a `Duck` instance? That quickly solves the sharing problem faced earlier!

Instead of making deep, inheritance tree like introducing `NormalQuackingDuck` and whatsoever, let's instead extract those behaviors out and make them objects! (For __Java__, use abstract classes):

* `QuackBehavior` - must define `quack()` for those inheriting it
* `FlyBehavior` - must define `fly()` for those inheriting it

Now, since both ducks is able to quack and fly, the class definition would look something like:

```java
class Duck {
    QuackBehavior quackingBehavior;
    FlyBehavior flyingBehavior;
    ...

    void quack() {
        this.quackingBehavior.quack();
    }
    ...
}
```

Since both `CityDuck` and `WildDuck` share the same quacking behavior, we would define a __concrete__ `QuackBehavior` instance that can be used by both classes:

```java
class NormalQuackBehavior extends QuackBehavior {
    public void quack() {...}
}
```

---

Now, we can get rid of the inheritance tree in its entirety! All the behaviors of `Duck`s are __extracted__ away and implemented in the form of composition rather than inheritance!

It become a lot easier to extend the functionality, whether we want to add a `RubberDuck`, or add a `swim()` method

<br><br>



---
## 2.0 - __Observer__ 👀

---

__References [HERE](https://www.youtube.com/watch?v=_BpmfnqjgzQ)__

__Observer__ pattern, official defined as:

> A one to many dependency, where when the core dependency changes its state, all the other dependencies are notified

### Problem:

Think of this as a Weather System, where when the Station changes the weather state, all the subscribed clients (your phone, other weather websites) needs to be notified in real time.

This design pattern essentially helps to change from __poll__ process to __push__ process. In __polling__, the observers has to keep checking on the observable at fixed intervals. However, this process may be taxing on the observable (server), and still possibly causes delay in information (Say weather updates in 1s but observer polling interval is 10s). Instead in __push__, the server notifies all the observers about the update.

---

### Solution:

Conceptually, __Observer__ design pattern is implemented by first having two __interfaces__:

* `Observer` - Need to implement `addObserver`, `removeObserver` and `notify` method on inherited classes
* `Observable` - Need to implement `onUpdate` method on inherited classes

The concrete `Observable` classes, like `WeatherStation`, should keep track of a list of `Observable`s and notify them whenever there is an update.

Also, it is suggested that concrete `Observer`s should keep a reference to the `Observable` they are subscribed to, to get the state whenever they want, say through `weatherStation.getWeather()`


<br><br>



---
## 3.0 - __Command__ 🗯

__Reference [HERE](https://www.youtube.com/watch?v=9qA5kw8dcSU)__

The definition:

> __Command__ pattern encapsulates a request as object, thereby letting us parameterize other object with different request queue or by require and support undoable requests.

In essence, __Command__ design pattern is similar to __Strategy__ pattern, where the methods of `Invoker` is an object rather than merely functions.

The __Command__ pattern consists of `Invoker` (the one sending the commands), `Receiver` (the one receiving the commands), and `Command` themselves. An abstract `Command` would commonly have an `execute()` and `unexecute()` method, and used to create concrete `Command`s like `TurnOnCommand` and `ChangeSpeedCommand`

---

### Problem:

Think of this: You are programming for a programmable/configurable remote control, where each button can be configured to perform different actions. How would you program such system?

Maybe you suggest to have a internal state keeping track of what each button does, encoded as string or integers. Like:

```json
{
    button1Action: 'turnon',
    button2Action: 'changeSpeed'
}
```

Then in the actual event handler, we could:

```java
public void onButton1Pressed(args) {
    if (state.button1Action == 'turnon') ...
    else...
}
```

---

### Solution:

However, if you learnt __Strategy__ pattern, where methods themselves are already objects, suddenly we can just have our code like so:

```java
class RemoteControl {
    Command button1Command = new TurnOnCommand(receiver);
    Command button2Command = new ChangeSpeedCommand(receiver);

    public void onButton1Pressed(args) {
        button1Command.execute(args);
    }
}
```

The actual implementation of the command is now encapsulated inside the concrete `Command` itself. For example in the `TurnOnCommand`, `exeucte()` will contain `receiver.turnOn()`.

Now, since the `Command` itself had became class attribute, the `Command` suddenly become very easily swappable in the `Invoker`!

---

### Furthermore...

That's not all the benefits of __Command__ pattern! Think: functions themselves cannot possibly be saved in data structure (Unless you are using a language where functions are first class citizens), but `Command` object can! This opens up the possibility of __History__ and __Undo__ functionality!

Previously in our `Command` interface, we have `execute()` and `unexecute()`. If those `Command` are saved in the `Invoker` as a __Stack__ data structure, we could now very easily perform __undo__! Just pop the top `Command` and call its `unexecute()`!

---