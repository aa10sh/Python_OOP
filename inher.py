      ## Inheritance in python allows the child class to inherit the data and methods from the parent class.
      ##  but it's reverse is not true i.e. parent class cannot access the data and methods of child class.



class User: ## This is the parent class

    def __init__(self,year,location):
        self.year=year
        self.__location=location  ## Private data and methods are not inherited to the child class 
    
    def login(self):
        print("Login")

    def register(self):
        print("Register")

class Student(User): ## This is the child class which inherits from the parent class User
        
    def enroll(self):
        print("Enroll")

    def review(self):
        print("Review")   

Adarsh=Student(3,"Delhi")
Adarsh.login()         ## Login
Adarsh.register()      ## Register
Adarsh.enroll()        ## Enroll
Adarsh.review() 

print(Adarsh.year)
print(Adarsh._User__location) ## Delhi(name mangling)
print(Adarsh.__location)     ## AttributeError: 'Student' object has no attribute '__location'
                           ## as location is private data of User class it can't access directly.


Adam=User(3,"UP")
Adam.login()
Adam.register()
# Adam.enroll()     ## 'User' object has no attribute 'enroll
# Adam.review()     ## same...