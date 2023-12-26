class StudentNotFoundException(Exception):
    def __init__(self,msg="Student is not found"):
        self.msg=msg
        super().__init__(self,msg)

