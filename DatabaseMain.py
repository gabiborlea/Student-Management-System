from Infrastracture.dbRepo import dbRepository
from Domain.student import Student
from Domain.assignment import Assignment
from Domain.grade import Grade
from Validations.validations import ValidationStudent, ValidationAssignment, ValidationGrade
from Business.services import ServiceStudents, ServiceAssignments, ServiceGrades, SeviceUndo
from Presentation.MainWindow import Ui_A
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "rootpassword",
    database = "assignment9db",

)
my_cursor = mydb.cursor()

def create_student(student_id, name, group):
    return Student(int(student_id), name, int(group))

def create_assignments(assignment_id, description, deadline):
    deadline = str(deadline)
    deadline = deadline.split('-')
    return Assignment(int(assignment_id), description, date(int(deadline[0]), int(deadline[1]), int(deadline[2])))

def create_grade(student_id, assignment_id, grade):
    return Grade(int(student_id), int(assignment_id), int(grade))

#my_cursor.execute("CREATE TABLE students (student_id INTEGER(10) PRIMARY KEY , name VARCHAR (10), group_nr INTEGER (10))")
#my_cursor.execute("CREATE TABLE assignments (assignment_id INTEGER(10) , description VARCHAR(255), deadline VARCHAR(255))")
#my_cursor.execute("CREATE TABLE grades (student_id INTEGER(10) , assignment_id INTEGER(10), grade INTEGER (10))")


valid_student = ValidationStudent()
valid_assignment = ValidationAssignment()
valid_grade = Vundo_service = ValidationGrade()

undo_service = SeviceUndo()
students_repo = dbRepository(mydb, my_cursor, 'students' , ['student_id', 'name', 'group_nr'], create_student)
assignments_repo = dbRepository(mydb, my_cursor, 'assignments', ['assignment_id', 'description', 'deadline'], create_assignments)
grade_repo = dbRepository(mydb, my_cursor, 'grades', ['student_id','assignment_id', 'grade'], create_grade)

undo_service = SeviceUndo()
students_service = ServiceStudents(undo_service, students_repo, grade_repo, valid_student)
assignments_service = ServiceAssignments(undo_service, assignments_repo, grade_repo, valid_assignment)
grades_service = ServiceGrades(undo_service, students_repo, assignments_repo, grade_repo, valid_grade)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    A =QtWidgets.QMainWindow()
    ui = Ui_A(students_service, assignments_service , grades_service, undo_service)
    ui.setupUi(A)
    A.show()
    sys.exit(app.exec_())
