# We will build a real life project to understand oop better based on banking system 
class Atm:
    def __init__(self) :
        self.pin= ""
        self.balance=0
        self.menu()
        

    def menu(self):
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


          
                  

               
       