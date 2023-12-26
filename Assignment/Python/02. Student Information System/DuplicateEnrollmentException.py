class DuplicateEnrollmentException(Exception):
    def __init__(self, message="Student already enrolled"):
        self.message = message
        super().__init__(self.message)