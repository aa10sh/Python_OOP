                      ## Imlementing getter and setter method ##

class Atm:
    def __init__(self):
        self.__user_balance = 0
        self.user_name = "xyz"
        self.__user_pin = 1234

        self.homepage()

## Getter methods: A method used to access (read) the value of a private variable safely.
    def get_balance(self):
        return self.__user_balance

    def get_pin(self):
        return self.__user_pin

## Setter method: A method used to modify (update) the value of a private variable with control (often with validation).
    def set_pin(self, new_pin):
        if len(str(new_pin)) == 4:
            self.__user_pin = new_pin
            print("PIN updated successfully")
        else:
            print("PIN must be 4 digits")

    def homepage(self):
        user_input = int(input("""
press 2 to check balance
press 5 to change pin
press 6 to exit                          
Your response: """))

        if user_input == 2:
            self.check_balance()
        elif user_input == 5:
            self.change_pin()
        elif user_input == 6:
            exit

    def check_balance(self):
        print(self.user_name, "is checking balance...")
        pin = int(input("Enter your pin: "))
        if pin == self.__user_pin:
            print("Your Current Balance is:", self.get_balance()) ## use getter
        else:
            print("Invalid Pin")

        if input("Go to homepage? Yes/No: ") == "Yes":
            self.homepage()

    def change_pin(self):
        print(self.user_name, "is changing pin...")
        old_pin = int(input("Enter old pin: "))

        if old_pin == self.__user_pin:
            new_pin = int(input("Enter new pin: "))
            self.set_pin(new_pin)  ## use setter
        else:
            print("Invalid old PIN")

        if input("Go to homepage? Yes/No: ") == "Yes":
            self.homepage()

sbi=Atm()
