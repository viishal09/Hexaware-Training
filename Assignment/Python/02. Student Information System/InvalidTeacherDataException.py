class InvalidTeacherDataException(Exception):
    def __init__(self,msg="Invalid Teacher Data"):
        super().__init__(self,msg)