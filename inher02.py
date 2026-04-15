## ________________________________________________________________________________________________##

class Car:
    def __init__(self, name, year ):
        print("inside car class")
        self.name=name
        self.year=year

class Tata(Car):    ## Since Tata class have no constructor, 
            pass    ## it will automatically call the constructor of car class and pass the argument to Parent class

c1=Tata("Nexon", 2025)  ## inside car class

##____________________________________________________________________________________________________##

# class Phone:
#        def __init__(self,price, brand, camera):
#               print("Inside the Phone Constructor")
#               self.price=price
#               self.brand=brand
#               self.camera=camera

#        def buy(self):
#               print("Buying a Phone")
                    

# class Smartphone(Phone):
#        def buy(self):
#               print("Buying a Smartphone")


# S1=Smartphone(18000,"Nothing","100mpx")  ## Inside the Phone Constructor
# S1.buy()                                 ## Buying a Smartphone
# ## Method Overriding:(Polymorphism)
 
