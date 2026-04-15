class Car:
    def __init__(self, name, year ):
        print("inside car class")
        self.name=name
        self.year=year

class Tata(Car):    ## Since Tata class have no constructor, 
            pass    ## it will automatically call the constructor of car class and pass the argument to Parent class

c1=Tata("Nexon", 2025)  ## inside car class

