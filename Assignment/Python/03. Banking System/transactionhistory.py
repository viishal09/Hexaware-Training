class TransactionHistory:
    transaction_history = []

    @staticmethod
    def add_transaction(transaction):
        TransactionHistory.transaction_history.append(transaction)

    @staticmethod
    def display_transaction_history():
        print("Transaction History:")
        for transaction in TransactionHistory.transaction_history:
            print(transaction)
