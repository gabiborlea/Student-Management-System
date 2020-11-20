import unittest
from Domain.student import Student
from Domain.assignment import Assignment
from Domain.grade import Grade
from datetime import date
from Validations.validations import ValidationStudent, ValidationError,\
    ValidationAssignment, ValidationGrade
from Infrastracture.repo import Repository
from Business.services import ServiceStudents, ServiceAssignments, ServiceGrades
class StudentTests(unittest.TestCase):
    
    def elems(self):
        self._valid_student = ValidationStudent()
        self._repo_students = Repository([])
        self._studService = ServiceStudents(self._repo_students, self._valid_student)
    
    def test_create_student(self):
        test_student = Student(1, 'Mircea', 911)
        self.assertEqual(test_student.get_student_id(), 1)
        self.assertEqual(test_student.get_name(), 'Mircea')
        test_student.set_name('Iusti')
        self.assertEqual(test_student.get_name(), 'Iusti')
        
    def test_validate_student(self):
        
        ok_student = Student(1, 'Mircea', 911)
        not_ok_student = Student(-1, 'Mircea', 911)
        self.elems()
        
        self._valid_student.validate_student(ok_student)
        
        with self.assertRaises(ValidationError):
            self._valid_student.validate_student(not_ok_student)
            
        not_ok_student = Student(-1, '', 911)
        try:
            self._valid_student.validate_student(not_ok_student)
            self.assertTrue(False)
        except ValidationError as error:
            self.assertEqual(str(error), "invalid id!\ninvalid name!\n")
        except Exception:
            self.assertTrue(False)
        
        not_ok_student = Student(-1, '', -911)
        try:
            self._valid_student.validate_student(not_ok_student)
            self.assertTrue(False)
        except ValidationError as error:
            self.assertEqual(str(error), "invalid id!\ninvalid name!\ninvalid group!\n")
        except Exception:
            self.assertTrue(False)


class AssignmentTests(unittest.TestCase):
    
    def elems(self):
        self._valid_assignment = ValidationAssignment()
        self._repo_assignments = Repository([])
        self._assignmentService = ServiceAssignments(self._repo_assignments, self._valid_assignment)
    
    def test_create_assignment(self):
        test_assignment = Assignment(12, 'Homework', date(2019, 12, 1))
        self.assertEqual(test_assignment.get_assignment_id(),12)
        self.assertEqual(test_assignment.get_deadline(), date(2019, 12, 1))  
        test_assignment.set_description('Project')
        self.assertEqual(test_assignment.get_description(), 'Project' )
        
    def test_validate_assignment(self):
        
        ok_assignment = Assignment(12, 'Homework', date(2019, 12, 1))
        not_ok_assignment = Assignment(12, '', date(2010,1,1))
        self.elems()
        
        self._valid_assignment.validate_assignment(ok_assignment)
        
        try:
            self._valid_assignment.validate_assignment(not_ok_assignment)
            self.assertTrue(False)
        except ValidationError as error:
            self.assertEqual(str(error), "invalid description!\n" )
        except Exception:
            self.assertTrue(False)
            
        not_ok_assignment = Assignment(-12, '', date(2010,1,1))
        try:
            self._valid_assignment.validate_assignment(not_ok_assignment)
            self.assertTrue(False)
        except ValidationError as error:
            self.assertEqual(str(error), "invalid id!\ninvalid description!\n" )
        except Exception:
            self.assertTrue(False)
            
            
class GradeTests(unittest.TestCase):
    
    def elems(self):
        self._valid_grade = ValidationGrade()
        self._repo_grades = Repository([])
        self._repo_students = Repository([])
        self._repo_assignments = Repository([])
        self._gradeService = ServiceGrades(self._repo_students, self._repo_assignments, self._repo_grades, self._valid_grade)
    
    def test_create_grade(self):
        test_grade = Grade(1,2, 9)
        self.assertEqual(test_grade.get_student_id(), 1)
        self.assertEqual(test_grade.get_assignment_id(), 2)
        test_grade.set_grade(6)
        self.assertEqual(test_grade.get_grade(), 6)
        
    def test_validate_grade(self):
        
        ok_grade = Grade(1,2, 9)
        not_ok_grade = Grade(-1, 2, 9)
        self.elems()
        
        self._valid_grade.validate_grade(ok_grade)
        
        try:
            self._valid_grade.validate_grade(not_ok_grade)
            self.assertTrue(False)
        except ValidationError as error:
            self.assertEqual(str(error), "invalid student id!\n")
        except Exception:
            self.assertTrue(False)
            
        not_ok_grade = Grade(-1, -2, 9)
        try:
            self._valid_grade.validate_grade(not_ok_grade)
            self.assertTrue(False)
        except ValidationError as error:
            self.assertEqual(str(error), "invalid student id!\ninvalid assignment id!\n")
        except Exception:
            self.assertTrue(False)

        
         



