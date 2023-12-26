class ATMService:
    @staticmethod
    def perform_transaction(current_balance, transaction_type, amount):
        if transaction_type == "Check Balance":
            print(f"Your current balance is: {current_balance}")
        elif transaction_type == "Withdraw":
            if amount > current_balance or amount % 100 != 0:
                print("Withdrawal failed. Invalid amount or insufficient balance.")
            else:
                current_balance -= amount
                print(f"Withdrawal successful. Remaining balance: {current_balance}")
        elif transaction_type == "Deposit":
            current_balance += amount
            print(f"Deposit successful. Updated balance: {current_balance}")
        else:
            print("Invalid transaction type. Please choose Check Balance, Withdraw, or Deposit.")
