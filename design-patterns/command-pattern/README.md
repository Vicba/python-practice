# Command Pattern

1. What is it?

   The Command Pattern is like giving your computer a to-do list. Instead of directly telling it what to do, you write down a task on a piece of paper, and your computer will know how to follow that instruction.

2. What is its purpose?

   The purpose is to make things flexible and organized. Imagine you have a remote control for your TV. The command pattern is like pressing a button on the remote – it tells the TV what to do without you needing to know all the details.

3. When to use this?

   Use the Command Pattern when you want to separate the sender of a request (like pressing a button) from the object that knows how to perform that request. It's handy when you want to queue tasks, undo actions, or even make a smart remote control for your code.

4. Small Code Example:

```python
# Imagine a simple TV remote control

# Command interface
class Command:
    def execute(self):
        pass

# Concrete Command
class TurnOnCommand(Command):
    def execute(self):
        print("TV turned on")

# Receiver
class TV:
    def turn_on(self):
        print("TV is on")

# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

# Client code
tv = TV()
turn_on_command = TurnOnCommand()

remote = RemoteControl()
remote.set_command(turn_on_command)
remote.press_button()

```

When you run this code, it prints "TV turned on" without directly calling TV methods. The remote control holds the command and makes the TV do things without knowing the details.
