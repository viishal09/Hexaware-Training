class InvalidStudentDataException(Exception):
    def __init__(self,msg="Invalid Student Data"):
        super().__init__(self,msg)