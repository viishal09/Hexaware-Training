from accountdao import AccountDAO

class Account:
    last_account_number = int(1000)

    def __init__(self, ls_account_number, account_type, balance, customer = None):
        Account.last_account_number += 1
        self._account_number = Account.last_account_number
        self._account_type = account_type
        self._balance = int(balance)
        self._customer = customer
        self._account_dao = AccountDAO()

    @property
    def account_number(self):
        return self._account_number

    @property
    def account_type(self):
        return self._account_type

    @property
    def balance(self):
        return self._balance

    @property
    def customer(self):
        return self._customer

    @balance.setter
    def balance(self, value):
        self._balance = value

    @customer.setter
    def customer(self, value):
        self._customer = value

    def deposit(self, amount):
        self._account_dao.deposit(self, amount)

    def withdraw(self, amount):
        self._account_dao.withdraw(self, amount)

    def transfer(self, to_account, amount):
        if amount > self._balance:
            print("Insufficient funds.")
        else:
            self._balance -= amount
            to_account.balance += amount
            print(f"Transfer of {amount} to {to_account.account_number} successful.")


    def __str__(self):
        return f"Account Number: {self._account_number}\n" \
               f"Account Type: {self._account_type}\n" \
               f"Balance: {self._balance}\n" \
               f"Customer: {self._customer}"
