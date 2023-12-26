from ConnUtil import dbConnection
from InvalidCourseDataException import InvalidCourseDataException
class Course(dbConnection):
    def AddCourse(self,Course_ID,Course_Name,credits,Teacher_Id):
        self.Course_ID=Course_ID
        self.Course_Name=Course_Name
        self.credits=credits
        self.Teacher_Id=Teacher_Id
        self.open()
        insert_str='''insert into Courses(Course_ID,Course_Name,credits,Teacher_Id) values(%s,%s,%s,%s)'''
        data=[(self.Course_ID,self.Course_Name,self.credits,self.Teacher_Id)]
        self.stmt.executemany(insert_str,data)
        self.conn.commit()
        self.close()
    def UpdateCourseInfo(self):
        try:
            Course_ID=int(input("Enter Course ID u want to update:"))
            self.Course_Name=input("Enter Course Name:")
            self.credits=input("Enter Course Code:")
            self.Teacher_Id=input("Enter Instructor Name:")
            self.open()
            if not self.validate_course_data():
                raise InvalidCourseDataException("Invalid course data.")
            update_str='''update Courses set Course_Name=%s,credits=%s,Teacher_Id=%s where Course_ID=%s'''
            data=[(self.Course_Name,self.credits,self.Teacher_Id,Course_ID)]
            self.stmt.executemany(update_str,data)
            self.conn.commit()
            print("Courses updated successfully")
        except InvalidCourseDataException as e:
            print(e)
        except Exception as e:
            print(e)
        finally:
            self.close()
    def DisplayCourseInfo(self):
        self.open()
        select_str='''select * from Courses'''
        self.stmt.execute(select_str)
        data=self.stmt.fetchall()
        for i in data:
            print(i)
        self.close()
    def GetEnrollments(self):
        self.open()
        select_str='''select StudentID,Course_ID from Enrollments'''
        self.stmt.execute(select_str)
        data=self.stmt.fetchall()
        for i in data:
            print(i)
        self.close()
    def AssignTeacher(self):
        self.open()
        Course_ID=int(input("Enter Course_ID to assign teacher:"))
        self.TeacherID=int(input("TeacherID:"))
        update_str='''update Courses set TeacherID=%s where Course_ID=%s'''
        data=[(self.TeacherID,Course_ID)]
        self.stmt.executemany(update_str,data)
        self.conn.commit()
        print("Teacher assigned successfully")
        self.close()
    def GetTeacher(self):
        self.open()
        print("Teacher assigned to course:")
        select_str='''select Course_ID,TeacherID from Courses'''
        self.stmt.execute(select_str)
        data=self.stmt.fetchall()
        for i in data:
            print(i)
        self.close()
    def validate_course_data(self):
        if len(self.credits) < 3 or len(self.Teacher_Id) < 3:
            return False
        return True



