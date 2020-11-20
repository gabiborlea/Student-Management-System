# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Presentation.StudentsWindow import StudentsWindow
from Presentation.AssignmentsWindow import AssignmentsWindow
from Presentation.GradesWindow import GradesWindow
from Presentation.StatisticsWindow import StatisticsWindow
from Presentation.AddNewStudent import AddStudent
from Presentation.DeleteStudent import DeleteStudent
from Presentation.ShowStudents import ShowStudents
from Presentation.UpdateStudent import UpdateStudent
from Presentation.AddAssignemnt import AddAssignment
from Presentation.DeleteAssignment import DeleteAssignment
from Presentation.UpdateAssignemnt import UpdateAssignment
from Presentation.AssignToStudent import AssignToStudent
from Presentation.AssignToGroup import AssignToGroup
from Presentation.GradeStudent import GradeStudent
from Presentation.AllAssign import AllAssign

from Infrastracture.repo import RepoError
from datetime import date

class Ui_A(object):

    def __init__(self, servStudents, servAssignments, servGrades, servUndo):
        self._servStudents = servStudents
        self._servAssignments = servAssignments
        self._servGrades = servGrades
        self._servUndo = servUndo

    def setupUi(self, A):
        A.setObjectName("A")
        A.resize(803, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(A.sizePolicy().hasHeightForWidth())
        A.setSizePolicy(sizePolicy)
        A.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(A)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.btn_student = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_student.sizePolicy().hasHeightForWidth())
        self.btn_student.setSizePolicy(sizePolicy)
        self.btn_student.setBaseSize(QtCore.QSize(0, 0))
        self.btn_student.setObjectName("btn_student")
        self.verticalLayout.addWidget(self.btn_student)
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.btn_assignment = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_assignment.sizePolicy().hasHeightForWidth())
        self.btn_assignment.setSizePolicy(sizePolicy)
        self.btn_assignment.setObjectName("btn_assignment")
        self.verticalLayout.addWidget(self.btn_assignment)
        spacerItem3 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem3)
        self.btn_grade = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_grade.sizePolicy().hasHeightForWidth())
        self.btn_grade.setSizePolicy(sizePolicy)
        self.btn_grade.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_grade.setObjectName("btn_grade")
        self.verticalLayout.addWidget(self.btn_grade)
        spacerItem4 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.btn_statistic = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_statistic.sizePolicy().hasHeightForWidth())
        self.btn_statistic.setSizePolicy(sizePolicy)
        self.btn_statistic.setObjectName("btn_statistic")
        self.verticalLayout.addWidget(self.btn_statistic)
        spacerItem5 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem5)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        A.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(A)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 22))
        self.menubar.setObjectName("menubar")
        A.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(A)
        self.statusbar.setObjectName("statusbar")
        A.setStatusBar(self.statusbar)

        self.retranslateUi(A)
        QtCore.QMetaObject.connectSlotsByName(A)

    def messagebox(self,title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()



    def retranslateUi(self, A):
        _translate = QtCore.QCoreApplication.translate
        A.setWindowTitle(_translate("A", "MainWindow"))
        self.label.setText(_translate("A", "Choose the object that you want to work with:"))
        self.btn_student.setText(_translate("A", "Student"))
        self.btn_assignment.setText(_translate("A", "Assignemnt"))
        self.btn_grade.setText(_translate("A", "Grade"))
        self.btn_statistic.setText(_translate("A", "Statistic"))
        self.pushButton.setText(_translate("A", "Exit"))
        self.windows_init()
        self.Main_buttons()
        self.A = A


    def windows_init(self):
        self.students_window = StudentsWindow()

        self.assignments_window = AssignmentsWindow()

        self.grades_window = GradesWindow()

        self.statistics_window = StatisticsWindow()

        self.add_student_window = AddStudent()

        self.show_stud = ShowStudents()

        self.delete_stud = DeleteStudent()

        self.update_stud = UpdateStudent()

        self.add_assign = AddAssignment()

        self.delete_assign = DeleteAssignment()

        self.update_assign = UpdateAssignment()

        self.assign_to_stud = AssignToStudent()

        self.assign_to_group = AssignToGroup()

        self.grade_stud = GradeStudent()

        self.all_assign = AllAssign()

        self.window = QtWidgets.QMainWindow()

        self.window2 = QtWidgets.QMainWindow()

    def Main_buttons(self):
        self.btn_student.clicked.connect(self.show_students_window)
        self.btn_assignment.clicked.connect(self.show_assignemnts_window)
        self.btn_grade.clicked.connect(self.show_grades_window)
        self.btn_statistic.clicked.connect(self.show_statistics_window)
        self.pushButton.clicked.connect(self.exit)


    def show_students_window(self):
        self.students_window.setupUi(self.window)

        self.students_window.back.clicked.connect(self.back)
        self.students_window.add_student.clicked.connect(self.show_add_student_window)
        self.students_window.show_students.clicked.connect(self.students_list)
        self.students_window.delete_student.clicked.connect(self.gui_delete_student)
        self.students_window.update_student.clicked.connect(self.gui_update_student)

        self.students_window.undo.clicked.connect(self.undo)
        self.students_window.redo.clicked.connect(self.redo)

        self.A.hide()
        self.window.show()

    def show_assignemnts_window(self):
        self.assignments_window.setupUi(self.window)

        self.assignments_window.back.clicked.connect(self.back)
        self.assignments_window.add_assignemnt.clicked.connect(self.gui_add_assignment)
        self.assignments_window.show_assignemnts.clicked.connect(self.gui_show_assignments)
        self.assignments_window.delete_assignment.clicked.connect(self.gui_delete_assignment)
        self.assignments_window.update_assignment.clicked.connect(self.gui_update_assignment)

        self.assignments_window.undo.clicked.connect(self.undo)
        self.assignments_window.redo.clicked.connect(self.redo)

        self.A.hide()
        self.window.show()

    def show_grades_window(self):
        self.grades_window.setupUi(self.window)

        self.grades_window.back.clicked.connect(self.back)
        self.grades_window.assign_student.clicked.connect(self.gui_assign_student)
        self.grades_window.assign_group.clicked.connect(self.gui_assign_group)
        self.grades_window.show_grades.clicked.connect(self.gui_show_grades)
        self.grades_window.grade_student.clicked.connect(self.gui_grade_student)

        self.grades_window.undo.clicked.connect(self.undo)
        self.grades_window.redo.clicked.connect(self.redo)

        self.A.hide()
        self.window.show()

    def show_statistics_window(self):
        self.statistics_window.setupUi(self.window)

        self.statistics_window.back.clicked.connect(self.back)
        self.statistics_window.all_assignemnt.clicked.connect(self.gui_all_assign)
        self.statistics_window.all_late.clicked.connect(self.gui_all_late)
        self.statistics_window.best_students.clicked.connect(self.gui_best_students)

        self.A.hide()
        self.window.show()

    def exit(self):
        QtCore.QCoreApplication.instance().quit()

    def back(self):
        self.window.hide()
        self.A.show()

    def back2(self):
        self.window2.hide()
        self.window.show()

    def add_student_submit(self):
        student_id = self.add_student_window.id_text.text()
        name = self.add_student_window.name_text.text()
        group = self.add_student_window.group_text.text()
        errors = ""

        try:
            student_id = int(student_id)
        except ValueError:
            errors += "Invalid id!\n"

        try:
            group = int(group)
        except ValueError:
            errors += "Invald group\n"

        if len(errors) == 0:
            try:
                self._servStudents.add_student(student_id, name, group)
            except Exception as error:
                self.messagebox("Error", str(error))
        else:
            self.messagebox("Error", str(errors))

        self.window2.hide()
        self.window.show()


    def show_add_student_window(self):
        self.add_student_window.setupUi(self.window2)
        self.add_student_window.submit.clicked.connect(self.add_student_submit)
        self.window.hide()
        self.window2.show()

    def students_list(self):
        self.show_stud.setupUi(self.window2)
        _translate = QtCore.QCoreApplication.translate
        self.show_stud.label.setText(_translate("MainWindow", "The list of students"))
        self.window.hide()
        self.window2.show()
        for student in self._servStudents.get_students():
            self.show_stud.listWidget.addItem(str(student))

        self.show_stud.back.clicked.connect(self.back2)

    def gui_delete_student(self):
        self.delete_stud.setupUi(self.window2)
        self.delete_stud.delete_2.clicked.connect(self.del_stud)
        self.window.hide()
        self.window2.show()

    def del_stud(self):
        studentID = self.delete_stud.id_text.text()
        errors = ""
        try:
            studentID = int(studentID)
        except ValueError:
            errors += "invalid id\n"

        if len(errors) == 0:
            try:
                student = self._servStudents.get_student_by_id(studentID)
                self.messagebox("Warning", "Delete " + str(student) )
                self._servStudents.delete_student(studentID)

            except RepoError as error:
                self.messagebox("RepoError", str(error))
        else:
            self.messagebox("Errors", str(errors))

        self.window2.hide()
        self.window.show()

    def gui_update_student(self):
        self.update_stud.setupUi(self.window2)
        self.update_stud.submit.clicked.connect(self.ui_update_student)
        self.window.hide()
        self.window2.show()

    def ui_update_student(self):
        studentID = self.update_stud.id_text.text()
        name = self.update_stud.name_text.text()
        group = self.update_stud.group_text.text()
        errors = ""
        try:
            studentID = int(studentID)
        except ValueError:
            errors += "invalid id\n"

        if len(errors) == 0:
            try:
                student = self._servStudents.get_student_by_id(studentID)
                self.messagebox("Warning", "Update " + str(student))
                name = name
                group = int(group)
                self._servStudents.update_student(studentID, name, group)

            except ValueError:
                self.messagebox("Error" , "Invalid group")
            except Exception as error:
                self.messagebox("Error", str(error))
        else:
            self.messagebox("Errors", str(errors))

        self.window2.hide()
        self.window.show()

    def gui_add_assignment(self):
        self.add_assign.setupUi(self.window2)
        self.add_assign.submit.clicked.connect(self.ui_add_assignment)
        self.window.hide()
        self.window2.show()

    def ui_add_assignment(self):
        assignmentID = self.add_assign.id_text.text()
        description = self.add_assign.name_text.text()
        deadl = self.add_assign.group_text.text()
        deadl = deadl.split('-')

        errors = ""

        if len(deadl) == 3:
            try:
                year = int(deadl[0])
                month = int(deadl[1])
                day = int(deadl[2])
                deadline = date(year, month, day)
            except ValueError:
                errors += "invalid deadline\n"

        else:
            errors += "invalid deadline\n"

        try:
            assignmentID = int(assignmentID)
        except ValueError:
            errors += "invalid id\n"

        if len(errors) == 0:
            try:
                self._servAssignments.add_assignment(assignmentID, description, deadline)
            except Exception as error:
                self.messagebox("Error", str(error))
        else:
            self.messagebox("Errors", str(errors))

        self.window2.hide()
        self.window.show()

    def gui_show_assignments(self):
        self.show_stud.setupUi(self.window2)
        _translate = QtCore.QCoreApplication.translate
        self.show_stud.label.setText(_translate("MainWindow", "The list of assignments"))
        self.window.hide()
        self.window2.show()
        for assignment in self._servAssignments.get_assignments():
            self.show_stud.listWidget.addItem(str(assignment))

            self.show_stud.back.clicked.connect(self.back2)

    def gui_delete_assignment(self):
        self.delete_assign.setupUi(self.window2)
        self.delete_assign.delete_2.clicked.connect(self.ui_delete_assignment)
        self.window.hide()
        self.window2.show()

    def ui_delete_assignment(self):
        assignmentID = self.delete_assign.id_text.text()
        errors = ""
        try:
            assignmentID = int(assignmentID)
        except ValueError:
            errors += "invalid id\n"

        if len(errors) == 0:
            try:
                assignment = self._servAssignments.get_assignment_by_id(assignmentID)
                self.messagebox("Warning", "Delete " + str(assignment))
                self._servAssignments.delete_assignment(assignmentID)

            except RepoError as error:
                self.messagebox("RepoError", str(error))
        else:
            self.messagebox("Errors", str(errors))

        self.window2.hide()
        self.window.show()

    def gui_update_assignment(self):
        self.update_assign.setupUi(self.window2)
        self.update_assign.submit.clicked.connect(self.ui_update_assignment)
        self.window.hide()
        self.window2.show()

    def ui_update_assignment(self):
        assignmentID = self.update_assign.id_text.text()
        description = self.update_assign.name_text.text()
        deadl = self.update_assign.group_text.text()
        errors = ""
        try:
            assignmentID = int(assignmentID)
        except ValueError:
            errors += "invalid id\n"

        if len(errors) == 0:
            try:
                assignment = self._servAssignments.get_assignment_by_id(assignmentID)
                self.messagebox("Warning", "update " + str(assignment))
                deadl = deadl.split('-')

                if len(deadl) == 3:
                    year = int(deadl[0])
                    month = int(deadl[1])
                    day = int(deadl[2])
                    deadline = date(year, month, day)
                    self._servAssignments.update_assignment(assignmentID, description, deadline)

                else:
                    raise ValueError

            except ValueError:
                self.messagebox("ValueError","Invalid deadline\n")
            except Exception as error:
                self.messagebox("Error", str(error))
        else:
            self.messagebox("Errors", str(errors))
        self.window2.hide()
        self.window.show()

    def gui_assign_student(self):
        self.assign_to_stud.setupUi(self.window2)
        self.assign_to_stud.submit.clicked.connect(self.ui_assign_student)
        self.window.hide()
        self.window2.show()

    def ui_assign_student(self):
        assignmentID = self.assign_to_stud.id_assignment.text()
        studentID = self.assign_to_stud.id_student.text()
        try:
            assignmentID = int(assignmentID)
            studentID = int(studentID)
            self._servStudents.get_student_by_id(studentID)
            self._servAssignments.get_assignment_by_id(assignmentID)
            self._servGrades.assign_assignment_to_student(assignmentID, studentID)

        except ValueError:
            self.messagebox("ValueError", "Invalid inputs")

        except Exception as error:
            self.messagebox("Error", str(error))

        self.window2.hide()
        self.window.show()

    def gui_assign_group(self):
        self.assign_to_group.setupUi(self.window2)
        self.assign_to_group.submit.clicked.connect(self.ui_assign_group)

        self.window.hide()
        self.window2.show()

    def ui_assign_group(self):
        assignmentID = self.assign_to_group.id_assignment.text()
        group = self.assign_to_group.group.text()
        try:
            assignmentID = int(assignmentID)
            group = int(group)
            self._servAssignments.get_assignment_by_id(assignmentID)
            self._servGrades.assign_assignment_to_group(group, assignmentID, self._servStudents)

        except ValueError:
            self.messagebox("ValueError","Invalid inputs\n")

        except Exception as error:
            self.messagebox("Error", str(error))

        self.window2.hide()
        self.window.show()

    def gui_show_grades(self):
        self.show_stud.setupUi(self.window2)
        _translate = QtCore.QCoreApplication.translate
        self.show_stud.label.setText(_translate("MainWindow", "The list of grades"))
        self.window.hide()
        self.window2.show()
        for grade in self._servGrades.get_all_grades():
            self.show_stud.listWidget.addItem(str(grade))

        self.show_stud.back.clicked.connect(self.back2)

    def gui_grade_student(self):
        self.grade_stud.setupUi(self.window2)
        self.grade_stud.submit1.clicked.connect(self.ui_grade_student)
        self.grade_stud.back.clicked.connect(self.back2)
        self.window.hide()
        self.window2.show()

    def ui_grade_student(self):
        studentID = self.grade_stud.id_student.text()
        try:
            studentID = int(studentID)
            the_student = self._servStudents.get_student_by_id(studentID)
            self.messagebox("Warning", "The student is: " + str(the_student))

            for assignmentID in self._servGrades.get_graded(studentID):
                self.grade_stud.listWidget.addItem(str(self._servAssignments.get_assignment_by_id(assignmentID)))

            for assignmentID in self._servGrades.get_ungraded(studentID):
                self.grade_stud.listWidget_2.addItem(str(self._servAssignments.get_assignment_by_id(assignmentID)))

            self.grade_stud.submit2.clicked.connect(self.ui_grade_student_2)

        except ValueError:
            self.messagebox("ValueError", "Invalid id!")
        except RepoError as error:
            self.messagebox("RepoError", str(error))
        except Exception as error:
            self.messagebox("Error", str(error))


    def ui_grade_student_2(self):
        assignmentID = self.grade_stud.id_assignment.text()
        grade = self.grade_stud.grade.text()
        try:
            assignmentID = int(assignmentID)
            grade = int(grade)
            self._servGrades.update_grade(int(self.grade_stud.id_student.text()), int(assignmentID), int(grade))

        except ValueError:
            self.messagebox("ValueError", "invalid id\n")
        except RepoError as error:
            self.messagebox("RepoError", str(error))

        except Exception as error:
            self.messagebox("Error", str(error))
        self.window2.hide()
        self.window.show()

    def gui_all_assign(self):
        self.all_assign.setupUi(self.window2)
        self.all_assign.submit1.clicked.connect(self.ui_all_assign)
        self.window.hide()
        self.window2.show()

    def ui_all_assign(self):
        assignmentID = self.all_assign.id_assignment.text()
        try:
            assignmentID = int(assignmentID)
            the_assignment = self._servAssignments.get_assignment_by_id(assignmentID)
            self.messagebox("Warning", "The assignment: " + str(the_assignment))
            the_list = self._servGrades.get_students_by_assignment(assignmentID)
            for grade in the_list:
                self.all_assign.listWidget.addItem(str(self._servStudents.get_student_by_id(grade.get_student_id())) + "| grade: " + str(
                    grade.get_grade()))

        except ValueError:
            self.messagebox("ValueError","Invalid Id")
        except RepoError as error:
            self.messagebox("RepoError", str(error))

        self.all_assign.back.clicked.connect(self.back2)

    def gui_all_late(self):
        self.show_stud.setupUi(self.window2)
        _translate = QtCore.QCoreApplication.translate
        self.show_stud.label.setText(_translate("MainWindow", "All students who are late in handing in at least one assignment"))
        self.window.hide()
        self.window2.show()
        stud_list = self._servGrades.dead_line_passed()
        for student in stud_list:
            self.show_stud.listWidget.addItem(str(self._servStudents.get_student_by_id(student[0]))+"  "+str(self._servAssignments.get_assignment_by_id(student[1]).get_deadline()))

        self.show_stud.back.clicked.connect(self.back2)

    def gui_best_students(self):
        self.show_stud.setupUi(self.window2)
        _translate = QtCore.QCoreApplication.translate
        self.show_stud.label.setText(_translate("MainWindow", "Students with the best school situation"))
        self.window.hide()
        self.window2.show()
        students_list = self._servGrades.best_students()
        for student in students_list:
            self.show_stud.listWidget.addItem(str(self._servStudents.get_student_by_id(student[0])) + "| avg: " + str(student[1]))

        self.show_stud.back.clicked.connect(self.back2)

    def undo(self):
        try:
            self._servUndo.undo()
        except Exception as error:
            self.messagebox("Error", str(error))

    def redo(self):
        try:
            self._servUndo.redo()
        except Exception as error:
            self.messagebox("Error", str(error))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    A = QtWidgets.QMainWindow()
    ui = Ui_A()
    ui.setupUi(A)
    A.show()
    sys.exit(app.exec_())