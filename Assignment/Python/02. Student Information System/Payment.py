class Payment:
    def __init__(self,Payment_ID,Student_ID,Amount,Payment_Date):
        self.Payment_ID=Payment_ID
        self.Student_ID=Student_ID
        self.Amount=Amount
        self.Payment_Date=Payment_Date
        print(f"Payment ID:{self.Payment_ID} \nStudent ID:{self.Student_ID} \nAmount:{self.Amount} \nPayment Date:{self.Payment_Date}")

Payment(700,12,45000.00,'2023-09-08')