# Decorator Pattern

1. What is it?

   The decorator pattern is like adding a special wrapper or cover to something. In Python, it helps you add new features or change the behavior of functions or classes without changing their actual code.

2. What is its purpose?

   The purpose is to make your code more flexible and easy to update. Instead of changing the original code, you can wrap it with decorators to add new abilities or modify its behavior.

3. When to use this?

   Use the decorator pattern when you want to add extra features to your code without making big changes. It's handy when you have different options or variations but want to keep your code clean and organized.

4. Small Code Example

   ```python
   # Original function
   def greet(name):
       return f"Hello, {name}!"

   # Decorator function
   def shout_decorator(func):
       def wrapper(name):
           result = func(name)
           return result.upper() + "!!!"
       return wrapper

   # Using the decorator
   @shout_decorator
   def greet_with_shout(name):
       return f"Hello, {name}!"

   # Example usage
   normal_greeting = greet("Alice")
   decorated_greeting = greet_with_shout("Bob")

   print(normal_greeting)           # Output: Hello, Alice!
   print(decorated_greeting)        # Output: HELLO, BOB!!!
   ```

In this example, the `shout_decorator` is like a wrapper that adds the ability to shout to the original `greet` function. The `@shout_decorator` syntax is a cool way to use decorators in Python.
