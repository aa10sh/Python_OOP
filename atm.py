class Atm:
  def __init__(self): ## This is constructor, it will run as soon as we create an object of the class.
    self.user_balance=0
    self.user_name="xyz"
    self.user_pin="1234"

    self.homepage() # homepage method will automatically called as soon as we create an Atm object.

  def homepage(self):
     user_input=int(input("""
press 1 to Create account
press 2 to check balance
press 3 to deposit
press 4 to withdraw 
press 5 to change pin
press 6 to exit                          
Your response: """))

     if user_input==1:
       self.create_account()
     elif user_input==2:
       self.check_balance()
     elif user_input==3:
       self.deposit()
     elif user_input==4:
       self.withdraw()
     elif user_input==5:
       self.change_pin()  
     elif user_input==6:
       exit      
       
        
    

  def create_account(self): # Thses functions inside class are called methods.
    self.user_name=input("Enter User name: ")
    self.user_pin=int(input("Enter you pin: "))
    print("pin succesfully set")
    self.user_balance=int(input("Enter amount you want to deposit: "))
    see_balance=input("Do you want to see your balance? ")
    if(see_balance=="Yes"):
      self.check_balance()
    go_home=input("Do you want to move on Home page? ")
    if(go_home=="Yes"):
      self.homepage()
  
      


  def check_balance(self):
    print(self.user_name," is using checking balance...")
    pin=int(input("Enter your pin: "))
    if(pin==self.user_pin):
      print("Your Current Balance is:",self.user_balance)
    else:
      print("Invalid Pin")
    go_home=input("Do you want to move on Home page? ")
    if(go_home=="Yes"):
      self.homepage()  
        
  def deposit(self):
    print(self.user_name," is depositing money...")
    amount=int(input("Enter amount: "))
    self.user_balance+=amount
    print(amount," is added to your account")
    go_home=input("Do you want to move on Home page? ")
    if(go_home=="Yes"):
      self.homepage()

  def withdraw(self):
    print(self.user_name,"is withdrawing money...")
    amount=int(input("Enter amount: "))
    pin=int(input("Enter your pin: "))
    if(self.user_balance>=amount):
      self.user_balance-=amount 
    go_home=input("Do you want to move on Home page? ")
    if(go_home=="Yes"):
      self.homepage()

  def change_pin(self):
    print(self.user_name,"is changing pin...")
    old_pin=int(input("enter your old pin: "))
    if(old_pin==self.__user_pin):
      new_pin=int(input("Enter your new pin: "))
      self.__user_pin=new_pin
      print("Pin changed succesfully")
    go_home=input("Do you want to move on Home page? ")
    if(go_home=="Yes"):
      self.homepage()        



atm=Atm() # atm object is created in memory(stack) and the self variable of class will refer to that object in memory.
print(atm.check_balance) # This will print the address of the check_balance method in memory e.g. <__main__.Atm object at 0x000001F66CB38C20
atm.check_balance() # This way we can call particular methods using object.
