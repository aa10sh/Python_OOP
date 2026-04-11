                        ### Implemented Encapsulation with covering how and why? ###

class Atm:
  def __init__(self):
    self.__user_balance=0 
    # now user_balance is private, you can't see it directly i.e. user will not know this data also exists
    # in this class
    # but user who knows that this data exist in this class could use it using " _Classname__data", e.g _Atm__user_balance
    ## known as Name Mangling in python.
    self.user_name="xyz"
    self.__user_pin=1234

    self.homepage()

  def homepage(self):
     user_input=int(input("""
press 2 to check balance
press 5 to change pin
press 6 to exit                          
Your response: """))

     
     if user_input==2:
       self.check_balance()
     elif user_input==5:
       self.change_pin()  
     elif user_input==6:
       exit      
       
      
  

  def check_balance(self):
    print(self.user_name," is using checking balance...")
    pin=int(input("Enter your pin: "))
    if(pin==self.__user_pin):
      print("Your Current Balance is:",self.__user_balance) 
      ## You can't fetch private data directly from outside,
      ## but you can use it using methods of class, this is called Encapsulation.
    else:
      print("Invalid Pin")
    go_home=input("Do you want to move on Home page? ")
    if(go_home=="Yes"):
      self.homepage()  
        
  ## Now you might think that if user can access private data using methods of class,
  ## then what is the use of making data private?
  ## The use of making data private is to control the access of data 
  ## i.e. you can add some constrains in methods to access
  ## the private data so that only authorized user can access that data.
  ## for e.g. in below method change_pin we added a condition that only user who knows
  ## the old pin can change the pin.

  def change_pin(self):
    print(self.user_name,"is changing pin...")
    old_pin=int(input("enter your old pin: "))
    if(old_pin==self.__user_pin): ## here we controlled the access of private data.
      new_pin=int(input("Enter your new pin: "))
      self.__user_pin=new_pin
      print("Pin changed succesfully")
    go_home=input("Do you want to move on Home page? ")
    if(go_home=="Yes"):
      self.homepage()        



atm=Atm()
# atm.__user_balance  
# ## This line will throw error because you can't directly access the private
# data of the class from outside,
# This concept is called Encapsulation
# To access private data of class you have to use following technique.
print(atm._Atm__user_balance)  # we can use private data and methods of class this way in python
print(atm._Atm__user_pin) # This technique is called Name Mangling.







