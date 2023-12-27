import mysql.connector as connection


from DBConnUtil import DbC

import mysql.connector as connection

from Customer import Customer
from Products import Product

from ServiceRepository import OrderProcessorRepository

from myExceptions import CustomerNotFoundException, ProductNotFoundException, OrderNotFoundException

class EcomApp(DbC):
    def __init__(self):
        pass

    def retrieveCustomerObject(self, cid):
        cust = None
        try:
            self.open()
            self.c.execute(f'''Select * From customers Where customer_id = {cid}''')
            rc = self.c.rowcount
            if rc != 1:
                raise CustomerNotFoundException('\nNo Such Customer Exists in the Database..')
            cust = self.c.fetchone()
            self.close()
        except Exception as e:
            print(e)
        else:
            return Customer(*cust)
        
    def retrieveProductObject(self, pid):
        pro = None
        try:
            self.open()
            self.c.execute(f'''Select * From products Where product_id = {pid}''')
            rc = self.c.rowcount
            if rc != 1:
                raise ProductNotFoundException('\nNo Such Product Exists in the Database..')
            pro = self.c.fetchone()
            self.close()
        except Exception as e:
            print(e)
        else:
            return Product(*pro)
        
    def main(self):
        opr = OrderProcessorRepository()
        while True:
            print('\n----------MAIN MENU----------')
            print('Press -> 1 to Register Customer')
            print('Press -> 2 to Create Product')
            print('Press -> 3 to Delete Product')
            print('Press -> 4 to Add to cart')
            print('Press -> 5 to View cart')
            print('Press -> 6 to Place order')
            print('Press -> 7 to View Customer Order')
            print('Press -> 8 to EXIT')
            ch = int(input())
            if ch == 1:
                n = input('\nEnter Name : ')
                e = input('Enter Email : ')
                p = input('Enter Password : ')
                cob = Customer(name=n, email=e, password=p)
                opr.createCustomer(cob)
            elif ch == 2:
                n = input('\nEnter Product Name : ')
                p = float(input('Enter Product Price : '))
                d = input('Enter Product Description : ')
                qty = int(input('Enter the Stock Quantity : '))
                pob = Product(name=n, price=p, description=d, stock_quantity=qty)
                opr.createProduct(pob)
            elif ch == 3:
                pid = int(input('\nEnter the Product ID : '))
                try:
                    if not opr.deleteProduct(pid):
                        raise ProductNotFoundException('\nNo Such Product Exists in the Database..')
                except Exception as e:
                    print(e)
            elif ch == 4:
                cid = int(input('\nEnter the Customer ID : '))
                print()
                self.open()
                self.c.execute('Select * From products')
                for i in self.c:
                    print(i)
                self.close()
                pid = int(input('\nEnter the ID for Product from the Table above : '))
                qty = int(input('Enter the Product Quantity : '))
                opr.addToCart(self.retrieveCustomerObject(cid), self.retrieveProductObject(pid), qty)
            elif ch == 5:
                cid = int(input('\nEnter the Customer ID : '))
                pros = opr.getAllFromCart(self.retrieveCustomerObject(cid))
                if len(pros) == 0:
                    print('\nYour Cart is Empty...')
                    continue
                print('\nFollowing are the Cart Items :\n*ProductName-(Qty)*')
                for p, qty in pros.items():
                    print(f'> {self.retrieveProductObject(p).get_name()}-({qty})')
            elif ch == 6:
                cid = int(input('\nEnter the Customer ID : '))
                pros = opr.getAllFromCart(self.retrieveCustomerObject(cid))
                if len(pros) == 0:
                    print('\nYour Cart is Empty...')
                    continue
                add = input('\nEnter the Shipping Address : ')
                opr.placeOrder(self.retrieveCustomerObject(cid), pros, add)
            elif ch == 7:
                cid = int(input('\nEnter the Customer ID : '))
                opr.getOrdersByCustomer(cid)
            elif ch == 8:
                print('\n----------THANK YOU----------')
                break
            else:
                print('\nInvalid Choice ..... Please Try Again !!!')

if __name__ == "__main__":
    EcomApp().main()