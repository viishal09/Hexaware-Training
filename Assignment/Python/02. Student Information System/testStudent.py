import unittest
from ConnUtil import dbConnection
from Studentdao import Students

class TestStudentEnrollment(unittest.TestCase):
    def setUp(self):
        self.test_conn = dbConnection()
        self.test_conn.open()
# Testcase to find student is added properly or not
    def test_studentEnrollment(self):
        student = Students()
        student.conn = self.test_conn
        student_id = 1010
        student.addStudent(student_id, "John", "Doe", "2000-01-01", "john.doe@example.com", "123456789")
        is_enrolled = student.studentExists(student_id)
        self.assertTrue(is_enrolled, f"Student with ID {student_id} should be enrolled.")
    def tearDown(self):
        self.test_conn.close()
if __name__ == '__main__':
    unittest.main()
