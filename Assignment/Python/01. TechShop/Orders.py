class Orders:
    def __init__(self, customer, order_date, total_amount):
        self.customer = customer
        self.order_date = order_date
        self.total_amount = total_amount

    def CalculateTotalAmount(self):
        pass

    def GetOrderDetails(self):
        details = (
            # f"Order ID: {self.order_id}\n"
            f"Order Date: {self.order_date}\n"
            f"Total Amount: ${self.total_amount}\n"
            f"Customer Details:\n{self.customer.GetCustomerDetails()}"
        )
        return details

    def UpdateOrderStatus(self, new_status):
        pass

    def CancelOrder(self):
        pass