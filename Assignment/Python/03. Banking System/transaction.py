from datetime import datetime

class Transaction:
    def __init__(self, transaction_id, account_id, transaction_type, amount, transaction_date):
        self.transaction_id = transaction_id
        self.account_id = account_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.transaction_date = transaction_date

    def __str__(self):
        formatted_date = datetime.strftime(self.transaction_date, "%Y-%m-%d")
        return f"Transaction ID: {self.transaction_id}, " \
               f"Account ID: {self.account_id}, " \
               f"Transaction Type: {self.transaction_type}, " \
               f"Amount: {self.amount}, " \
               f"Transaction Date: {formatted_date}"