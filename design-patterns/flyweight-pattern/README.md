# Flyweight Pattern

1. What is it?

   The Flyweight pattern is a design pattern in Python that helps to save memory by sharing common parts of objects between multiple objects. It's like having a blueprint for creating objects, where some parts are reused instead of creating them again and again.

1. What is its purpose?

   The purpose of the Flyweight pattern is to reduce memory usage and improve performance by reusing common parts of objects instead of storing them separately for each object. It's like using the same Lego piece multiple times instead of getting a new one for each part of your Lego creation.

1. When to use this?

   You can use the Flyweight pattern when you have lots of objects that share common parts, and you want to save memory. For example, if you're making a game with lots of trees, instead of storing the same tree image separately for each tree, you can use the Flyweight pattern to share the image among all the trees.

1. Small Code example

```python
class Tree:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class TreeFactory:
    trees = {}

    @staticmethod
    def get_tree(name, color):
        if (name, color) not in TreeFactory.trees:
            TreeFactory.trees[(name, color)] = Tree(name, color)
        return TreeFactory.trees[(name, color)]

# Example usage
factory = TreeFactory()
tree1 = factory.get_tree("Pine", "Green")
tree2 = factory.get_tree("Maple", "Red")
tree3 = factory.get_tree("Pine", "Green")

print(tree1 is tree2)  # Output: False, because they are different objects
print(tree1 is tree3)  # Output: True, because they share the same parts

```

In this example, we have a TreeFactory that creates tree objects. If we ask the factory for a tree with the same name and color, it will return the same object instead of creating a new one. This helps to save memory because we're reusing common parts of the objects.
