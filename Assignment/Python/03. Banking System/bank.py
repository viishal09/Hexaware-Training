from account import Account


class Bank:
    accounts = []

    @classmethod
    def create_account(cls, customer, acc_type, balance):
        account = Account(acc_type, balance, customer)
        cls.accounts.append(account)
        return account

    @classmethod
    def get_account_balance(cls, account_number):
        for account in cls.accounts:
            if account.account_number == account_number:
                return account.balance
        return None

    @classmethod
    def deposit(cls, account_number, amount):
        for account in cls.accounts:
            if account.account_number == account_number:
                account.balance += amount
                return account.balance
        return None

    @classmethod
    def withdraw(cls, account_number, amount):
        for account in cls.accounts:
            if account.account_number == account_number:
                if account.balance >= amount:
                    account.balance -= amount
                    return account.balance
                else:
                    return "Insufficient balance."
        return None

    @classmethod
    def transfer(cls, from_account_number, to_account_number, amount):
        from_account = cls.get_account(from_account_number)
        to_account = cls.get_account(to_account_number)

        if from_account and to_account:
            if from_account.balance >= amount:
                from_account.balance -= amount
                to_account.balance += amount
                return from_account.balance
            else:
                return "Insufficient funds for transfer."
        return None

    @classmethod
    def get_account_details(cls, account_number):
        account = cls.get_account(account_number)
        if account:
            return str(account)
        return None

    @classmethod
    def get_account(cls, account_number):
        for account in cls.accounts:
            if account.account_number == account_number:
                return account
        return None
