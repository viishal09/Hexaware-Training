class CourseNotFoundException(Exception):
    def __init__(self,msg="Course not found."):
        self.msg=msg
        super().__init__(self.msg)
