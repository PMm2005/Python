from bankaccount import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"{self.name}'s account balance:")
        self.account.display_account_info()
        return self

    def yield_interest(self):
        self.account.yield_interest()
        return self

user = User("John Doe", "john@example.com")
user.make_deposit(500).display_user_balance().make_withdrawal(200).display_user_balance().yield_interest().display_user_balance()

