
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn successfully")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: {self.balance}")


acc1 = BankAccount("Biswajit", 1000)

acc1.show_balance()
acc1.deposit(500)
acc1.withdraw(300)
acc1.show_balance()