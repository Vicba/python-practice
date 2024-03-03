# Builder Pattern

1. What is it?

   The Builder Pattern is like following a recipe to build something step by step. Imagine making a burger – you add the bun, then the patty, then lettuce, and so on, until you have a delicious burger!

1. What is its purpose?

   Its main job is to make building complex objects easier. Instead of putting everything together at once, the Builder Pattern lets us construct an object piece by piece. It's like playing with Lego bricks – you add one piece at a time until your creation is complete.

1. When to use this?

   Use the Builder Pattern when you have an object with lots of parts, and you want to create it in different ways. It's handy when you want to customize the way an object is made without making the process too complicated.

1. Small Code example

```python
# Imagine building a car with different features

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def add_engine(self, engine):
        self.car.engine = engine

    def add_color(self, color):
        self.car.color = color

    def add_wheels(self, wheels):
        self.car.wheels = wheels

    def get_car(self):
        return self.car

class Car:
    def __init__(self):
        self.engine = None
        self.color = None
        self.wheels = None

# Using the builder pattern to create a car
builder = CarBuilder()
builder.add_engine("V8")
builder.add_color("Red")
builder.add_wheels(4)

my_car = builder.get_car()

```

In this example, the CarBuilder helps us build a car by adding different parts one by one. It makes creating cars more flexible and easier to understand, just like building with Lego bricks.
