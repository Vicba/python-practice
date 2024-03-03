# Prototype Pattern

1. What is it?

   The Prototype Pattern is like making copies of your favorite toy. Imagine you have a cool robot, and you want another one just like it. Instead of building it from scratch, you take your robot, make a photocopy, and voila! You have a new robot buddy without starting over.

2. What is its purpose?

   The purpose of the Prototype Pattern is to create new things by copying existing ones. It's like having a master copy that serves as a template, and you can use it to make as many identical copies as you want.

3. When to use this?

   Use the Prototype Pattern when you want to create objects that are similar to existing objects without going through all the detailed setup again. It's handy when making copies is easier than creating something new.

4. Small Code Example

```python
import copy

class Robot:
    def __init__(self, name):
        self.name = name

    def clone(self):
        # Using copy.deepcopy to create an exact copy
        return copy.deepcopy(self)

# Original robot
original_robot = Robot("RoboMax")

# Making a copy
copied_robot = original_robot.clone()

# Let's see if it worked
print(original_robot.name)  # Output: RoboMax
print(copied_robot.name)    # Output: RoboMax

```

In this example, the clone method makes a duplicate of the original robot. Now you have two robots without redoing all the work to set up the second one.
