from abc import ABC, abstractmethod

# Define an abstract base class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

# A subclass that implements the abstract methods
class Dog(Animal):
    def sound(self):
        return "Bark"
    
    def move(self):
        return "Run"

# Another subclass that implements the abstract methods
class Cat(Animal):
    def sound(self):
        return "Meow"
    
    def move(self):
        return "Walk"

# Attempting to instantiate an abstract class will raise an error
try:
    animal = Animal()
except TypeError as e:
    print(e)

# Instantiating subclasses and calling their methods
dog = Dog()
cat = Cat()

print(f"Dog sound: {dog.sound()}, Dog move: {dog.move()}")
print(f"Cat sound: {cat.sound()}, Cat move: {cat.move()}")
