class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -=amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print("Balance: $" + str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance * self.int_rate
            self.balance += interest
            return self

account1 = BankAccount(0.02, 1000)
account2 = BankAccount(0.05, 500)

account1.display_account_info()
account2.display_account_info()

account1.deposit(200)
account1.display_account_info()

account2.withdraw(100)
account2.display_account_info()

account1.yield_interest()
account1.display_account_info()

account2.yield_interest()
account2.display_account_info()

account1.deposit(100).deposit(200).deposit(300).withdraw(150).yield_interest().display_account_info()
