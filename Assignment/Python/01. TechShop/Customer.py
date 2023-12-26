import Exceptions
import re
from DBConnUtil import dbConnection

class Customer(dbConnection):
    def __init__(self, firstName, lastName, email, phone, address):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone
        self.address = address

    def customerID(self):
        return self.customerID


    def firstName(self):
        return self.firstName

    def firstName(self, value):
        if not isinstance(value, str):
            raise ValueError("First name must be a string")
        self.firstName = value

    def lastName(self):
        return self.lastName

    def lastName(self, value):
        if not isinstance(value, str):
            raise ValueError("Last name must be a string")
        self.lastName = value

    def email(self):
        return self.email

    def email(self, value):
        if not self._is_valid_email(value):
            raise Exceptions.InvalidEmailError("Invalid email address")
        self.email = value

    def _is_valid_email(self, email):
        # Basic email validation using a regular expression
        email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
        return bool(re.match(email_pattern, email))
    def phone(self):
        return self.phone


    def phone(self, value):
        # Add phone validation logic if needed
        self._phone = value


    def address(self):
        return self.address


    def address(self, value):
        if not isinstance(value, str):
            raise Exceptions.InvalidAddressError("Address must be a string")
        self.address = value
