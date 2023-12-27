import mysql.connector as connection

from DBConnUtil import DbC

class OrderProcessorRepository(DbC):
    def __init__(self):
        pass

    def createProduct(self, pob):
        pid = 0
        try:
            self.open()
            self.c.execute(f'''Insert Into products (name, price, description, stockQuantity) Values ('{pob.name}', {float(pob.price)}, '{pob.description}', {pob.stock_quantity})''')
            self.mydb.commit()
            pid = self.c.lastrowid
        except Exception as e:
            print(e)
        else:
            print(f'\nProduct - {pob.name} Inserted into the database with ID - {pid}.')
        finally:
            self.close()
            return not pid == 0
        
    def deleteProduct(self, pid):
        rc = 0
        try:
            self.open()
            self.c.execute(f'''Delete From products Where product_id = {pid}''')
            self.mydb.commit()
            rc = self.c.rowcount
        except Exception as e:
            print(e)
        else:
            if rc > 0:
                print(f'\nDeleted Product with ID - {pid} from the database.')
        finally:
            self.close()
            return rc>0
        
    def createCustomer(self, cob):
        cid = 0
        try:
            self.open()
            self.c.execute(f'''Insert Into customers (name, email, password) Values ('{cob.name}', '{cob.email}', '{cob.password}')''')
            self.mydb.commit()
            cid = self.c.lastrowid
            self.close()
        except Exception as e:
            print(e)
        else:
            print(f'\nCustomer - {cob.name} Inserted into the database with ID - {cid}.')
        finally:
            self.close()
            return not cid == 0
    
    def deleteCustomer(self, cid):
        rc = 0
        try:
            self.open()
            self.c.execute(f'''Delete From customers Where customer_id = {cid}''')
            self.mydb.commit()
            rc = self.c.rowcount
        except Exception as e:
            print(e)
        else:
            print(f'\nDeleted Customer with ID - {cid} from the database.')
        finally:
            self.close()
            return rc>0
        
    def addToCart(self, cob, pob, qty):
        cartid =0
        try:
            self.open()
            self.c.execute(f'''Insert Into cart (customer_id, product_id, quantity) Values ({cob.get_customer_id()}, {pob.get_product_id()}, {qty})''')
            cartid = self.c.lastrowid
            self.mydb.commit()
        except Exception as e:
            print(e)
        else:
            print(f'\nItems Added to the Cart.')
        finally:
            self.close()
            return not (cartid == 0)

    def removeFromCart(self, cob, pob):
        rc = 0
        try:
            self.open()
            self.c.execute(f'''Delete From cart Where customer_id = {cob.customer_id} And product_id = {pob.product_id}''')
            self.mydb.commit()
            rc = self.c.rowcount
        except Exception as e:
            print(e)
        else:
            print('\nItems Removed From the Cart.')
        finally:
            self.close()
            return rc>0
        
    def getAllFromCart(self, cob):
        pros = dict()
        try:
            self.open()
            self.c.execute(f'''Select product_id , quantity From cart c Where customer_id = {cob.customer_id}''')
            for i in self.c:
                p, qty = i[0], i[1]
                pros[p] = qty
        except Exception as e:
            print(e)
        finally:
            self.close()
            return pros


    def placeOrder(self, cob, pros, add):
        total_price, oid = 0, 0
        try:
            for pid,qty in pros.items():
                self.open()
                self.c.execute(f'''Select price from products Where product_id = {pid}''')
                cost = self.c.fetchone()[0]
                total_price = total_price + (qty*float(cost))
                self.close()
        except Exception as e:
            print(e)

        try:
            self.open()
            self.c.execute(f'''Insert Into orders (customer_id, order_date, total_price, shipping_address) Values ({cob.customer_id}, CURDATE(), {total_price}, '{add}')''')
            self.mydb.commit()
            oid = self.c.lastrowid
            self.close()
        except Exception as e:
            print(e)

        try:
            for k,v in pros.items():
                self.open()
                self.c.execute(f'''Insert Into order_items (order_id, product_id, quantity) Values ({oid}, {k}, {v})''')
                self.mydb.commit()
                self.close()
                self.open()
                self.c.execute(f'''Update products SET stockQuantity = stockQuantity-{v} Where product_id = {k}''')
                self.mydb.commit()
                self.close()
        except Exception as e:
            print(e)
        
        if oid != 0:
            print(f'\nOrder Placed Successfully..\nYour Order ID is {oid}.')
            self.open()
            self.c.execute(f'''Delete From cart Where customer_id = {cob.customer_id}''')
            self.mydb.commit()
            self.close()
            return True
        
        return False
    

    def getOrdersByCustomer(self, cid):
        o = 0
        try:
            self.open()
            self.c.execute(f'''Select * From orders Where customer_id = {cid}''')
            o = self.c.fetchall()
        except Exception as e:
            print(e)
        else:
            print('\nThese are the Orders placed : ')
            for i in o:
                print(i)
        finally:
            if self.c.rowcount == 0:
                print('None')
            self.close()
