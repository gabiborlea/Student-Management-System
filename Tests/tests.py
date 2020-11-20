from Domain.student import Student
from Validations.validations import ValidationStudent, ValidationError, ValidationAssignment, ValidationGrade
from Infrastracture.repo import Repository, RepoError
from Business.services import ServiceStudents, ServiceAssignments
from Domain.assignment import Assignment
from datetime import date
from Domain.grade import Grade
import unittest
class Tests(unittest.TestCase):

    
    
    def _test_create_student(self):
        test_student = Student(10, "Iliescu Georgian", 911)
        self.assertEqual( test_student.get_student_id(),  10)
        assert test_student.get_group() == 911
        test_student.set_group(900)
        assert test_student.get_group() == 900
        self._stud_ok = test_student
        
    def _test_validate_student(self):
        valid_student = ValidationStudent()
        try:
            valid_student.validate_student(self._stud_ok)
            assert True
        except Exception:
            assert False
            
        self._stud_not_ok = Student(-11, "", -11)
        try:
            valid_student.validate_student(self._stud_not_ok)
            assert False
        except ValidationError as errors:
            assert str(errors) == "invalid id!\ninvalid name!\ninvalid group!\n"
            
    def _test_add_search_student(self):
        self._repo = Repository([])
        assert self._repo.size() == 0
        
        self._repo.add(self._stud_ok)
        assert self._repo.size() == 1
        
        student_key = Student(self._stud_ok.get_student_id(), None, None)
        found_student = self._repo.search(student_key)
        assert found_student.get_name() == self._stud_ok.get_name() 
        
        self._student_sameID = Student(10, "mircea", 987)
        try:
            self._repo.add(self._student_sameID)
            assert False
        except RepoError as error:
            assert str(error) == "id existent\n"
            
        self._another_student = Student(56, "Iliescu Horea", 976)
        try:
            self._repo.search(self._another_student)
            assert False
        except RepoError as error:
            assert str(error) == "id inexistent\n"
            
    def _test_remove_student(self):
        self._repo = Repository([])
        self._repo.add(Student(56, "Iliescu Horea", 976))
        assert self._repo.size() == 1
        self._repo.delete(Student(56, "Iliescu Horea", 976))
        assert self._repo.size() == 0
        
    def _test_update_student(self):
        self._repo = Repository([])
        self._repo.add(Student(56, "Iliescu Horea", 976))
        self._repo.update(Student(56, None, None), Student(56, 'Mihai', 911))
        assert self._repo.search(Student(56, None, None)).get_name() == 'Mihai'
        assert self._repo.search(Student(56, None, None)).get_group() == 911
            
            
    def _test_service_student(self):
        repo = Repository([])
        valid_student = ValidationStudent()
        self._serv_students = ServiceStudents(repo, valid_student)
        assert self._serv_students.get_nr_students() == 0
        
        #ADD
        self._serv_students.add_student(12, "Jecan Marius", 865)
        assert self._serv_students.get_nr_students() == 1
        
        found_student = self._serv_students.get_student_by_id(12)
        assert found_student.get_name() == "Jecan Marius"    
        
        try:
            self._serv_students.add_student(-12, "Ceva", 561)
            assert False
        except ValidationError as error:
            assert str(error) == "invalid id!\n"    
            
        try:
            self._serv_students.add_student(3, "", 812)
            assert False
        except ValidationError as error:
            assert str(error) == "invalid name!\n"
            
        try:
            self._serv_students.add_student(3, "Iliescu", -98)
            assert False
        except ValidationError as error:
            assert str(error) == "invalid group!\n"
            
        try:
            self._serv_students.add_student(12, "Marcel Pavel", 761)
            assert False
        except RepoError as error:
            assert str(error) == "id existent\n"
            
        #GET BY ID
        try:
            self._serv_students.get_student_by_id(90)
            assert False
        except RepoError as error:
            assert str(error) == "id inexistent\n"
            
        #DELETE
        assert self._serv_students.get_nr_students() == 1
        self._serv_students.delete_student(12) 
        assert self._serv_students.get_nr_students() == 0
        
        try:
            self._serv_students.delete_student(12) 
            assert False
        except RepoError as error:
            assert str(error) == "id inexistent\n"
            
        #UPDATE
        self._serv_students.add_student(33, "Iliescu", 912)
        stud = self._serv_students.get_student_by_id(33)
        assert stud.get_name() == "Iliescu"
        assert stud.get_group() == 912
        self._serv_students.update_student(33, "Marcel Pavel", 192)
        stud = self._serv_students.get_student_by_id(33)
        assert stud.get_name() == "Marcel Pavel"
        assert stud.get_group() == 192 
            
    def _test_create_assignment(self):
        test_assignment = Assignment(12, 'Ceva tema grea', date(2019, 12, 12))
        self._assignment_ok = test_assignment
        assert test_assignment.get_assignment_id() == 12
        
        test_assignment.set_description('Nimic nou')
        assert test_assignment.get_description() == 'Nimic nou'
        assert test_assignment.get_deadline().year == 2019
        assert test_assignment.get_deadline().month == 12
        assert test_assignment.get_deadline().day == 12
        test_assignment.set_deadline(date(2020, 11, 2))
        assert test_assignment.get_deadline().month == 11
        
    def _test_validate_assignment(self):
        validation_assignment = ValidationAssignment()
        
        validation_assignment.validate_assignment(self._assignment_ok)
        
        self._assignment_not_ok = Assignment(-11, 'Ceva', date(2022, 12, 2))
        try:
            validation_assignment.validate_assignment(self._assignment_not_ok)
            assert False
        except ValidationError as error:
            assert str(error) == "invalid id!\n"
        
        self._assignment_not_ok = Assignment(-11, "", date(2022, 12, 2))
        try:
            validation_assignment.validate_assignment(self._assignment_not_ok)
            assert False
        except ValidationError as error:
            assert str(error) == "invalid id!\ninvalid description!\n"
            
            
    def _test_add_search_assignment(self):
        self._repo = Repository([])
        assert self._repo.size() == 0
        
        self._repo.add(self._assignment_ok)
        assert self._repo.size() == 1
        
        key_assignment = Assignment(self._assignment_ok.get_assignment_id(), None, None)
        found_assignment = self._repo.search(key_assignment)
        
        assert found_assignment.get_description() == self._assignment_ok.get_description()
        
        assignment_same_id = Assignment(self._assignment_ok.get_assignment_id(), 'Ceva ', date(2022, 12, 2))
        try:
            self._repo.add(assignment_same_id)
            assert False
        except RepoError as error:
            assert str(error) == "id existent\n"
            
        another_assignment = Assignment(123, 'nu stiu', date(2022, 12, 2))
        try:
            self._repo.search(another_assignment)
            assert False
        except RepoError as error:
            assert str(error) == "id inexistent\n"
            
    def _test_remove_assignment(self):
        self._repo = Repository([])
        self._repo.add(Assignment(56, "Iliescu Horea", date(2019, 12, 1)))
        assert self._repo.size() == 1
        self._repo.delete(Assignment(56, "Iliescu Horea", date(2019, 12, 1)))
        assert self._repo.size() == 0
            
            
    def _test_service_assignment(self):
        repo = Repository([])
        valid_assigment = ValidationAssignment()
        self._serv_assignments = ServiceAssignments(repo, valid_assigment)
        
        assert self._serv_assignments.get_nr_assignements() == 0
        #ADD
        self._serv_assignments.add_assignment(123, 'Ceva fain', date(2019, 11, 30))
        assert self._serv_assignments.get_nr_assignements() == 1
        
        try:
            self._serv_assignments.add_assignment(123, 'Traeas', date(2019, 12, 1))
            assert False
        except RepoError as error:
            assert str(error) == "id existent\n"
            
        try:
            self._serv_assignments.add_assignment(-12, 'Tracs', date(2029, 1, 1))
            assert False
        except ValidationError as error:
            assert str(error) == "invalid id!\n"
            
            
        #DELETE
        
        assert self._serv_assignments.get_nr_assignements() == 1
        self._serv_assignments.delete_assignment(123) 
        assert self._serv_assignments.get_nr_assignements() == 0
        
        try:
            self._serv_assignments.delete_assignment(12) 
            assert False
        except RepoError as error:
            assert str(error) == "id inexistent\n"
            
        #UPDATE
        
        self._serv_assignments.add_assignment(33, "O scrisoare", date(2019, 11, 30))
        assignment = self._serv_assignments.get_assignment_by_id(33)
        assert assignment.get_description() == "O scrisoare"
        assert assignment.get_deadline() == date(2019, 11, 30)
        self._serv_assignments.update_assignment(33, "O scoala", date(2020, 12, 4))
        assignment = self._serv_assignments.get_assignment_by_id(33)
        assert assignment.get_description() == "O scoala"
        assert assignment.get_deadline() == date(2020, 12, 4)
            
        
    def _test_create_grade(self):
        test_grade = Grade(12, 45, 8)
        assert test_grade.get_assignment_id() == 45
        assert test_grade.get_student_id() == 12
        assert test_grade.get_grade() == 8
        
        
    def _test_validate_grade(self):
        ok_grade =  Grade(12, 45, 8)
        vld_grade = ValidationGrade()
        try:
            vld_grade.validate_grade(ok_grade)
        except ValidationError:
            assert False
        not_ok_grade = Grade(-1,-1,-1)
        try:
            vld_grade.validate_grade(not_ok_grade)
            assert False
        except ValidationError as error:
            assert str(error) == "invalid student id!\ninvalid assignment id!\ninvalid grade!\n"
            
    def _test_search_grade(self):
        self._repo = Repository([])
        assert self._repo.size() == 0
        self._repo.add(Grade(1,3,5))
        assert self._repo.size() == 1
        
        key_grade = Grade(1,3, None)
        found_grade = self._repo.search(key_grade)
        
        assert found_grade.get_grade() == 5
        
            
                    
if __name__ == '__main__':
    unittest.main()


    




