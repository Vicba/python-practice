# State Pattern

1. What is it?

   The State Pattern is a design pattern in Python that helps organize and manage the behavior of an object by representing its various states as separate classes.

2. What is its purpose?

   The purpose of the State Pattern is to allow an object to alter its behavior when its internal state changes. Instead of having a single monolithic class with many if-else statements, different states are encapsulated in separate classes, making the code more modular and maintainable.

3. When to use this?

   Use the State Pattern when an object can have different behaviors based on its internal state, and these behaviors need to change dynamically during the program's execution. It is handy when you find yourself using multiple if-else conditions to manage various states.

4. Small Code Example

```python
# Define state classes

class State:
    def handle(self):
        pass

class StateA(State):
    def handle(self):
        return "Handling State A"

class StateB(State):
    def handle(self):
        return "Handling State B"

# Context class that uses the states

class Context:
    def __init__(self):
        self.state = StateA()

    def change_state(self, new_state):
        self.state = new_state

    def request(self):
        return self.state.handle()

# Example Usage

context = Context()
print(context.request())  # Output: Handling State A

context.change_state(StateB())
print(context.request())  # Output: Handling State B

```

In this example, the Context object can change its internal state, and its behavior adapts accordingly. The State Pattern helps keep the code organized and makes it easier to add new states in the future.
