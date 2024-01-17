class Phone:
    def __init__(self,price,brand, camera):
        print("Inside the constructor")
        self.price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):


    def buy(self):
        print("Buying smartphone")

s=SmartPhone(17200,"REDMI Note 10S", 64) # Phone class constructor will be called as SmartPhone doesn't have constructor
print(s.price,s.brand,s.camera)

s.buy() # SmartPhone method buy will be called not Phone class method cause we create an object of SmartPhone. 


