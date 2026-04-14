class Bank_user:
    Bank_name="SBI"
    counter=1 ## static variable
## Static variables are declared before the constructor and are shared among all the istances of the class.

    def __init__(self,name, balance):
        self.name=name ## Instance variable 
## Instance variables are declared inside the constructor and are unique to each instance of the class.        
        self.__balance=balance
        self.__sr_no=Bank_user.counter
        Bank_user.counter+=1

    def get_balance(self):
        return self.__balance
    

    def get_sr_no(self):
        return self.__sr_no
    
    @staticmethod
    def get_counter():
        return Bank_user.counter
    
    @staticmethod
    def set_counter(value):
        if type(value)==int and value>0:
         Bank_user.counter=value
        else:
            print("enter valid counter value") 

# Without @staticmethod:

# Python assumes it's an instance method
# Automatically passes self
# Causes argument mismatch error

# With @staticmethod:

# No automatic argument passing
# Works like a normal function inside class


        @classmethod  ## These methods takes class as the first argument and can access class variable and
        ## other class methods but cannot access instance variable and instance methods.
        def display_bank_name(cls):
            print("Bnak name is:", cls.Bank_name)

        @classmethod
        def set_bank_name(cls, name):
            if type(name)==str:
                cls.Bank_name=name
            else:
                print("Enter valid bank name:")        



      
Adarsh=Bank_user("Adarsh", 120000)
Riya=Bank_user("Riya", 100000)
Abhay=Bank_user("Abhay",900000)
print(Adarsh.get_sr_no()," ", Adarsh.name," ",Adarsh.get_balance()) ## 1   Adarsh   120000
print(Riya.get_sr_no()," ", Riya.name," ",Riya.get_balance())       ## 2   Riya   100000
print(Abhay.get_sr_no()," ", Abhay.name," ",Abhay.get_balance())    ## 3   Abhay   900000

Bank_user.set_counter(80)
print("Updated counter:", Bank_user.get_counter())                  ## Updated counter: 80
print(Adarsh.get_sr_no()," ", Adarsh.name," ",Adarsh.get_balance()) ## 1   Adarsh   120000

## Since counter is updated to 80, but sr_no of Adarsh is still 1 because 
## sr_no is instance variable and it is assigned the value of counter at the time of object creation.
## Further objects will have sr_no starting from 80, 81,82and so on.

Chatur=Bank_user("Chatur",700000)
Rancho=Bank_user("Rancho", 800000)
print(Chatur.get_sr_no()," ", Chatur.name," ",Chatur.get_balance())
print(Rancho.get_sr_no()," ", Rancho.name," ",Rancho.get_balance())


