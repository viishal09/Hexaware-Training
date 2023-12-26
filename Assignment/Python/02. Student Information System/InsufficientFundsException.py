class InsufficientFundsException(Exception):
    def __init__(self,msg="Insufficient Funds"):
        super().__init__(self,msg)