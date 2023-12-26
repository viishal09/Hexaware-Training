from abc import ABC, abstractmethod
from customerservice import ICustomerServiceProvider

class IBankServiceProvider(ICustomerServiceProvider, ABC):
    @abstractmethod
    def create_account(self, customer, account_type, balance):
        pass

    @abstractmethod
    def list_accounts(self):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass