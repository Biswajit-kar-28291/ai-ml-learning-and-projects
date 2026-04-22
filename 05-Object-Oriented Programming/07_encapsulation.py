class Bank:
    def __init__(self):
        self.__balance = 1000

    def show_balance(self):
        print("Balance:", self.__balance)

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")


b = Bank()
b.show_balance()
b.deposit(500)
b.withdraw(300)
b.show_balance()