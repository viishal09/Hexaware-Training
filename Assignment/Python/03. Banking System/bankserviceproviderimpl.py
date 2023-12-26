from customerserviceproviderimpl import CustomerServiceProviderImpl
from bankservice import IBankServiceProvider
from exceptions import InsufficientFundException
from exceptions import InvalidAccountException
from exceptions import OverDraftLimitExceededException
from exceptions import NullPointerException

class BankServiceProviderImpl(CustomerServiceProviderImpl, IBankServiceProvider):
    def __init__(self, branch_name = None, branch_address = None):
        super().__init__()
        self.branch_name = branch_name
        self.branch_address = branch_address

    def create_account(self, customer, account_type, balance):
        account_number = len(self.accounts) + 1
        account = {
            'account_number': account_number,
            'customer': customer,
            'account_type': account_type,
            'balance': balance
        }
        self.accounts[account_number] = account
        return account

    def list_accounts(self):
        return list(self.accounts.values())

    def calculate_interest(self):
        for account_number, account in self.accounts.items():
            if account['account_type'] == 'Savings':
                interest_rate = 0.045
                interest_amount = account['balance'] * interest_rate
                self.deposit(account_number, interest_amount)
                print(f"Interest of {interest_amount} added to the account {account_number}.")

    def withdraw(self, account_number, amount):
        account = self.get_account_by_number(account_number)
        if account is not None:
            try:
                account.withdraw(amount)
            except InsufficientFundException as e:
                print(f"Withdrawal failed: {str(e)}")
            except OverDraftLimitExceededException as e:
                print(f"Withdrawal failed: {str(e)}")
            except NullPointerException as e:
                print(f"Withdrawal failed: {str(e)}")
            except Exception as e:
                print(f"Withdrawal failed: {str(e)}")
        else:
            raise InvalidAccountException("Account not found.")

    def get_account_by_number(self, account_number):
        for account in self.list_accounts():
            if account.account_number == account_number:
                return account
        return None