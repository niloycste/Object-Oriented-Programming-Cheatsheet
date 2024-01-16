# OOP-Cheatsheet
## Core Concept of OOP
Lets talk about what is  `OOP` in a layman language.

Imagine you're building a virtual world, like a video game or a simulation. In this world, everything can be thought of as objects. Objects are like characters or things that have characteristics (attributes) and can do things (methods).

**Class:** Class is a blueprint like how an object will behave.

**Objects:** These are the main entities in your virtual world. For example, if you're creating a game, an object could be a player, an enemy, or a weapon.

**Attributes:** These are the characteristics or properties of the objects. For a player object, attributes might include the player's name, health, and score.

**Methods:** These are the actions or behaviors that objects can perform. In a game, a player object might have methods like "move," "attack," or "collect items."

**Encapsulation:** This is like putting things in a box. It means that an object keeps its attributes and methods together, and the outside world doesn't need to know all the details. For example, when you play a game, you don't need to know how the player's health is calculated; you just see the current health value.

**Inheritance:** This is like passing down traits in a family. One object can inherit attributes and methods from another object. For instance, if you have a general "character" object, a "player" object could inherit from it and add specific player-related features.

**Polymorphism:** This is like using the same word in different contexts. It allows different objects to be treated as instances of the same type. For example, both a player and an enemy might have a "damage" method, but they would behave differently.<br/>
<img src = "images/oop concept.jpg" width="1200" height="400">

## Break Down Each of the concepts with code and example 
### Function vs Method: 
**Functions:** A function is a block of code that performs a specific task. It is defined outside of any class or object.

**Usage:** Functions are standalone and can be called from anywhere in the code, as long as they are in the same scope or imported.

**Example:** 
```python
    def add_numbers(a, b):
        return a + b

    result = add_numbers(5, 7)
    ```
