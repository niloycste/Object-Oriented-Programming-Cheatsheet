# Base class representing a general character
class Character:
    def __init__(self, name):
        # Attribute: Name of the character
        self.name = name

    # Method: Display information about the character
    def display_info(self):
        print(f"Character: {self.name}")

# Derived class representing a player, inheriting from Character
class Player(Character):
    def __init__(self, name, health, score):
        # Call the constructor of the base class
        super().__init__(name)
        
        # Player-specific attributes
        # Attribute: Health of the player
        self.health = health
        # Attribute: Score of the player
        self.score = score

    # Method: Move action
    def move(self):
        print(f"{self.name} is moving.")

    # Method: Attack action
    def attack(self):
        print(f"{self.name} is attacking.")

    # Method: Collect items action
    def collect_items(self):
        print(f"{self.name} is collecting items.")

# Creating instances (objects) of the Player class
player1 = Player("Player 1", 100, 0)
player2 = Player("Player 2", 80, 50)

# Accessing attributes and calling methods
# Object: Displaying information about the character (inherited method)
player1.display_info()

# Object: Player 1 performing specific actions
player1.move()
player1.attack()

# Object: Displaying information about the character (inherited method)
player2.display_info()

# Object: Player 2 performing a specific action
player2.collect_items()
