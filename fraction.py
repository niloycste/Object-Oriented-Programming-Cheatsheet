class Atm:

    __counter=1 # Static/Class varible

    def __init__(self) :
        self.__pin= ""  
        self.__balance=0
        self.serialno=Atm.__counter # to access static variable we write class name.static variable like Atm.counter
        Atm.__counter=Atm.__counter+1

#for static variable we dont need to use `self`. as we use this getter and setter method access the static variable so we dont need to use self 
    @staticmethod    
    def get_counter(): 
        return Atm.__counter


    def set_counter(new):
       if type(new)==int:
          Atm.__counter=new
       else:
          print("Not Allowed")      

        

   
    def get_pin(self):     
       return self.__pin

    def set_pin(self,new_pin):
       if type(new_pin)==str:
          
          self.__pin=new_pin
          print("print changed")
       else: 
          print("not allowed")      
        