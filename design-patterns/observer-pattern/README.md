# Observer Pattern

1. What is it?

   The Observer Pattern is like a buddy system in coding. Imagine you have a cool gadget that tells your friends when you're doing something fun. The Observer Pattern is like that gadget for your code. It helps different parts of your program stay updated about what's happening in another part.

2. What is its purpose?

   The main job of the Observer Pattern is to make sure that when one part of your code changes, other parts that are interested get to know about it. It's like sharing exciting news with your friends so everyone can join the fun!

3. When to use this?

   Use the Observer Pattern when you have some parts of your code that depend on what's happening in another part, and you want them to know when things change. It's like having a magical mirror that shows everyone the same picture whenever something cool happens.

4. Small Code example

```python
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        print(f"Got the news: {message}")

# Example Usage
subject = Subject()

observer1 = Observer()
observer2 = Observer()

subject.add_observer(observer1)
subject.add_observer(observer2)

subject.notify_observers("Exciting Event!")

```

In this example, the Subject is like the cool gadget, and the Observer is like a friend who gets notified. When the Subject has some news (calls notify_observers), all the attached observers (friends) get the update.
