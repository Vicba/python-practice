# Bridge Pattern

1. What is it?

   The Bridge Pattern is like a traffic controller for your code. It helps separate the main part of your program from its different variations.

1. What is its purpose?

   The purpose of the Bridge Pattern is to make your code more flexible. It lets you change and add parts without affecting the rest of your program.

1. When to use this?

   Use the Bridge Pattern when you have different parts in your program that can change independently. It's great when you want to avoid a tangled mess in your code.

1. Small Code Example

```python
# Abstraction: The main part of your program
class Shape:
    def __init__(self, drawing):
        self.drawing = drawing

    def draw(self):
        pass

# Implementor: The different variations
class CircleDrawer:
    def draw_circle(self):
        print("Drawing a circle")

class SquareDrawer:
    def draw_square(self):
        print("Drawing a square")

# Refined Abstraction: Specific shape using an implementor
class Circle(Shape):
    def draw(self):
        self.drawing.draw_circle()

class Square(Shape):
    def draw(self):
        self.drawing.draw_square()

# Usage
circle = Circle(CircleDrawer())
square = Square(SquareDrawer())

circle.draw()  # Output: Drawing a circle
square.draw()  # Output: Drawing a square

```

In this example, Shape is the main part, and Circle and Square are specific shapes. The CircleDrawer and SquareDrawer are the different ways to draw these shapes. The Bridge Pattern helps to keep things organized and easy to change.
