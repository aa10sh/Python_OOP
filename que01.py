##______________________Question 01__________________________##

class Parent:
    def __init__(self,num):
        self.__num=num

    def get_num(self):
        return self.__num

class Child(Parent):
    def __init__(self,val,num):
        self.__val=val

    def get_val(self):
        return self.__val

C1=Child(10,100)              
# print(C1.get_val())    ## 10
# print(C1.get_num())    ## AttributeError: 'Child' object has no attribute '_Parent__num'
## this error since child class has its own constructor , it is not calling the parent class constructor 
## which means the parent class variable is not getting initialized and hence we are getting this error.


##____________________________Question 02____________________##

class A:
    def __init__(self):
        self.val1=100

    def display1(self,val1):
        print(self.val1) ## Output= 100 not 200
      

class B(A):
    def display2(self, val1):
        print("Inside class B",self.val1)

# obj=B()
# obj.display1(200)

##_________________________Question 03_______________________##

class Parent:
    def __init__(self, val1,val2):
        self.val1=val1
        self.val2=val2
        print("Inside Parent constructor")

    def display(self): ## Ye self kiska hai?   Even though the method belongs to Parent:
        print(self.val1," ", self.val2)       ## The object is still of type Child
        print("display method inside Parent class")

class Child(Parent):
    def __init__(self,val1, val2):
        self.val1=val1
        self.val2=val2
        print("inside Child constructor")


    def display(self):
        print("display method inside Child class")
        print("value in child class:",self.val1," ",self.val2)
        super().display()  ## self of Child class is passed to the display method of Parent class

## Important point:
## Super keyword doesn't work outside the class 
## Also you can only access constructors and the methods of the parent class using super keyword,
## you cannot access the variables of the parent class using super kywords.

# C1=Child(55,77)
# C1.display()

## Output:
## inside Child constructor
##display method inside Child class
##value in child class: 55   77
##55   77
##display method inside Parent class

##__________________________Question 04_______________________##

class Phone:
    def __init__(self,price, brand, camera):
        print("Inside phone constructor")
        self.price=price
        self.brand=brand
        self.camera=camera


class Smartphone(Phone):
    def __init__(self, price, brand, camera, ram, memory):
        print("Before calling super constructor")
        super().__init__(price, brand, camera) ## If we have some common attributes in both Parent and child class  
        print("Inside smartphone constructor") ## we can pass these arguments to the Parent class constructor explicitly using super keyword.
        self.ram=ram
        self.memory=memory

S1=Smartphone(20000,"Samsung",48, 4, 64)
print(S1.brand)
print(S1.ram)

## Output:
## Before calling super constructor
## Inside phone constructor
## Inside smartphone constructor
## Samsung
## 4

##____________________________Question 05_________________________##

