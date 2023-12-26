class InvalidEmailError(Exception):
    def __init__(self, email, message="Invalid email format"):
        self.email = email
        # self.message = f'{email} should end with @gmail.com or @yahoo.com'
        super().__init__(self.message)

class InvalidAddressError(Exception):
    def __init__(self, message="Address must be a string"):
        self.message = message
        super().__init__(self.message)

class InvalidPriceError(Exception):
    def __init__(self, message="Price must be number and positive"):
        self.message = message
        super().__init__(self.message)

class InvalidIDError(Exception):
    def __init__(self, message="ID must be an integer and must be positive"):
        self.message = message
        super().__init__(self.message)
