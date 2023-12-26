class AccountDAO:
    @staticmethod
    def deposit(account, amount):
        account.balance += int(amount)

    @staticmethod
    def withdraw(account, amount):
        if account.balance >= amount:
            account.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    @staticmethod
    def calculate_interest(account):
        if account.account_type == "Savings":
            interest_rate = 0.045
            interest_amount = account.balance * interest_rate
            AccountDAO.deposit(account, interest_amount)
            print(f"Interest of {interest_amount} added to the account.")