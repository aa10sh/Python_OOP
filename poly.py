## Method Overriding(Polymorphism)

class Phone:
       def __init__(self,price, brand, camera):
              print("Inside the Phone Constructor")
              self.price=price
              self.brand=brand
              self.camera=camera

       def buy(self):
              print("Buying a Phone")
                    

class Smartphone(Phone):
       def buy(self):
              print("Buying a Smartphone")


S1=Smartphone(18000,"Nothing","100mpx")  ## Inside the Phone Constructor
S1.buy()                                 ## Buying a Smartphone
## Method Overriding:(Polymorphism)