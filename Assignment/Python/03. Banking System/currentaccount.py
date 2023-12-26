from account import Account
from accountdao import AccountDAO

class CurrentAccount(Account, AccountDAO):
    overdraft_limit = 1000.0

    def __init__(self, account_number, balance, customer):
        super().__init__(account_number, "Current", balance, customer)

    def withdraw(self, amount):
        if amount > (self.balance + self.overdraft_limit):
            print("Insufficient funds and overdraft limit exceeded.")
        elif amount > self.balance:
            overdraft_used = amount - self.balance
            self.balance = 0
            self.overdraft_limit -= overdraft_used
            print(f"Withdrawal successful. Overdraft used: {overdraft_used}")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} from Current account successful.")
