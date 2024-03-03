# Model-View-Controller (MVC) Pattern

1. What is it?

   The Model-View-Controller (MVC) pattern is a way of organizing code in a software application. It divides the code into three main parts: Model, View, and Controller.

2. What is its purpose?

   Model: Manages data and business logic.
   View: Displays information to the user.
   Controller: Handles user input and updates the Model and View accordingly.
   The purpose is to keep different parts of the code separate, making it easier to understand, maintain, and update.

3. When to use this?

   Use MVC when you want a clear structure in your code, especially for applications with a user interface. It helps in creating flexible and organized software, making it easier to collaborate on large projects.

4. Small Code example

   Here's a simple Python example using a hypothetical game:

```python
# Model
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

# View
class PlayerView:
    def display_player_info(self, player):
        print(f"Player: {player.name}, Score: {player.score}")

# Controller
class GameController:
    def __init__(self, player, view):
        self.player = player
        self.view = view

    def update_score(self, new_score):
        self.player.score = new_score
        self.view.display_player_info(self.player)

# Example Usage
# Create instances
player = Player("Alice", 100)
view = PlayerView()
controller = GameController(player, view)

# Display initial info
view.display_player_info(player)

# Player scores change
controller.update_score(150)

```

In this example, the Player class is the Model, PlayerView is the View, and GameController is the Controller. They work together to manage the player's information and update the display.
