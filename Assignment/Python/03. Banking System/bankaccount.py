class BankAccount:
    accounts = {
        '123': 1000.0,
        '456': 5000.0,
        '789': 200.0
    }

    @staticmethod
    def get_account_balance(account_number):
        return BankAccount.accounts.get(account_number)
