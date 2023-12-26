import mysql.connector as sql
from datetime import date
from ConnUtil import dbConnection
class SIS(dbConnection):
    def CreateTables(self):
        try:
            self.open()
            self.stmt.execute("create table if not exists Student(StudentID int primary key,"
                              "FirstName varchar(30),"
                              "LastName varchar(30),"
                              "DateOfBirth date,"
                              "Email varchar(30),"
                              "PhoneNumber char(10))")
            print("Student table created successfully")
            self.stmt.execute("create table if not exists Course(CourseID int primary key,"
                              "CourseName varchar(30),"
                              "CourseCode varchar(10),"
                              "InstructorName varchar(30))")
            print("Course Table created successfully")
            self.stmt.execute("create table  Enrollment(EnrollmentID int primary key AUTO_INCREMENT,"
                              "StudentID int,"
                              "CourseID int,"
                              "EnrollmentDate date,"
                              "FOREIGN KEY(StudentID) references Student(StudentID),"
                              "FOREIGN KEY(CourseID) references Course(CourseID))")
            print("Enrollment Table created successfully")
            self.stmt.execute("create table if not exists Teacher(TeacherID int primary key,"
                              "FirstName varchar(30),"
                              "LastName varchar(30),"
                              "Email varchar(30))")
            print("Teacher table created successfully")
            self.stmt.execute("create table if not exists Payment(PaymentID int primary key,"
                              "StudentID int,"
                              "Amount float,"
                              "PaymentDate date,"
                              "FOREIGN KEY(StudentID) references Student(StudentID))")
            print("Payment table created successfully")
        except Exception as e:
            print(e)

sis=SIS()
sis.CreateTables()