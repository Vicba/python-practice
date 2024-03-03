# Factory Pattern

1. What is it?

   The Factory Pattern is like a recipe for making things. Imagine you want to bake cookies, and you have a cookie factory that follows the recipe to make different types of cookies.

2. What is its purpose?

   The purpose is to create objects (like cookies) without knowing the exact details of how each object is made. It's like ordering a pizza without needing to know how the pizza chef prepares each topping.

3. When to use this?

   Use the Factory Pattern when you want to create different types of objects, but you don't want to worry about how each object is made. It's handy when you need flexibility and want to hide the complicated creation process.

4. Small Code Example:

   ```python
   class Cookie:
       def bake(self):
           pass

   class ChocolateCookie(Cookie):
       def bake(self):
           return "Baking a chocolate cookie!"

   class VanillaCookie(Cookie):
       def bake(self):
           return "Baking a vanilla cookie!"

   class CookieFactory:
       def create_cookie(self, cookie_type):
           if cookie_type == "chocolate":
               return ChocolateCookie()
           elif cookie_type == "vanilla":
               return VanillaCookie()
           else:
               raise ValueError("Invalid cookie type")

   # Using the Factory
   factory = CookieFactory()
   my_cookie = factory.create_cookie("chocolate")
   print(my_cookie.bake())  # Output: Baking a chocolate cookie!
   ```

   This example shows a `CookieFactory` that can create different types of cookies (like chocolate or vanilla) without worrying about the details of how each cookie is baked.
