class FutureBalance:
    @staticmethod
    def calculate_future_balance(initial_balance, annual_interest_rate, years):
        future_balance = initial_balance * (1 + annual_interest_rate / 100) ** years
        return future_balance
