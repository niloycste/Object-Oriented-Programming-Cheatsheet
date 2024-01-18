from abc import ABC,abstractmethod
class BankApp(ABC):


    def database(self):
        print("connected to database")

    @abstractmethod    
    def security(self):
        pass
    

class MobileApp(BankApp):
    def mobile_login(self):
        print("login into mobile")

    def security(self):
        print("mobile security") # we must make security method in this class which is abstract method of its parent class `BankApp`, otherwise we can't inherit.
mob=MobileApp()
mob.security()
mob.mobile_login()        
