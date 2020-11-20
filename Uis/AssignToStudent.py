# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AssignToStudent.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.id_assignment = QtWidgets.QLineEdit(self.centralwidget)
        self.id_assignment.setObjectName("id_assignment")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.id_assignment)
        spacerItem = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.id_student = QtWidgets.QLineEdit(self.centralwidget)
        self.id_student.setText("")
        self.id_student.setObjectName("id_student")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.id_student)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setObjectName("submit")
        self.verticalLayout_3.addWidget(self.submit, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Assign assignment to a student"))
        self.label_3.setText(_translate("MainWindow", "Assignment\'s Id:"))
        self.label_2.setText(_translate("MainWindow", "Student\'s Id:"))
        self.submit.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
