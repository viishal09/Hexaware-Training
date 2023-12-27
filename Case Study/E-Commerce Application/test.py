import unittest

from Customer import Customer
from Products import Product
from ServiceRepository import OrderProcessorRepository

class TestEcommerce(unittest.TestCase):
    def test_product_creation(self):
        p = Product(name='Iphone', price=1999, description= 'Phone', stock_quantity=200)
        result = OrderProcessorRepository.createProduct(pob=p)
        self.assertEqual(result, True, 'Product Creation Successful.')

    def test_customer_registration(self):
        c = Customer(name='Vishal', email = 'vishal@mail.com', password='vishal')
        result = OrderProcessorRepository.createCustomer(cob=c)
        self.assertEqual(result, True, 'Customer Registration Successful.')

if __name__ == '_main_':
    unittest.main()