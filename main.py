from Domain.student import Student
from Domain.assignment import Assignment
from Domain.grade import Grade
from Validations.validations import ValidationStudent, ValidationAssignment, ValidationGrade
from Infrastracture.repo import Repository, RepoError
from Infrastracture.textRepo import TextRepository
from Infrastracture.binaryRepo import BinaryRepository
from Infrastracture.jsonRepo import JsonRepository
from Business.services import ServiceStudents, ServiceAssignments, ServiceGrades, SeviceUndo
from Presentation.ui import UI
from Presentation.MainWindow import Ui_A
from PyQt5 import QtCore, QtGui, QtWidgets
from _datetime import date
import random
from configparser import ConfigParser
from Infrastracture.dbRepo import dbRepository


class InitializeStudents:
    def __init__(self, Names, Groups):
        self._init_students = []
        self._names = Names
        self._groups = Groups
        
    def generate(self):
        for i in range(1, 11):
            name = random.choice(self._names)
            self._names.remove(name)
            group = random.choice(self._groups)
            stud = Student(i, name, group)
            self._init_students.append(stud)
            
    def get_list(self):
        return self._init_students
    
class InitializeAssignments:
    def __init__(self, Descriptions, Deadlines):
        self._init_assignments = []
        self._descriptions = Descriptions
        self._deadlines = Deadlines
        
    def generate(self):
        for i in range(1, 11):
            description = random.choice(self._descriptions)
            self._descriptions.remove(description)
            deadline = random.choice(self._deadlines)
            assign = Assignment(i, description, deadline)
            self._init_assignments.append(assign)
            
    def get_list(self):
        return self._init_assignments 
            
Names = ['Mihai', 'Paul', 'Iustin', 'Falviu', 'Sergiu', 'Tudor', 'Marcel', 'Ion', 'Tudose', 'Nimeni']
Groups = [911, 901, 912, 913, 911, 901, 911, 913, 916, 913]

Descriptions = ['Game with pirates', 'Calculator with sinus', 'Andorid game', 'Calendar', 'IOS game', 'Python app', 'Game with barbie', 'IOS plane game', 'Assignment 06-08', 'Games']
Deadlines = [date(2019, 12, 1), date(2019, 12, 1), date(2019, 12, 1), date(2019, 12, 1), date(2019, 12, 1), date(2019, 12, 1), date(2019, 12, 1), date(2019, 12, 1), date(2019, 12, 1), date(2019, 12, 1)]

stud_list = InitializeStudents(Names, Groups)
stud_list.generate()

assignments_list = InitializeAssignments(Descriptions, Deadlines)
assignments_list.generate()

valid_student = ValidationStudent()
valid_assignment = ValidationAssignment()
valid_grade = ValidationGrade()

def create_student(student_id, name, group):
    return Student(int(student_id), name, int(group))

def create_assignment(assignment_id, description, deadline):
    deadline = str(deadline)
    deadline = deadline.split('-')
    return Assignment(int(assignment_id), description, date(int(deadline[0]), int(deadline[1]), int(deadline[2])))

def create_grade(student_id, assignment_id, grade):
    return Grade(int(student_id), int(assignment_id), int(grade))





parser = ConfigParser()
parser.read("settings.properties")
repository = parser.get('settings', 'repository')
students = parser.get('settings', 'students')
assignments = parser.get('settings', 'assignments')
grades = parser.get('settings', 'grades')
ui = parser.get('settings', 'ui')

if repository == 'inmemory':
    students_repo = Repository(stud_list.get_list())
    assignments_repo = Repository(assignments_list.get_list())
    grade_repo = Repository([Grade(1, 1, 0), Grade(1, 2, 5), Grade(2, 1, 10)])


elif repository == 'textfile':
    students_repo = TextRepository(students, create_student, [])
    assignments_repo = TextRepository(assignments, create_assignment, [])
    grade_repo = TextRepository(grades, create_grade,  [])

elif repository == 'binaryfile':
    students_repo = BinaryRepository(students, [])
    assignments_repo = BinaryRepository(assignments, [])
    grade_repo = BinaryRepository(grades, [])

elif repository == 'json':
    students_repo = JsonRepository(students, create_student, [], ["student_id", "name", "group"])
    assignments_repo = JsonRepository(assignments, create_assignment, [], ["assignment_id", "description", "deadline"])
    grade_repo = JsonRepository(grades, create_grade, [], ["student_id", "assignment_id", "grade"])

undo_service = SeviceUndo()
students_service = ServiceStudents(undo_service, students_repo, grade_repo, valid_student)
assignments_service = ServiceAssignments(undo_service, assignments_repo, grade_repo, valid_assignment)
grades_service = ServiceGrades(undo_service, students_repo, assignments_repo, grade_repo, valid_grade)

if ui == "UI":
    ui = UI(students_service, assignments_service , grades_service, undo_service)
    ui.start()

if ui == "GUI":
    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        A =QtWidgets.QMainWindow()
        ui = Ui_A(students_service, assignments_service , grades_service, undo_service)
        ui.setupUi(A)
        A.show()
        sys.exit(app.exec_())




