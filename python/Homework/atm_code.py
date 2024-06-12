# -*- coding: utf-8 -*-
"""ATM code.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xe0G9wKbuyv701BQkzxajCTPR_YIny3o
"""

class BankAccount:
    def __init__(self, pin):
        self.balance = 0
        self.pin = pin
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

    def verify_pin(self):
        for _ in range(3):
            entered_pin = input("Please enter your PIN: ")
            if entered_pin == self.pin:
                print("PIN verified successfully!")
                return True
            else:
                print("Incorrect PIN.")
        print("Your account is locked due to too many incorrect PIN entries.")
        return False

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance")

    def display(self):
        print("\n Net Available Balance =", self.balance)


if __name__ == "__main__":
    account_pin = "1234"
    account = BankAccount(pin=account_pin)

    if account.verify_pin():
        while True:
            print("\nChoose an option:")
            print("1. Deposit")
            print("2. Withdraw")

            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                account.deposit()
            elif choice == "2":
                account.withdraw()
            elif choice == "3":
                account.display()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")