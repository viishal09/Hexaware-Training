from typing import List
import mysql.connector as sql
from ibankrepository import IBankRepository
from customer import Customer
from account import Account


class BankRepositoryImpl(IBankRepository):
    def __init__(self, db_connection):
        self.connection = db_connection

    def create_account(self, customer: Customer, acc_no: int, acc_type: str, balance: float) -> None:
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO Account (account_number, account_type, balance, customer_id) VALUES (%s, %s, %s, %s)",
                           (acc_no, acc_type, balance, customer.customer_id))
            self.connection.commit()
        except sql.Error as e:
            raise e

    def list_accounts(self) -> List[Account]:
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Account")
            accounts_data = cursor.fetchall()

            accounts = []
            for acc_data in accounts_data:
                account = Account(acc_data[1], acc_data[2], acc_data[3])
                account.account_number = acc_data[0]
                accounts.append(account)

            return accounts
        except sql.Error as e:
            raise e