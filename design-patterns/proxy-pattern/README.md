# Proxy Pattern

1. What is it?

   The Proxy Pattern is like having a superhero friend who helps you interact with the world. Instead of doing everything yourself, your friend can handle some tasks for you.

2. What is its purpose?

   The main goal is to control access to something. Imagine you have a cool gadget, but you want to decide who gets to use it. The Proxy Pattern helps you manage and protect access to your gadget.

3. When to use this?

   Use the Proxy Pattern when you want to add a layer of control around an object. For example, when you share a game with friends, the proxy can make sure they play it nicely without breaking anything.

4. Small Code example

```python
# Let's create a proxy for a gaming console

class GamingConsole:
    def play_game(self):
        pass

class RealGamingConsole(GamingConsole):
    def play_game(self):
        print("Playing the game!")

class GameConsoleProxy(GamingConsole):
    def __init__(self, age):
        self.age = age
        self.real_console = RealGamingConsole()

    def play_game(self):
        if self.age < 16:
            print("Sorry, you are too young to play.")
        else:
            self.real_console.play_game()

# Example usage
player1 = GameConsoleProxy(age=14)
player1.play_game()  # Output: Sorry, you are too young to play.

player2 = GameConsoleProxy(age=18)
player2.play_game()  # Output: Playing the game!

```

In this example, the GameConsoleProxy decides if someone is old enough to play the game on the RealGamingConsole. It acts as a protective friend for the gaming console.
