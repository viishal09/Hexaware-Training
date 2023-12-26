class Enrollment:
    def __init__(self,Enrollment_ID,Student_ID,Course_ID,Enrollment_Date):
        self.Enrollment_ID=Enrollment_ID
        self.Student_ID=Student_ID
        self.Course_ID=Course_ID
        self.Enrollment_Date=Enrollment_Date
        print(f"Enrollment_ID={self.Enrollment_ID} \nStudent_ID={self.Student_ID} \nCourse_ID={self.Course_ID} \nEnrollment_Date:{self.Enrollment_Date}")

Enrollment(200,11,102,'2022-06-12')