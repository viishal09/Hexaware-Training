from ConnUtil import dbConnection
from PaymentValidationException import PaymentValidationException
class Payment(dbConnection):
    def validate_payment_data(self, Amount, Payment_Date):
        try:
            amount_float = float(Amount)
            if amount_float <= 0:
                raise PaymentValidationException("Invalid payment amount. Amount must be greater than 0.")
            if not Payment_Date:
                raise PaymentValidationException("Payment date is required.")
        except ValueError:
            raise PaymentValidationException("Invalid payment amount format. Amount must be a valid number.")

    def AddPayment(self,Payment_Id,Student_Id,Amount,Payment_Date):
        try:
            self.validate_payment_data(Amount, Payment_Date)
            self.Payment_Id=Payment_Id
            self.Student_Id=Student_Id
            self.Amount=Amount
            self.Payment_Date=Payment_Date
            self.open()
            insert_str='''insert into Payments(Payment_Id,Student_Id,Amount,Payment_Date) values(%s,%s,%s,%s)'''
            data=[(self.Payment_Id,self.Student_Id,self.Amount,self.Payment_Date)]
            self.stmt.executemany(insert_str,data)
            self.conn.commit()
        except PaymentValidationException as e:
            print(e)
        except Exception as e:
            print(e)
        finally:
            self.close()
    def GetStudent(self):
        self.open()
        print("List of Students who made payments:")
        select_str='''select Payment_Id,Student_Id from Payments'''
        self.stmt.execute(select_str)
        data=self.stmt.fetchall()
        for i in data:
            print(i)
    def GetPaymentAmount(self):
        self.open()
        print("Payment Amount")
        select_str='''select Payment_Id,Amount from Payments'''
        self.stmt.execute(select_str)
        data=self.stmt.fetchall()
        for i in data:
            print(i)
    def GetPayment_Date(self):
        self.open()
        print("Payment Dates")
        select_str='''select Payment_Id,Payment_Date from Payments'''
        self.stmt.execute(select_str)
        data=self.stmt.fetchall()
        for i in data:
            print(i)
