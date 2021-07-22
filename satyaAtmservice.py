import datetime
import sys

s = datetime.datetime.now().strftime("%H:%M:%S")
print("\t\t\t\t\t\t welcome to Satya Atm")
print("\t\t\t\t\t\t please insert your card here\t\t\t\t\t", s)


class Tulasibank:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
        print("hello", self.name)

    def deposit(self, amount):
        self.balance = amount + self.balance
        print("your balance after deposit:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficient funds")
            sys.exit()
        self.balance = self.balance - amount
        print("your balance after withdrwa", self.balance)

    def exit(self):
        print("thanks for banking with us", self.name)
        sys.exit()

    def signup(self):
        a = int(input("enter your phone number"))
        print("an otp has sent to our moble number")

        b = int(input("enter the otp"))
        print("congratulations your account created successfully")


name = input("enter yourname:")

a = Tulasibank(name)
while True:
    print('d-deposit\t\tw-withdraw\t\te-exit\t\ts-signup')
    option = input("enter your option")
    if option == 'd' or option == 'D':
        amount = float(input("enter the amount"))
        a.deposit(amount)
    elif option == 'w' or option == 'W':
        amount = float(input("enter the amount you want to withdraw"))
        a.withdraw(amount)
    elif option == 'e' or option == 'E':
        a.exit()
    elif option == 's' or option == 'S':
        a.signup()
    else:
        print("enter valid option")


































