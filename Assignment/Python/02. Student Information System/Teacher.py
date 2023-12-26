class Teacher:
    def __init__(self,Teacher_ID,First_Name,Last_Name,Email):
        self.Teacher_ID=Teacher_ID
        self.First_Name=First_Name
        self.Last_Name=Last_Name
        self.Email=Email
        print(f"Teacher ID:{self.Teacher_ID} \nFirst Name:{self.First_Name} \nLast Name:{self.Last_Name} \nEmail:{self.Email}")

Teacher(400,"Dhana","Laxmi",'dhana@gmail.com')