class Student:
    def __init__(self,Student_ID,First_Name,Last_Name,Date_of_Birth,Email,Phone_Number):
        self.Student_ID=Student_ID
        self.First_Name=First_Name
        self.Last_Name=Last_Name
        self.Date_of_Birth=Date_of_Birth
        self.Email=Email
        self.Phone_Number=Phone_Number
        print(f"Student ID:{self.Student_ID} \nFirst Name:{self.First_Name} \nLast Name:{self.Last_Name} \nDate of Birth:{self.Date_of_Birth}"
              f"\nEmail:{self.Email} \nPhone Number:{self.Phone_Number}")

Student(1,"Sona","Vuthur",'2002-01-06','sona@gmail.com','8247238787')