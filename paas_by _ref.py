                  ### Python objects could be pass by reference
class Customer:
    def __init__(self, name, gender):
        self.name=name
        self.gender=gender

def greet(customer):
    # if(customer.gender=="male"):
    #     print("hello sir!!")
    # else:
    #     print("Hello Ma'am")
    print(id(customer)) 



# Adarsh=Customer("Adarsh","male")
# greet(Adarsh)
# print(id(Adarsh))    ## address : 2236921777520 which is same as address of customer argument in greet function.
## And if both of them are are pointing to same address, any change made with customer object inside the
## greet function will reflect in Adarsh object as well.

## Lets see with example:
class Vehicle:
    def __init__(self,name, year):
        self.name=name
        self.year=year

def change_car(car):
    print("Car name before:",car.name)
    car.name="XUV"
    print("address car argument: ",id(car))  ## address car argument:  1402855066656

car=Customer("Nexon",2025)
change_car(car)                               
print("address of car object is: ",id(car))  ## address of car object is:  1402855066656
print("Car name later:",car.name)  ## XUV ## the name of car is changed 

## Important concept:
## Class ke objects are mutable like list, dict and sets.
## Which means sending list in a function might cause changes in original List,
## so it's good pratice to clone it first a send the clone to the function.
## you can do so as:  function(List[:])   , it would send clone to the function.

## Tuples are the immutable data types
## Tuples are also passed by reference, but when function tries to change it,
## it creates a new copy of tuple at another address.


