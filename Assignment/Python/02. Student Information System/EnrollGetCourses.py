from ConnUtil import dbConnection
from datetime import datetime
from DuplicateEnrollmentException import DuplicateEnrollmentException
from CourseNotFoundException import CourseNotFoundException

class Student2(dbConnection):
    def __init__(self, StudentID, FirstName, LastName, DateOfBirth, Email, PhoneNumber):
        super().__init__()
        self.StudentID = StudentID
        self.FirstName = FirstName
        self.LastName = LastName
        self.DateOfBirth = DateOfBirth
        self.Email = Email
        self.PhoneNumber = PhoneNumber
        self.enrolled_courses = []

    def EnrollInCourse(self, course):
        try:
            if not self.CourseExists(course["CourseID"]):
                raise CourseNotFoundException("Course not found.")
            if self.IsEnrolledInCourse(course["CourseID"]):
                raise DuplicateEnrollmentException("Student is already enrolled in this course.")

            EnrollmentDate = datetime.now().date()
            data = [(self.StudentID, course["CourseID"], EnrollmentDate)]
            query = '''
                INSERT INTO Enrollment (StudentID, CourseID, EnrollmentDate)
                VALUES (%s, %s, %s)
            '''
            self.open()
            self.stmt.executemany(query, data)
            self.conn.commit()
            print("Enrolled successfully in the course!")
        except CourseNotFoundException as e:
            print(f"Course Not Found:{e}")
        except DuplicateEnrollmentException as e:
            print(f"Error enrolling in the course: {e}")
        except Exception as e:
            print(f"Error enrolling in the course: {e}")
        finally:
            self.close()

    def IsEnrolledInCourse(self, CourseID):
        select_str = 'SELECT COUNT(*) FROM Enrollment WHERE StudentID=%s AND CourseID=%s'
        try:
            self.open()
            data = (self.StudentID, CourseID)
            self.stmt.execute(select_str, data)
            count = self.stmt.fetchone()[0]
            return count > 0
        except Exception as e:
            print(f"Error while checking enrollment status: {e}")
        finally:
            self.close()

    def CourseExists(self, course_id):
        try:
            self.open()
            select_query = "SELECT COUNT(*) FROM Course WHERE CourseID = %s"
            self.stmt.execute(select_query, (course_id,))
            count = self.stmt.fetchone()[0]
            return count > 0
        except Exception as e:
            print(f"Error while checking course status:{e}")
        finally:
            self.close()

    def GetEnrolledCourses(self):
        select_query = 'SELECT CourseID FROM Enrollment WHERE StudentID = %s'
        try:
            self.open()
            self.stmt.execute(select_query, (self.StudentID,))
            enrolled_courses = self.stmt.fetchall()
            return enrolled_courses
        except Exception as e:
            print(f"Error retrieving enrolled courses: {e}")
        finally:
            self.close()





