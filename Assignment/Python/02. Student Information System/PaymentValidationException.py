class PaymentValidationException(Exception):
    def __init__(self,msg="Invalid Payment"):
        super().__init__(msg)
