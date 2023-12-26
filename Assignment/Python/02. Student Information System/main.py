from DuplicateEnrollmentException import DuplicateEnrollmentException
from CourseNotFoundException import CourseNotFoundException
from  StudentNotFoundException import StudentNotFoundException
from TeacherNotFoundException import TeacherNotFoundException
from PaymentValidationException import PaymentValidationException
from InvalidStudentDataException import InvalidStudentDataException
from InvalidCourseDataException import InvalidCourseDataException
from InvalidEnrollmentDataException import InvalidEnrollmentDataException
from InvalidTeacherDataException import InvalidTeacherDataException
from InsufficientFundsException import InsufficientFundsException
from Studentdao import Students
from EnrollGetCourses import Student2
from MakeGetPayment import Student1
from datetime import datetime
from Coursedao import Course
from Enrollmentdao import Enrollment
from teacherdao import Teacher
from Paymentdao import Payment
if __name__ == '__main__':
    try:
        print("................................................................................")
        while True:
            print("1.STUDENT MANAGEMENT \n2.COURSE MANAGEMENT \n3.ENROLLMENT MANAGEMENT \n4.TEACHER MANAGEMENT \n5.PAYMENT MANAGEMENT \n6.STOP")
            choice=int(input("Enter your choice:"))
            if choice==1:
                print("STUDENT MANAGEMENT")
                print("1.Add Student \n2.Update Student Info \n3.Display Student Info \n4.Enroll Courses \n5.Get Enroll Courses\n6.Make Payment"
              "\n7.Get Payment History \n8.Stop")
                k=int(input("Enter choice:"))
                if k==1:
                    s = Students()
                    s.addStudent(Student_ID=int(input("Student ID:")),
                                 First_Name=input("First Name:"),
                                 Last_Name=input("Last Name:"),
                                 Date_of_Birth=input("Date of Birth (YYYY-MM-DD):"),
                                 Email=input("Email:"),
                                 Phone_Number=input("Phone Number:"))
                if k==2:
                    s=Students()
                    s.UpdateStudentInfo()
                if k==3:
                    s=Students()
                    s.DisplayStudentInfo()
                if k==4:
                    s1 = Student2(
                        Student_ID=int(input("Student ID:")),
                        First_Name=input("First Name:"),
                        Last_Name=input("Last Name:"),
                        Date_of_Birth=input("Date of Birth:"),
                        Email=input("Email:"),
                        Phone_Number=input("Phone Number:")
                    )

                    c1 = {"CourseID": 100, "CourseName": "Introduction to Programming", "CourseCode": "CS101",
                          "InstructorName": "Dr. Smith"}
                    s1.EnrollInCourse(c1)
                if k==5:
                    s1=Student2(9000,"Anjali","Rao","2000-9-8","anju@gmail.com",'2323232323')
                    enrolled_courses = s1.GetEnrolledCourses()
                    if enrolled_courses:
                        print("Enrolled Courses:")
                        for CourseID in enrolled_courses:
                            print(f"CourseID: {CourseID[0]}")
                    else:
                        print("No enrolled courses.")
                if k==6:
                    student1 = Student1(
                        Student_ID=int(input("Student ID")),
                        First_Name=input("First name"),
                        Last_Name=input("Last Name"),
                        Date_of_Birth=input("Date of Birth"),
                        Email=input("Email"),
                        Phone_Number=input("Phone Number")
                    )
                    PaymentID = int(input("Enter Payment ID:"))
                    Amount = input("Enter Amount")
                    PaymentDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    student1.MakePayment(PaymentID, Amount, PaymentDate)
                if k==7:
                    student1 = Student1(
                        Student_ID=int(input("Student ID")),
                        First_Name=input("First name"),
                        Last_Name=input("Last Name"),
                        Date_of_Birth=input("Date of Birth"),
                        Email=input("Email"),
                        Phone_Number=input("Phone Number")
                    )
                    payment_history = student1.GetPaymentHistory()
                    if payment_history:
                        print("Payment History:")
                        for payment_record in payment_history:
                            print(
                                f"PaymentID: {payment_record[0]}, Amount: {payment_record[1]}, PaymentDate: {payment_record[2]}")
                    else:
                        print("No payment history available.")
                if k==8:
                    break
            if choice==2:
                print("COURSE MANAGEMENT")
                print("1.Add Course \n2.Update Course Info \n3.Display Course Info \n4.Get Enrollments \n5.Assign Teacher \n6.Get Teacher \n7.Stop")
                k=int(input("Enter choice:"))
                if k==1:
                    c = Course()
                    c.AddCourse(Course_ID=int(input("Course_ID")),
                                Course_Name=input("Course_Name"),
                                credits=input("credits"),
                                Teacher_Id=input("Teacher_Id"))
                if k==2:
                    c=Course()
                    c.UpdateCourseInfo()
                if k==3:
                    c=Course()
                    c.DisplayCourseInfo()
                if k==4:
                    c=Course()
                    c.GetEnrollments()
                if k==5:
                    c=Course()
                    c.AssignTeacher()
                if k==6:
                    c=Course()
                    c.GetTeacher()
                if k==7:
                    break
            if choice==3:
                print("ENROLLMENT MANAGEMENT")
                print("1.Get Student \n2.Get Course \n3.Enroll Student In Course \n4.Stop")
                s=int(input("Enter choice:"))
                if s==1:
                    e=Enrollment()
                    e.GetStudent()
                if s==2:
                    e=Enrollment()
                    e.GetCourse()
                if s==3:
                    e=Enrollment()
                    e.EnrollStudentInCourse(Student_ID=int(input("Student_ID")), Course_ID=int(input("Course_ID")))
                if s==4:
                    break
            if choice==4:
                print("TEACHER MANAGEMENT")
                print("1.Add Teacher \n2.Update Teacher Info \n3.Display Teacher Info \n4.Get Assigned Courses \n5.Assign Teacher to Course \n6.Stop")
                s=int(input("Enter choice:"))
                if s==1:
                    t = Teacher()
                    t.addTeacher(Teacher_ID=int(input("Teacher_ID:")),
                                 First_Name=input("First_Name:"),
                                 Last_Name=input("Last_Name:"),
                                 Email=input("Email:"))
                if s==2:
                    t=Teacher()
                    t.UpdateTeacherInfo()
                if s==3:
                    t=Teacher()
                    t.DisplayTeacherInfo()
                if s==4:
                    t=Teacher()
                    t.GetAssignedCourses()
                if s==5:
                    t=Teacher()
                    t.AssignTeacherToCourse(77,222)
                if s==6:
                    break
            if choice==5:
                print("PAYMENT MANAGEMENT")
                print("1.Add Payment \n2.Get STudent \n3.Get Payment Amount \n4.Get Payment Date \n5.Stop")
                s=int(input("Enter choice:"))
                if s==1:
                    p = Payment()
                    p.AddPayment(PaymentID=int(input("Payment ID")),
                                 Student_ID=int(input("Student ID")),
                                 Amount=input("Amount"),
                                 PaymentDate=input("Payment Date"))
                if s==2:
                    p=Payment()
                    p.GetStudent()
                if s==3:
                    p=Payment()
                    p.GetPaymentAmount()
                if s==4:
                    p=Payment()
                    p.GetPaymentDate()
                if s==5:
                    break
            if choice==6:
                break
    except Exception as e:
        print(e)


