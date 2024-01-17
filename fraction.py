class Phone:
    def __init__(self,price,brand, camera):
        print("Inside the phone constructor")
        self.price=price
        self.brand=brand
        self.camera=camera

    

class SmartPhone(Phone):
     
     def __init__(self,price,brand,camera,os,ram):
         print("this portion will execute first")
         super().__init__(price,brand,camera)
         self.os=os
         self.ram=ram
         print("inside smartphone constructor")


s=SmartPhone(17200,"REDMI Note 10S", 64, "Android",6) 

print(s.os,s.brand)


