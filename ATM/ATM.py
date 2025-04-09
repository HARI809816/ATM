class ATM:
    with open("pass.txt", "r") as file:
        pin = int(file.read()) #default pin is 1234
    
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Withdrawal amount exceeds balance or is not positive.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")
    
    def change_pin(self, new_pin):
        self.pin = new_pin
        with open("pass.txt", "w") as file:
            file.write(str(new_pin))
        print("Pin changed successfully.")

user1=ATM(10000)
print("======Welcome to ATM======")

get_pin=int(input(" Enter your pin: "))
if get_pin==ATM.pin:
    while True:
        print("==============================")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check balance")
        print("4. Change pin")
        print("5. Exit")
        print()
        ch=int(input("Enter your Choice : "))
        print("==============================")

        if ch==1:
            amount=int(input("Enter the amount to deposit: "))
            user1.deposit(amount)
        elif ch==2:
            amount=int(input("Enter the amount to withdraw: "))
            user1.withdraw(amount)
        elif ch==3:
            user1.check_balance()
        elif ch==4:
            new_pin=int(input("Enter the new pin: "))
            if type(new_pin)==int and len(str(new_pin))==4:
                user1.change_pin(new_pin)
            else:
                print("pin must be in  number or 4 digits")
        elif ch==5:
            print("Thank you for using ATM")
            break


else:
    print("the pin is invalid")