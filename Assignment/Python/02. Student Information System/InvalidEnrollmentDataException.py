class InvalidEnrollmentDataException(Exception):
    def __init__(self,msg="Inavalid Enrollment Data"):
        super().__init__(msg)
        self.msg=msg