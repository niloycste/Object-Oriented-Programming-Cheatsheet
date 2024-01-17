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
## Functions

- **Definition:** A function is a standalone block of code that performs a specific task. It is defined outside of any class or object.

- **Usage:** Functions can be called from anywhere in the code, as long as they are in the same scope or imported.

- **Example:**

    ```python
    def add_numbers(a, b):
        return a + b

    result = add_numbers(5, 7)
    ```

## Methods

- **Definition:** A method is a function associated with an object. It is defined within a class and is called on instances of that class.

- **Usage:** Methods are called on objects and operate on the data within those objects.

- **Example:**

    ```python
    class Calculator:
        def add_numbers(self, a, b):
            return a + b

    calc = Calculator()
    result = calc.add_numbers(5, 7)
    ```
- **Short Note:** lets we have a list l and we want to find out length of this list.so we will write len(l) , but if we append something in a list we will write l.append(). cause len is a function and append, copy, pop,remove etc are a method of a list class.    

## Constructor

A constructor is like a setup wizard for objects in programming. It's a special method, often named `__init__`, that runs automatically when  create an object. Its main job is to initialize the object's attributes or perform any necessary setup.
In Python:

```python
class MyClass  
    def __init__(self, initial_pin, initial_balance): 
    # this is constructor
     self.pin = initial_pin # instance variable 
    #  we call it instance variable cause we write it within the constructor and value will be different for each object 
     self.balance = initial_balance # instance variable
    
my_object = MyClass("1234", 1000)

```
- **Short Note:** 
- we usually write any sort of configuration related task in the constructor like database connectivity, hardware connectivity etc.
so basically we dont want to give specific control to the user and that time we will use constructor.<br/>

- Inside Class only two things are possible one is data and other one is method. Only object of this class can access that data and method even one method can't access another method and its datas within the class. if one method is trying to access another method we need and object and as `self` is the current object so we can access if we use self and thats why we use `self`.

## Simple Implementation based on `class`,`constructor`,`method` and `object`
 Now let's write a code  to understand oop better based on atm system 

 ```python 
  class Atm:
    def __init__(self) : 
        # Constructor
        self.pin= ""
        self.balance=0 
        self.menu() #we can access menu method property cause we use self
        

    def menu(self):
        # method
        user_input= input(""" 
                         Hello, How would you like to proceed
                          1.Enter 1 to create pin
                          2.Enter 2 to deposit
                          3.Enter 3 to Withdraw
                          4.Enter 4 to check balance
                          5.Enter 5 to exit

                         """)
        if user_input=="1":
         self.create_pin()
        elif user_input=="2":
           self.deposit()
        elif user_input=="3":
           self.withdraw()
        elif user_input=="4":
           self.check_balance() 
        else:
           print("Bye")          
        
    # methods
    def create_pin(self):
       self.pin=input("Enter your pin : ")
       print("Pin set sucessfully")

    def deposit(self):
       temp=input("Enter your pin : ")
       if temp==self.pin:
          amount=int(input("Enter the amount : "))
          self.balance=self.balance+amount
          print("Deposit Sucessfully")
       else:
          print("Invalid pin")   

    def withdraw(self):
       temp=input("Enter your pin : ")
       if temp==self.pin:
          amount=int(input("Enter the amount : "))
          if amount<self.balance:
             self.balance=self.balance-amount
             print("operation sucessfull")
          else:
             print("Insufficient Funds") 
       else:
          print("Invalid Pin : ")  
          
    def check_balance(self):
       temp=input("Enter your pin : ")
       if temp==self.pin:
          print(self.balance)
       else:
          print("invalid pin")  
# Object creation name bank based on the class Atm
  bank=Atm()
 ```

 ### Encapsulation
 Usually object can access everything like datas and methods so anyone can change the data so good practise is to hide the data.In pyhton we use `__` to hide the data and method. but fun fact is in python nothing is truely private. anyone can access the private data using class name and that data_name. lets give an example. lets we have a class name `Atm` and private data name `__balance` and object name `value`. now we can access that private data using `value._Atm__balance`. whatever in conventional method we use `getter` and `setter` emthod to access the data.
 Let's implement the encapsulation concept on our previous code.
 ```python
 
  # We will build a real life project to understand oop better based on banking system 
class Atm:
    def __init__(self) :
        self.__pin= ""  # hide the data using `__` so that user can't see that data
        self.__balance=0
        self.__menu()

     # we use getter and setter method to access the private data
    def get_pin(self):     
       return self.__pin

    def set_pin(self,new_pin):
       if type(new_pin)==str:
          
          self.__pin=new_pin
          print("print changed")
       else: 
          print("not allowed")      
        

    def __menu(self):  # we can also hide the method also 
        user_input= input(""" 
                         Hello, How would you like to proceed
                          1.Enter 1 to create pin
                          2.Enter 2 to deposit
                          3.Enter 3 to Withdraw
                          4.Enter 4 to check balance
                          5.Enter 5 to exit

                         """)
        if user_input=="1":
         self.create_pin()
        elif user_input=="2":
           self.deposit()
        elif user_input=="3":
           self.withdraw()
        elif user_input=="4":
           self.check_balance() 
        else:
           print("Bye")          
        

    def create_pin(self):
       self.__pin=input("Enter your pin : ")
       print("Pin set sucessfully")

    def deposit(self):
       temp=input("Enter your pin : ")
       if temp==self.__pin:
          amount=int(input("Enter the amount : "))
          self.__balance=self.__balance+amount
          print("Deposit Sucessfully")
       else:
          print("Invalid pin")   

    def withdraw(self):
       temp=input("Enter your pin : ")
       if temp==self.__pin:
          amount=int(input("Enter the amount : "))
          if amount<self.__balance:
             self.__balance=self.__balance-amount
             print("operation sucessfull")
          else:
             print("Insufficient Funds") 
       else:
          print("Invalid Pin : ")  
          
    def check_balance(self):
       temp=input("Enter your pin : ")
       if temp==self.__pin:
          print(self.__balance)
       else:
          print("invalid pin")  


 ```      




      
