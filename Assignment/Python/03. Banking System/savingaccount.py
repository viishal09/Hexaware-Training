from account import Account

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate, customer):
        super().__init__(account_number, "Savings", balance, customer)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest_amount = (self.balance * self.interest_rate) / 100
        self.deposit(interest_amount)
        print(f"Interest of {interest_amount} added to the Savings account.")
