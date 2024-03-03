# Template Pattern

1. What is it?

   The Template Pattern is a design pattern in Python that helps us create a blueprint for a process. It defines the steps of a certain algorithm but lets the specific details be implemented by individual parts of the code.

2. What is its purpose?

   The purpose of the Template Pattern is to provide a structure for an algorithm and allow different parts of the code to customize certain steps. It promotes code reusability and helps in organizing code in a way that makes it easy to understand and maintain.

3. When to use this?

   You should use the Template Pattern when you have a process that has a common structure but can have different implementations for certain steps. It's handy when you want to avoid duplicating code and allow flexibility in how parts of the algorithm are carried out.

4. Small Code example

```python
class RecipeTemplate:
    def prepare_ingredients(self):
        raise NotImplementedError("This method should be overridden")

    def cook(self):
        raise NotImplementedError("This method should be overridden")

    def serve(self):
        raise NotImplementedError("This method should be overridden")

    def make_recipe(self):
        self.prepare_ingredients()
        self.cook()
        self.serve()

class PizzaRecipe(RecipeTemplate):
    def prepare_ingredients(self):
        print("Gather pizza dough, sauce, cheese, and toppings")

    def cook(self):
        print("Bake in the oven until the crust is golden and cheese is melted")

    def serve(self):
        print("Slice the pizza and serve hot")

class PancakeRecipe(RecipeTemplate):
    def prepare_ingredients(self):
        print("Mix flour, eggs, and milk to make pancake batter")

    def cook(self):
        print("Pour batter on a hot griddle and flip until both sides are golden brown")

    def serve(self):
        print("Top with syrup and enjoy your pancakes")

# Example Usage
pizza_recipe = PizzaRecipe()
pizza_recipe.make_recipe()

pancake_recipe = PancakeRecipe()
pancake_recipe.make_recipe()

```

This code shows a template for a recipe. The RecipeTemplate class outlines the general steps (prepare ingredients, cook, and serve), and specific recipes like PizzaRecipe and PancakeRecipe customize these steps as needed.
