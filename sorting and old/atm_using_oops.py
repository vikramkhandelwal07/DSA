class Atm:
    
    # constructor 
    def __init__(self) :
        self.pin = ""
        self.balance = 0
        
        self.menu()
        
    def menu(self):
        user_input =input("""
                        hello , how would you like to procced further
                        1.enter 1 to create pin
                        2.enter 2 to deposit
                        3.enter 3 to withdraw
                        4.enter 4 to check balance
                        5.enter 5 to exit 
                          """)
        if user_input == "1":
            print("create pin")
            self.create_pin()
        elif user_input == "2":
            print("deposit")
            self.deposit()
        elif user_input == "3":
            print("withdraw")
            self.withdraw()
        elif user_input == "4":
            print("check balance")
            self.check_balance()
        else:
            print("exit")
            
    def create_pin(self):
        self.pin = input("enter your pin")
        print("print set successfully")
        
    def deposit(self):
        temp = input("enter your pin")
        if temp == self.pin:
            
            amount= int(input("enter the amount to be deposited "))
            self.balance = self.balance + amount
            print("deposit successful")
        else:
            print("wrong pin , please enter correct pin")
            
    def withdraw(self):
        temp = input("enter your pin")
        if temp == self.pin:
            amount= int(input("enter the amount to be deposited "))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("successful operation")
            else:
                print("insufficient balance")
        else:
            print("wrong pin , please enter correct pin")
    
    def check_balance(self):
        temp = input("enter your pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("inavalid pin")