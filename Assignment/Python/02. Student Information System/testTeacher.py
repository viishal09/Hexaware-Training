import unittest
from ConnUtil import dbConnection
from teacherdao import Teacher

class TestTeacherAddition(unittest.TestCase):
#Test case to find teacher added successfully or not
    def setUp(self):
        self.test_conn = dbConnection()
        self.test_conn.open()
    def test_addTeacher_successful(self):
        teacher = Teacher()
        teacher.conn = self.test_conn
    # Add a test teacher to the database
        teacher_id = 222
        teacher.addTeacher(teacher_id, "John", "Doe", "john.doe@example.com")
    # Check if the teacher is added successfully
        is_added = self.check_teacher_existence(teacher_id)
        self.assertTrue(is_added, f"Teacher with ID {teacher_id} should be added.")
    def check_teacher_existence(self, teacher_id):
        # Check if the teacher exists in the database
        teacher_instance = Teacher()
        teacher_instance.conn = self.test_conn
        return teacher_instance.teacherExists(teacher_id)
    def tearDown(self):
        self.test_conn.close()

if __name__ == '__main__':
    unittest.main()

