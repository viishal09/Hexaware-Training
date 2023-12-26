from ConnUtil import dbConnection
from TeacherNotFoundException import TeacherNotFoundException
from InvalidTeacherDataException import InvalidTeacherDataException
class Teacher(dbConnection):
    def addTeacher(self,Teacher_Id,First_Name,Last_Name,Email):
        self.Teacher_Id=Teacher_Id
        self.First_Name=First_Name
        self.Last_Name=Last_Name
        self.Email=Email
        try:
            self.open()
            insert_str="insert into Teacher(Teacher_Id,First_Name,Last_Name,Email)values(%s,%s,%s,%s)"
            data=[(Teacher_Id,First_Name,Last_Name,Email)]
            self.stmt.executemany(insert_str,data)
            self.conn.commit()
            print("Teacher added successfully")
            self.close()
        except Exception as e:
            print(e)
    def UpdateTeacherInfo(self):
        try:
            Teacher_Id=int(input("Enter Teacher ID you want to update:"))
            self.First_Name=input("Enter First Name:")
            self.Last_Name=input("Last Name:")
            self.Email=input("Email:")
            if not self.validate_email(self.Email):
                raise InvalidTeacherDataException("Invalid email format.")
            self.open()
            update_str='''update Teacher set First_Name=%s,Last_Name=%s,Email=%s where Teacher_Id=%s'''
            data=[(self.First_Name,self.Last_Name,self.Email,Teacher_Id)]
            self.stmt.executemany(update_str,data)
            self.conn.commit()
            print("Updated successfully")
            self.close()
        except InvalidTeacherDataException as e:
            print(e)
        except Exception as e:
            print(e)
    def DisplayTeacherInfo(self):
        try:
            self.open()
            print("Teacher Info:")
            select_str='''select * from teacher'''
            self.stmt.execute(select_str)
            data=self.stmt.fetchall()
            for i in data:
                print(i)
        except Exception as e:
            print(e)
        finally:
            self.close()
    def GetAssignedCourses(self):
        try:
            self.open()
            print("Assigned Courses")
            select_str='''select Teacher_Id,Course_ID from Courses'''
            self.stmt.execute(select_str)
            data=self.stmt.fetchall()
            for i in data:
                print(i)
        except Exception as e:
            print(e)

    def teacherExists(self, Teacher_Id):
        try:
            self.open()
            select_str = '''select COUNT(*) from Teacher where Teacher_Id=%s'''
            self.stmt.execute(select_str, (Teacher_Id,))
            count = self.stmt.fetchone()[0]
            return count > 0
        except Exception as e:
            print(e)
        finally:
            self.close()

    def AssignTeacherToCourse(self, Teacher_Id, Course_ID):
        try:
            self.open()
            if not self.teacherExists(Teacher_Id):
                raise TeacherNotFoundException(f"Teacher with ID {Teacher_Id} not found.")
            print(f"Assigned teacher {Teacher_Id} to course {Course_ID}")
        except TeacherNotFoundException as e:
            print(e)
        except Exception as e:
            print(e)
        finally:
            self.close()

    def validate_email(self, email):
        return '@' in email



