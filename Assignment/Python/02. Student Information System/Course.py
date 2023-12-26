class Course:
    def __init__(self,CourseID,CourseName,Credits,Teacher_Id):
        self.CourseID=CourseID
        self.CourseName=CourseName
        self.Credits=Credits
        self.Teacher_Id=Teacher_Id
        print(f'Course ID:{self.CourseID} \nCourse Name:{self.CourseName} \nCredits:{self.Credits} \nInstructor Name:{self.Teacher_Id}')


Course(100,"Java",'J100','Sara')