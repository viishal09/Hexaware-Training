import re
# from main.main import BankApp

class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone_number, address, credit_score, annual_income):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.credit_score = credit_score
        self.annual_income = annual_income

    def get_customer_id(self):
        return self.customer_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phone_number

    def get_address(self):
        return self.address

    def get_credit_score(self):
        return self.credit_score

    def get_annual_income(self):
        return self.annual_income

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_email(self, email):
        self.email = email

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_address(self, address):
        self.address = address

    def set_credit_score(self, credit_score):
        self.credit_score = credit_score

    def set_annual_income(self, annual_income):
        self.annual_income = annual_income

    def validate_email(self, email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return email
        else:
            raise ValueError("Invalid email address")

    def validate_phone_number(self, phone_number):
        if re.match(r"^\d{10}$", phone_number):
            return phone_number
        else:
            raise ValueError("Invalid phone number")

    def __str__(self):
        return f"Customer ID: {self.customer_id}\n" \
               f"Name: {self.first_name} {self.last_name}\n" \
               f"Email: {self.email}\n" \
               f"Phone Number: {self.phone_number}\n" \
               f"Address: {self.address}"

