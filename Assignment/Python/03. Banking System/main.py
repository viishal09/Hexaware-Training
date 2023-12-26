import datetime
import traceback
from datetime import datetime, date
from typing import List, Optional
from bankserviceproviderimpl import BankServiceProviderImpl
from customer import Customer
from loanservice import LoanService
from transaction import Transaction
from exceptions import LoanEligibilityException, InvalidAccountException, InsufficientFundException, CustomerNotFoundException
from atmservices import ATMService
from futurebalance import FutureBalance
from bankaccount import BankAccount
from passwordvalidator import PasswordValidator
from transactionhistory import TransactionHistory
from account import Account
from accountdao import AccountDAO
from savingaccount import SavingsAccount
from currentaccount import CurrentAccount
from dbconnect import DBConn
import mysql.connector as sql

#Task 1:
print("Task 1:")
try:
    credit_score = int(input("Enter credit score: "))
    annual_income = float(input("Enter annual income: "))

    customer = Customer(None,None,None,None,None,None,credit_score, annual_income)
    LoanService.check_loan_eligibility(customer)

    print("Congratulations! You are eligible for a loan.")

except ValueError:
    print("Invalid input. Please enter valid numeric values.")
except LoanEligibilityException as e:
    print(f"Loan eligibility check failed: {str(e)}")

#Task 2:
print("Task 2:")
try:
    current_balance = float(input("Enter current balance: "))
    transaction_type = input("Enter transaction type (Check Balance/Withdraw/Deposit): ").capitalize()
    amount = float(input("Enter amount: "))

    ATMService.perform_transaction(current_balance, transaction_type, amount)

except ValueError:
    print("Invalid input. Please enter valid numeric values.")

#Task3:
print("Task 3:")
try:
    num_customers = int(input("Enter the number of customers: "))
    for _ in range(num_customers):
        initial_balance = float(input("Enter initial balance: "))
        annual_interest_rate = float(input("Enter annual interest rate: "))
        years = int(input("Enter the number of years: "))

        future_balance = FutureBalance.calculate_future_balance(initial_balance, annual_interest_rate, years)
        print(f"Future balance after {years} years: {future_balance}")

except ValueError:
    print("Invalid input. Please enter valid numeric values.")

#Task4:
print("Task 4:")
try:
    while True:
        account_number = input("Enter your account number: ")
        if account_number in BankAccount.accounts:
            balance = BankAccount.get_account_balance(account_number)
            print(f"Account balance for account {account_number}: {balance}")
            break
        else:
            print("Invalid account number. Please try again.")

except ValueError:
    print("Invalid input. Please enter a valid account number.")

#Task5:
print("Task 5:")
try:
    password = input("Create a password for your bank account: ")
    PasswordValidator.validate_password(password)

except ValueError:
    print("Invalid input. Please enter a valid password.")

#Task6:
print("Task 6:")
try:
    while True:
        transaction = input("Enter a transaction (Type 'exit' to finish): ")
        if transaction.lower() == 'exit':
            break
        else:
            TransactionHistory.add_transaction(transaction)
    TransactionHistory.display_transaction_history()

except ValueError:
    print("Invalid input.")

#Task7:
print("Task 7:")
customer = Customer(1, "John", "Doe", "john.doe@email.com", "1234567890", "123 Main St",None,None)
account = Account("A123", "Savings", 1000.0, None)
print(customer)
print(account)

AccountDAO.deposit(account, 500)
AccountDAO.withdraw(account, 200)
AccountDAO.calculate_interest(account)
print(account)

#Task8:
print("Task 8:")
savings_account = SavingsAccount("SA001", 1500.0, 5.0, None)
current_account = CurrentAccount("CA001", 2000.0, None)

print(savings_account)
print(current_account)

savings_account.calculate_interest()
current_account.withdraw(2500)
print(savings_account)
print(current_account)

#Task9: Abstract done in python.
print("Task 9: Done in entity")

#Task10:
print("Task 10:")
class BankApp:
    customers = {}
    accounts = {}

    @staticmethod
    def main():
        while True:
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Get Account Details")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                BankApp.create_account()
            elif choice == "2":
                BankApp.deposit()
            elif choice == "3":
                BankApp.withdraw()
            elif choice == "4":
                BankApp.transfer()
            elif choice == "5":
                BankApp.get_account_details()
            elif choice == "6":
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def create_account():
        BankApp.customers = {
            '1': Customer('1', 'John', 'Doe', 'john.doe@email.com', '1234567890', '123 Main St', None, None),
        }
        customer_id = input("Enter Customer ID: ")

        # Check if the customer_id exists in the customers dictionary
        if customer_id in BankApp.customers:
            # Placeholder logic to create a new account
            account_type = input("Enter Account Type (Savings/Current): ")
            initial_balance = float(input("Enter Initial Balance: "))

            # Create a new account object and add it to the accounts mapping
            account = Account(customer_id, account_type, initial_balance, BankApp.customers[customer_id])
            BankApp.accounts[account.account_number] = account

            print(f"Account created successfully. Account Number: {account.account_number}")
        else:
            print(f"Customer with ID {customer_id} does not exist.")


    @staticmethod
    def deposit():
        account_number = int(input("Enter Account Number: "))
        amount = float(input("Enter Deposit Amount: "))
        if account_number in BankApp.accounts:
            account = BankApp.accounts[account_number]
            account.deposit(amount)
            print(f"Deposit of {amount} successful. Updated balance: {account.balance}")
        else:
            print("Invalid account number.")

    @staticmethod
    def withdraw():
        account_number = int(input("Enter Account Number: "))
        amount = float(input("Enter Withdrawal Amount: "))
        if account_number in BankApp.accounts:
            account = BankApp.accounts[account_number]
            account.withdraw(amount)
            print(f"Withdrawal of {amount} successful. Updated balance: {account.balance}")
        else:
            print("Invalid account number.")

    @staticmethod
    def transfer():
        from_account_number = int(input("Enter From Account Number: "))
        to_account_number = int(input("Enter To Account Number: "))
        amount = float(input("Enter Transfer Amount: "))
        if from_account_number in BankApp.accounts and to_account_number in BankApp.accounts:
            from_account = BankApp.accounts[from_account_number]
            to_account = BankApp.accounts[to_account_number]
            from_account.transfer(to_account, amount)
            print(f"Transfer of {amount} from {from_account_number} to {to_account_number} successful.")
            print(f"Updated balance for {from_account_number}: {from_account.balance}")
            print(f"Updated balance for {to_account_number}: {to_account.balance}")
        else:
            print("Invalid account number(s).")

    @staticmethod
    def get_account_details():
        account_number = int(input("Enter Account Number: "))
        if account_number in BankApp.accounts:
            account = BankApp.accounts[account_number]
            print(account)
        else:
            print("Invalid account number.")

if __name__ == "__main__":
    BankApp.main()

#Task11: Abstract done. Single inheritance done in savingaccount.py
print("Task 11:Done in entity and dao.")

#Task12:
print("Task 12: Completed in exceptions and bankserviceproviderimpl")
class BankAppp:
    bank_service = BankServiceProviderImpl("My Bank", "123 Main St")
    @staticmethod
    def main():
        while True:
            print("1. Create Account")
            print("2. List Accounts")
            print("3. Calculate Interest")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                BankAppp.create_account()
            elif choice == "2":
                BankAppp.list_accounts()
            elif choice == "3":
                BankAppp.calculate_interest()
            elif choice == "4":
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def create_account():
        customer = {'customer_id': 1, 'name': 'John Doe'}
        account_type = input("Enter Account Type (Savings/Current): ")
        initial_balance = float(input("Enter Initial Balance: "))
        BankAppp.bank_service.create_account(customer, account_type, initial_balance)
        print("Account created successfully.")

    @staticmethod
    def list_accounts():
        accounts = BankAppp.bank_service.list_accounts()
        for account in accounts:
            print(account)

    @staticmethod
    def calculate_interest():
        BankAppp.bank_service.calculate_interest()
        print("Interest calculated successfully.")


if __name__ == "__main__":
    BankAppp.main()
#Task12:Completed in exceptions and bankserviceproviderimpl
print("Task 13: Done in dao")

#Task14:
print("Task 14:")
class Banking:
    def __init__(self, db_connection):
        self.connection = db_connection
        self.service = BankServiceProviderImpl(db_connection)

    def create_account(self, acc_id: int, acc_type: str, balance: float, customer_id: int) -> None:
        try:
            # Check if the customer_id exists in the customers table
            customer_exists = self.check_customer_exists(customer_id)

            if not customer_exists:
                print("Customer with the specified ID does not exist.")
                return

            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO Accounts (account_id, account_type, balance, customer_id) VALUES (%s, %s, %s, %s)",
                (acc_id, acc_type, balance, customer_id))
            self.connection.commit()
            print("Account created successfully.")
        except sql.Error as e:
            raise e

    def check_customer_exists(self, customer_id: int) -> bool:
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM Customers WHERE customer_id = %s", (customer_id,))
        result = cursor.fetchone()
        return result[0] > 0

    def list_accounts(self) -> List[Account]:
        try:
            cursor = self.connection.cursor()

            # Check for invalid customer IDs in Accounts
            cursor.execute(
                "SELECT account_id FROM Accounts WHERE customer_id NOT IN (SELECT customer_id FROM Customers)")
            invalid_account_ids_data = cursor.fetchall()
            invalid_account_ids = [invalid_acc_data[0] for invalid_acc_data in invalid_account_ids_data]

            for invalid_acc_id in invalid_account_ids:
                print(f"Error processing account ID {invalid_acc_id}: Customer not found.")

            # Fetch all valid accounts
            cursor.execute("SELECT * FROM Accounts")
            accounts_data = cursor.fetchall()

            accounts = []
            for acc_data in accounts_data:
                # Set default values in case of exceptions
                customer = None
                balance = 0.0

                try:
                    # Fetch customer details
                    customer_id = int(acc_data[3])  # Convert to integer
                    customer = self.get_customer_details(customer_id)

                    # Convert balance to float if it's a valid float
                    balance = float(acc_data[2])

                    # Print "ID Found" for valid accounts
                    print(f"Error processing account ID {acc_data[0]}")
                except (ValueError, CustomerNotFoundException) as e:
                    print(f"ID Found {acc_data[0]}")

                # Create the Account object with customer details (even if customer is None)
                account = Account(acc_data[0], acc_data[1], balance, customer)
                accounts.append(account)

            return accounts
        except sql.Error as e:
            raise e

    def get_customer_details(self, customer_id: int) -> Optional[Customer]:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Customers WHERE customer_id = %s", (customer_id,))
            customer_data = cursor.fetchone()

            if customer_data:
                customer = Customer(customer_data[1], customer_data[2], customer_data[3])
                customer.customer_id = customer_data[0]
                return customer
            else:
                raise CustomerNotFoundException("")
        except sql.Error as e:
            raise e

    def get_account_balance(self, account_id: int) -> float:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT balance FROM Accounts WHERE account_id = %s", (account_id,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                raise InvalidAccountException("Account not found.")
        except sql.Error as e:
            raise e

    def deposit(self, account_id: int, amount: float) -> float:
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE Accounts SET balance = balance + %s WHERE account_id = %s", (amount, account_id))
            self.connection.commit()
            print(f"Amount deposited in account ID {account_id} successfully")
            return self.get_account_balance(account_id)
        except sql.Error as e:
            raise e

    def withdraw(self, account_id: int, amount: float) -> float:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT balance FROM Accounts WHERE account_id = %s", (account_id,))
            result = cursor.fetchone()
            if result:
                current_balance = result[0]
                if current_balance >= amount:
                    cursor.execute("UPDATE Accounts SET balance = balance - %s WHERE account_id = %s", (amount, account_id))
                    self.connection.commit()
                    print(f"Amount withdrawn from account ID {account_id} successfully")
                    return self.get_account_balance(account_id)
                else:
                    raise InsufficientFundException("Insufficient funds.")
            else:
                raise InvalidAccountException("Account not found.")
        except sql.Error as e:
            raise e

    def transfer(self, from_account_id: int, to_account_id: int, amount: float) -> None:
        try:
            self.withdraw(from_account_id, amount)
            self.deposit(to_account_id, amount)
        except (InsufficientFundException, InvalidAccountException) as e:
            raise e

    def get_account_details(self, account_id: int) -> Account:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Accounts WHERE account_id = %s", (account_id,))
            result = cursor.fetchone()
            if result:
                account = Account(result[1], result[2], result[3])
                account.account_id = result[0]
                return account
            else:
                raise InvalidAccountException("Account not found.")
        except sql.Error as e:
            print(f"SQL Error: {e}")
        except CustomerNotFoundException as e:
            print(f"Customer Not Found: {e}")
        except InvalidAccountException as e:
            print(f"Invalid Account: {e}")

    def get_transactions(self, account_id: int, from_date: date, to_date: date) -> List[Transaction]:
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "SELECT * FROM Transactions WHERE account_id = %s AND transaction_date BETWEEN %s AND %s",
                (account_id, from_date.strftime('%Y-%m-%d'), to_date.strftime('%Y-%m-%d'))
            )
            transactions_data = cursor.fetchall()

            transactions = []
            for trans_data in transactions_data:
                transaction = Transaction(trans_data[0], trans_data[1], trans_data[2], trans_data[3], trans_data[4])
                transactions.append(transaction)

            # Print the transactions
            for transaction in transactions:
                print(transaction)

            return transactions
        except MySQLError as e:
            print(f"Error: {e}")
            traceback.print_exc()
            raise e

    @staticmethod
    def main():
        while True:
            print("1. Create Account")
            print("2. List Accounts IDs")
            print("3. Get Account Balance")
            print("4. Deposit")
            print("5. Withdraw")
            print("6. Transfer")
            print("7. Get Account Details")
            print("8. Get Transactions")
            print("9. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                acc_id = int(input("Enter Account ID: "))
                customer_id = int(input("Enter Customer ID: "))
                acc_type = input("Enter Account Type: ")
                balance = float(input("Enter Balance: "))
                banks.create_account(acc_id, acc_type, balance, customer_id)
            elif choice == "2":
                banks.list_accounts()
            elif choice == "3":
                try:
                    acc_id = int(input("Enter Account ID: "))
                    balance = banks.get_account_balance(acc_id)
                    print(f"Account balance for ID {acc_id}: {balance}")
                except ValueError:
                    print("Invalid input. Please enter a valid account ID.")
                except InvalidAccountException as e:
                    print(f"Error: {str(e)}")
            elif choice == "4":
                acc_id = int(input("Enter Account ID: "))
                amount = float(input("Enter Deposit Amount: "))
                banks.deposit(acc_id, amount)
            elif choice == "5":
                acc_id = int(input("Enter Account ID: "))
                amount = float(input("Enter Withdrawal Amount: "))
                banks.withdraw(acc_id, amount)
            elif choice == "6":
                from_acc_id = int(input("Enter From Account ID: "))
                to_acc_id = int(input("Enter To Account ID: "))
                amount = float(input("Enter Transfer Amount: "))
                banks.transfer(from_acc_id, to_acc_id, amount)
            elif choice == "7":
                acc_id = int(input("Enter Account ID: "))
                try:
                    account = banks.get_account_details(acc_id)
                    print(f"Account Details: {account}")
                except (InvalidAccountException, CustomerNotFoundException) as e:
                    print(f"Error: {str(e)}")
            elif choice == "8":
                acc_id = int(input("Enter Account ID: "))
                from_date_str = input("Enter From Date (YYYY-MM-DD): ")
                to_date_str = input("Enter To Date (YYYY-MM-DD): ")

                # Convert input date strings to date objects
                from_date = datetime.strptime(from_date_str, "%Y-%m-%d").date()
                to_date = datetime.strptime(to_date_str, "%Y-%m-%d").date()

                banks.get_transactions(acc_id, from_date, to_date)
            elif choice == "9":
                print("Exiting the application.")
                break
            else:
                print("Invalid choice. Please try again.")

db_connection = DBConn.get_connection()
banks = Banking(db_connection)
banks.main()

