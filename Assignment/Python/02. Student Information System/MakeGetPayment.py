from ConnUtil import dbConnection
from datetime import datetime

class Student1(dbConnection):
    def __init__(self, Student_ID, First_Name, Last_Name, Date_Of_Birth, Email, Phone_Number):
        super().__init__()
        self.Student_ID = Student_ID
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Date_Of_Birth = Date_Of_Birth
        self.Email = Email
        self.Phone_Number = Phone_Number
        self.payment_history = []

    def MakePayment(self, Payment_ID,amount, payment_Date):
        data = (self.Student_ID, Payment_ID,amount, payment_Date)
        query = '''
            INSERT INTO Payments (Student_ID, Payment_ID,Amount, Payment_Date)
            VALUES (%s, %s, %s,%s)
        '''
        try:
            self.open()
            self.stmt.execute(query, data)
            self.conn.commit()
            print("Payment recorded successfully!")
        except Exception as e:
            print(f"Error recording payment: {e}")
        finally:
            self.close()

    def GetPaymentHistory(self):
        query = '''
            SELECT Payment_ID, Amount, Payment_Date
            FROM Payments
            WHERE Student_ID = %s
        '''
        try:
            self.open()
            self.stmt.execute(query, (self.StudentID,))
            payment_records = self.stmt.fetchall()
            return payment_records
        except Exception as e:
            print(f"Error retrieving payment history: {e}")
        finally:
            self.close()


