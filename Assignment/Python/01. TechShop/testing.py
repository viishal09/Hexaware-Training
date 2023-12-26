import unittest
from ServiceProvider import ServiceProvider

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.customer_total_orders = ServiceProvider()
        self.view_product_details = ServiceProvider()

    # Test updating customer information.
    def test_customer_total_orders(self):
        print(" Test total orders for customerID = 4")
        result = self.customer_total_orders.Get_Total_Orders(4)
        self.assertEqual("Total orders placed by CustomerID 4: 1", result)

    def test_view_product_details(self):
        print("Product details for product id = 1 ")
        result = self.view_product_details.View_Product_Details(1)
        self.assertEqual("Product Details:\n ProductID: 1\nProductName: HARDDISK\nDescription: computer component that stores data\nPrice: 100.00",result)


if __name__ == '__main__':
    unittest.main()