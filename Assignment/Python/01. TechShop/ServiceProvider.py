from DBConnUtil import dbConnection
import mysql.connector as connection
from Customer import Customer
from Products import Product
from Orders import Orders
import Exceptions

class ServiceProvider(dbConnection):
    def New_Customer(self):

        first_name = input('Enter First Name :')
        self.firstname = first_name

        last_name = input('Enter Last Name :')
        self.lastname = last_name

        Email = input('Enter email:')
        self.email = Email

        Phone = input('Enter phone :')
        self.phone = Phone

        Address = input('Enter address :')
        self.address = Address

        data = [(self.firstname, self.lastname, self.email, self.phone, self.address)]
        insert_str = '''insert into Customers(FirstName,LastName,Email,Phone,Address) 
        values(%s,%s,%s,%s,%s)'''
        self.open()
        self.mycursor.executemany(insert_str, data)
        self.conn_str.commit()
        print('Records Inserted Successfully..')
        self.close()

    def Get_Total_Orders(self, customer_id):
        self.open()
        total_orders_str = '''
                        SELECT COUNT(*) FROM Orders
                        INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID
                        WHERE Customers.CustomerID = %s
                    '''
        self.mycursor.execute(total_orders_str, (customer_id,))
        total_orders = self.mycursor.fetchone()[0]
        self.close()
        return f"Total orders placed by CustomerID {customer_id}: {total_orders}"


    def Customer_Details(self, customer_id):
            self.open()
            select_customer_str = '''
                SELECT * FROM Customers
                WHERE CustomerID = %s
            '''
            self.mycursor.execute(select_customer_str,customer_id)
            customer_data = self.mycursor.fetchone()
            print('\nCustomer Details:')
            print(f"CustomerID: {customer_data[0]}")
            print(f"FirstName: {customer_data[1]}")
            print(f"LastName: {customer_data[2]}")
            print(f"Email: {customer_data[3]}")
            print(f"Phone: {customer_data[4]}")
            print(f"Address: {customer_data[5]}")

    def UpdateCustomerInfo(self):
        self.select()
        customer_id = int(input('Input Customer ID to be Updated: '))
        Id = customer_id

        first_name = input('Enter First Name ((Press Enter to skip)):')
        self.firstname = first_name

        last_name = input('Enter Last Name ((Press Enter to skip)):')
        self.lastname = last_name

        Email = input('Enter email:(Press Enter to skip)')
        self.email = Email

        Phone = input('Enter Phone (Press Enter to skip): ')
        self.phone = Phone

        Address = input('Enter Address (Press Enter to skip): ')
        self.address = Address

        update_str = 'UPDATE customers SET FirstName=%s,LastName=%s,Email=%s,Phone=%s,Address=%s WHERE CustomerID=%s'
        data = [self.firstname, self.lastname, self.email, self.phone, self.address, Id]

        self.open()
        self.mycursor.execute(update_str, data)
        self.conn_str.commit()
        print('Record updated successfully.')
        self.select()

    def select(self):
        self.open()
        select_str = '''select * from customers'''
        self.mycursor.execute(select_str)
        records = self.mycursor.fetchall()
        print('')
        print('_________________Records In Customer Table________________________')
        for i in records:
            print(i)
        self.close()


# '''   Products Table '''


    def New_Product(self):
        Product_Name = input('Enter Product Name :')
        self.productNameroductName = Product_Name

        Description = input('Enter Description:')
        self.description = Description

        price = int(input('Enter Price:'))
        self.price = price

        data = [(self.productName, self.description, self.price)]
        insert_str = '''INSERT INTO Products (ProductName, Description, Price) 
                        VALUES (%s, %s, %s)'''

        self.open()
        self.mycursor.executemany(insert_str, data)
        self.conn_str.commit()
        print('Records Inserted Successfully..')
        self.close()


    def selectProducts(self):
        self.open()

        select_str = '''SELECT * FROM Products'''
        self.mycursor.execute(select_str)
        records = self.mycursor.fetchall()
        print('')
        print('_________________Records In Products Table________________________')
        for record in records:
            print(record)
        self.close()


    def UpdateProductInfo(self):
        self.selectProducts()
        Product_id = int(input('Input Product ID to be Updated: '))
        Id = Product_id

        Product_name = input('Enter Product Name ((Press Enter to skip)):')
        self.productName = Product_name

        Description = input('Enter Description:(Press Enter to skip)')
        self.description = Description

        Price = input('Enter Price: (Press Enter to skip): ')
        self.price = int(Price)

        update_str = 'UPDATE Products SET ProductName=%s, Description=%s, Price=%s, WHERE ProductID=%s'
        data = [self.productName,self.description,self.price,Id]
        self.open()
        self.mycursor.execute(update_str, data)
        self.conn_str.commit()
        print('Record updated successfully.')
        self.selectProducts()


    def deleteProduct(self):
        self.selectProducts()
        Product_id = int(input('Input Product ID to be Deleted: '))
        Id = Product_id
        delete_str = f'DELETE FROM Products WHERE ProductID={Id}'
        self.open()
        self.mycursor.execute(delete_str)
        (self.conn_str.commit())
        self.close()
        print('Record Deleted Successfully..')


    def View_Product_Details(self, product_id):
        try:
            # Validate product_id
            if not isinstance(product_id, int) or product_id < 0:
                raise Exceptions.InvalidIDError()

            self.open()
            get_product_details_str = '''
                SELECT * FROM Products
                WHERE ProductID = %s
            '''
            self.mycursor.execute(get_product_details_str, (product_id,))
            product_data = self.mycursor.fetchone()

            if not product_data:
                print(f"No product found with ProductID: {product_id}")
            else:
                return f"Product Details:\n ProductID: {product_data[0]}\nProductName: {product_data[1]}\nDescription: {product_data[2]}\nPrice: {product_data[3]}"
            self.close()
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")


    # '''   Orders    '''
    #

    def place_new_order(self):
        CustomerID = int(input('Enter CustomerID:'))
        if not isinstance(CustomerID, int) or CustomerID < 0:
            raise Exceptions.InvalidIDError()
        self.CustomerId = CustomerID

        order_date = input('Enter Order Date (YYYY-MM-DD) or leave blank for current date: ')

        TotalAmount = int(input('Enter TotalAmount:'))
        self.TotalAmount = TotalAmount

        # if not order_date_input:
        #     order_date = datetime.now().strftime('%Y-%m-%d')
        # else:
        #     order_date = order_date_input

        data = [(self.CustomerId, order_date, self.TotalAmount)]
        insert_order_str = '''INSERT INTO Orders (CustomerID, OrderDate, TotalAmount) 
                              VALUES (%s, %s, %s)'''

        self.open()
        self.mycursor.executemany(insert_order_str, data)
        self.conn_str.commit()
        print('Order Record Inserted Successfully..')
        self.close()


    def view_order_details(self, order_id):
        try:
            if not isinstance(order_id, int) or order_id < 0:
                raise Exceptions.InvalidIDError()
            query = '''
                SELECT OrderID, CustomerID, OrderDate, TotalAmount, Status
                FROM Orders
                WHERE OrderID = %s
            '''

            self.open()
            self.mycursor.execute(query, (order_id,))
            order_details = self.mycursor.fetchone()

            if order_details:
                print('\nOrder Details:')
                print(f"OrderID: {order_details[0]}")
                print(f"CustomerID: {order_details[1]}")
                print(f"OrderDate: {order_details[2]}")
                print(f"TotalAmount: {order_details[3]}")
                print(f"Status: {order_details[4]}")
            else:
                print(f'Order with OrderID {order_id} not found.')

        except ValueError as ve:
            print(f"Error: {ve}")

        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

        finally:
            self.close()


    def selectOrders(self):
        self.open()
        select_orders_str = '''SELECT * FROM Orders'''
        self.mycursor.execute(select_orders_str)
        records = self.mycursor.fetchall()
        print('')
        print('_________________Records In Orders Table________________________')
        for record in records:
            print(record)
        self.close()


    def updateOrder(self):
        self.selectOrders()
        order = int(input('Input Order ID to be Updated: '))
        if not isinstance(order, int) or order < 0:
            raise Exceptions.InvalidIDError()
        orderId = order
        update_order_str = 'UPDATE Orders SET '
        data = []

        self.customerID = int(input('Enter Customer ID (Press Enter to skip): '))
        if self.customerID:
            update_order_str += 'CustomerID=%s, '
            data.append(self.customerID)

        self.orderDate = input('Enter Order Date (YYYY-MM-DD) (Press Enter to skip): ')
        if self.orderDate:
            update_order_str += 'OrderDate=%s, '
            data.append(self.orderDate)

        self.totalAmount = input('Enter Total Amount (Press Enter to skip): ')
        if self.totalAmount:
            update_order_str += 'TotalAmount=%s, '
            data.append(self.totalAmount)

        update_order_str = update_order_str.rstrip(', ')

        update_order_str += ' WHERE OrderID=%s'
        data.append(orderId)

        self.open()
        self.mycursor.execute(update_order_str, data)
        (self.conn_str.commit())
        print('Order Record updated successfully.')
        self.selectOrders()


    def deleteOrder(self):
        self.selectOrders()
        Order_id = int(input('Input Order ID to be Deleted: '))
        # if not isinstance(Order_id, int) or Order_id < 0:
        #     raise InvalidIDError()
        Id = Order_id
        delete_order_str = f'DELETE FROM Orders WHERE OrderID={Id}'
        self.open()
        self.mycursor.execute(delete_order_str)
        self.conn_str.commit()
        print('Order Record Deleted Successfully..')
        self.selectOrders()

    def update_order_status(self, order_id, new_status):
        self.selectOrders()
        update_str = 'UPDATE Orders SET Status = %s WHERE OrderID = %s'
        data = (new_status, order_id)
        self.open()
        self.mycursor.execute(update_str, data)
        self.conn_str.commit()
        print('Order status updated successfully.')
        self.selectOrders()
        self.close()


    # def CalculateTotalAmount(self):
    #     try:
    #         OrderID = int(input('Enter Order ID:'))
    #         if not isinstance(OrderID, int) or OrderID < 0:
    #             raise InvalidIDError()
    #
    #         self.OrderID = OrderID
    #         self.open()
    #
    #         statement = '''
    #             SELECT Price, Quantity
    #             FROM OrderDetails
    #             INNER JOIN Orders ON Orders.OrderID = OrderDetails.OrderID
    #             INNER JOIN Products ON Products.ProductID = OrderDetails.ProductID
    #             WHERE Orders.OrderID = %s
    #         '''
    #
    #         self.stmt.execute(statement, (OrderID,))
    #         records = self.stmt.fetchall()
    #
    #         if not records:
    #             raise CustomError("No records found for the specified Order ID.")
    #
    #         total_amount = 0
    #
    #         for record in records:
    #             price = float(record[0])
    #             quantity = int(record[1])
    #             total_amount += price * quantity
    #
    #         discount = float(input("Enter discount (in percentage):"))
    #
    #         if discount < 0 or discount > 100:
    #             raise CustomError("discount should be between 0-100")
    #
    #         discount /= 100
    #         total_amount *= (1 - discount)
    #         print(total_amount)
    #
    #         update_statement = 'UPDATE Orders SET TotalAmount=%s WHERE OrderID=%s'
    #         update_data = (Decimal(total_amount), OrderID)
    #
    #         self.stmt.execute(update_statement, update_data)
    #         self.conn.commit()
    #         self.close()
    #         print("Total Amount after discount:", total_amount)
    #
    #     except Exception as e:
    #         print(f"An unexpected error occurred: {str(e)}")
    #


    def IsProductInStock(self, product_id):
        try:
            if not isinstance(product_id, int) or product_id < 0:
                raise Exceptions.InvalidIDError()

            self.open()
            query = '''
                SELECT Inventory.QuantityInStock
                FROM Products
                INNER JOIN Inventory ON Products.ProductID = Inventory.ProductID
                WHERE Products.ProductID = %s
            '''

            self.mycursor.execute(query, (product_id,))
            result = self.mycursor.fetchone()

            if result and result[0] > 0:
                return True
            else:
                return False

        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            return False

    def AlterTable(self):
        alter_str = '''
                ALTER TABLE Orders
                    ADD COLUMN Status VARCHAR(50) DEFAULT 'Processing'
            '''
        self.open()
        self.mycursor.execute(alter_str)
        self.conn_str.commit()
        print('Orders Table altered successfully------:')
        self.close()


#
# sp=ServiceProvider()
# sp.AlterTable()