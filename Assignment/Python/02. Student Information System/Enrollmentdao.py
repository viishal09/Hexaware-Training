from ConnUtil import dbConnection
from datetime import datetime
from InvalidEnrollmentDataException import InvalidEnrollmentDataException
from InsufficientFundsException import InsufficientFundsException
class Enrollment(dbConnection):
    def GetStudent(self):
        try:
            self.open()
            print("Students enrolled:")
            select_str='''select Enrollment_Id as EID,Student_Id as SID from Enrollments'''
            self.stmt.execute(select_str)
            data=self.stmt.fetchall()
            for i in data:
                print(i)
        except Exception as e:
            print(e)
        finally:
            self.close()

    def GetCourse(self):
        try:
            self.open()
            print("Courses Enrolled:")
            select_str='''select Enrollment_Id,Course_Id from Enrollments'''
            self.stmt.execute(select_str)
            data=self.stmt.fetchall()
            for i in data:
                print(i)
        except Exception as e:
            print(e)
        finally:
            self.close()

    def validate_enrollment_data(self, Student_Id, Course_Id):
        try:
            if not (isinstance(Student_Id,int) and isinstance(Course_Id,int)):
                raise InvalidEnrollmentDataException("Invalid enrollment data. Both Student_Id and Course_Id must be integers.")
        except InvalidEnrollmentDataException as e:
            print(e)

    def check_sufficient_funds(self, Student_Id):
        try:
            self.open()
            select_str = '''select Amount from Payment where Student_Id = %s'''
            self.stmt.execute(select_str, (Student_Id,))
            total_payment = sum(row[0] for row in self.stmt.fetchall())
            return total_payment > 0
        except Exception as e:
            print(e)
            return False
        finally:
            self.close()

    def EnrollStudentInCourse(self, Student_Id, Course_Id):
        try:
            self.validate_enrollment_data(Student_Id, Course_Id)
            if not self.check_sufficient_funds(Student_Id):
                raise InsufficientFundsException(f"Insufficient funds for student with ID {Student_Id}.")

            self.open()
            insert_str = '''insert into Enrollments(Student_Id, Course_Id, Enrollment_Date)
                            values(%s, %s, %s)'''
            data = [(Student_Id, Course_Id, datetime.now())]
            self.stmt.executemany(insert_str, data)
            self.conn.commit()
            print("Student enrolled in course successfully")
        except InsufficientFundsException as e:
            print(e)
        except Exception as e:
            print(e)
        finally:
            self.close()
