from customerservice import ICustomerServiceProvider
class CustomerServiceProviderImpl(ICustomerServiceProvider):
    def __init__(self):
        # Assuming you have some data structure to store account details
        self.accounts = {}

    def get_account_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]['balance']
        else:
            return None

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            return self.accounts[account_number]['balance']
        else:
            return None

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number]['balance'] >= amount:
                self.accounts[account_number]['balance'] -= amount
                return self.accounts[account_number]['balance']
            else:
                print("Insufficient balance.")
                return None
        else:
            return None

    def transfer(self, from_account_number, to_account_number, amount):
        if from_account_number in self.accounts and to_account_number in self.accounts:
            if self.accounts[from_account_number]['balance'] >= amount:
                self.accounts[from_account_number]['balance'] -= amount
                self.accounts[to_account_number]['balance'] += amount
                return self.accounts[from_account_number]['balance']
            else:
                print("Insufficient balance.")
                return None
        else:
            return None

    def get_account_details(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            return None
