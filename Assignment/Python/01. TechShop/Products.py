import Exceptions

class Product:
    def __init__(self, productName, description, price):
        self.productName = productName
        self.description = description
        if not isinstance(price, (int, float)) or price < 0:
            raise Exceptions.InvalidPriceError("Price must be a non-negative number")
        self.price = price


    def productName(self):
        return self.productName

    def productName(self, value):
        if not isinstance(value, str):
            raise ValueError("Product name must be a string")
        self.productName = value


    def description(self):
        return self.description


    def set_description(self, value):
        self.description = value


    def price(self):
        return self.price

    def set_price(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            try:
                raise Exceptions.InvalidPriceError("Price must be a non-negative number")
            except Exception as e:
                print("Error",e)
        self.price = value

