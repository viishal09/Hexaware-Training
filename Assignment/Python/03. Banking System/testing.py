import unittest
from unittest.mock import patch
from accountdao import AccountDAO
from loanservice import LoanService
from customer import Customer
from exceptions import LoanEligibilityException


class TestAccountDAO(unittest.TestCase):
    def test_create_account(self):
        try:
            account_dao = AccountDAO()
            self.assertIsInstance(account_dao, AccountDAO)

        finally:
            pass

    @patch('builtins.input', side_effect=["701", "50001.0"])
    def test_loan_service_eligible(self, mock_input):
        try:
            # Collect input from the user (mocked in this case)
            credit_score = int(mock_input())
            balance = float(mock_input())

            # Create a Customer object
            customer = Customer(None, None, None, None, None, None, credit_score, balance)

            # Check loan eligibility, no exception should be raised
            LoanService.check_loan_eligibility(customer)

            # Assert that no exception is raised
            self.assertTrue(True)

        except ValueError:
            # AssertionError if ValueError is raised
            self.fail("Invalid input. Please enter valid numeric values.")
        except LoanEligibilityException as e:
            # AssertionError if LoanEligibilityException is raised
            self.fail(f"Loan eligibility check failed: {str(e)}")

    @patch('builtins.input', side_effect=["700", "50000.0"])
    def test_loan_service_not_eligible(self, mock_input):
        try:
            # Collect input from the user (mocked in this case)
            credit_score = int(mock_input())
            balance = float(mock_input())

            # Create a Customer object
            customer = Customer(None, None, None, None, None, None, credit_score, balance)

            # Check loan eligibility, LoanEligibilityException should be raised
            with self.assertRaises(LoanEligibilityException) as context:
                LoanService.check_loan_eligibility(customer)

            # Verify the error message in the exception
            self.assertEqual(str(context.exception), "Loan eligibility criteria not met.")

        except ValueError:
            # AssertionError if ValueError is raised
            self.fail("Invalid input. Please enter valid numeric values.")


if __name__ == '_main_':
    unittest.main()