class InsufficientBalanceError(Exception):
    pass

class DatabaseConnectionError(Exception):
    pass

class LoanEligibilityException(Exception):
    pass

class InsufficientFundException(Exception):
    pass

class InvalidAccountException(Exception):
    pass

class OverDraftLimitExceededException(Exception):
    pass

class NullPointerException(Exception):
    pass

class CustomerNotFoundException(Exception):
    pass