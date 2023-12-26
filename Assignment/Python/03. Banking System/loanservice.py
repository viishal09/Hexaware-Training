from customer import Customer
from exceptions import LoanEligibilityException

class LoanService:
    @staticmethod
    def check_loan_eligibility(customer: Customer):
        if customer.credit_score > 700 and customer.annual_income >= 50000:
            return True
        else:
            raise LoanEligibilityException("Loan eligibility criteria not met.")
