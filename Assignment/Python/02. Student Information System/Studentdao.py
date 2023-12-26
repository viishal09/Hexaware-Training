from ConnUtil import dbConnection
from datetime import datetime
from StudentNotFoundException import StudentNotFoundException
from InvalidStudentDataException import InvalidStudentDataException
class Students(dbConnection):
    try:
        def __init__(self):
            super().__init__()

        def addStudent(self, Student_ID, First_Name, Last_Name, Date_of_Birth, Email, Phone_Number):
            self.Student_ID = Student_ID
            self.First_Name = First_Name
            self.Last_Name = Last_Name
            self.Date_of_Birth = Date_of_Birth
            self.Email = Email
            self.Phone_Number = Phone_Number
            self.open()
            insert_str = '''insert into Students(Student_ID, First_Name, Last_Name, Date_of_Birth, Email, Phone_Number)
                            values(%s, %s, %s, %s, %s, %s)'''
            data = [(self.Student_ID, self.First_Name, self.Last_Name, self.Date_of_Birth, self.Email, self.Phone_Number)]
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            print("Student added successfully")
            self.close()

        def UpdateStudentInfo(self):
            try:
                Student_ID = int(input("Enter Student_ID you want to update:"))
                if not self.studentExists(Student_ID):
                    raise StudentNotFoundException(f"Student with ID {Student_ID} not found.")
                self.First_Name = input("First Name:")
                self.Last_Name = input("Last Name:")
                self.Date_of_Birth = input("Date of Birth (YYYY-MM-DD):")
                self.Email = input("Email:")
                if not self.validate_email(self.Email):
                    raise InvalidStudentDataException("Invalid email format.")

                self.Phone_Number = input("Phone Number:")
                self.open()
                update_str = '''update Students set First_Name=%s,Last_Name=%s,Date_of_Birth=%s,Email=%s,Phone_Number=%s 
                                where Student_ID=%s'''
                data = [(self.First_Name, self.Last_Name, self.Date_of_Birth, self.Email, self.Phone_Number, Student_ID)]
                self.stmt.executemany(update_str, data)
                self.conn.commit()
            except InvalidStudentDataException as e:
                print(e)
            except StudentNotFoundException as e:
                print(e)
            except Exception as e:
                print(e)
            finally:
                self.close()

        def DisplayStudentInfo(self):
            self.open()
            select_str = '''select * from Students'''
            self.stmt.execute(select_str)
            data = self.stmt.fetchall()
            for i in data:
                print(i)
            self.close()

        def studentExists(self, Student_ID):
            self.open()
            select_str = '''select COUNT(*) from Students where Student_ID=%s'''
            self.stmt.execute(select_str, (Student_ID,))
            count = self.stmt.fetchone()[0]
            return count > 0
            self.close()

        def validate_email(self, email):
            return '@' in email
    except Exception as e:
        print(e)






