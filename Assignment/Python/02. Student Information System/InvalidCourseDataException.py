class InvalidCourseDataException(Exception):
    def __init__(self,msg="Inavalid Course Data"):
        super().__init__(msg)
        self.msg=msg


