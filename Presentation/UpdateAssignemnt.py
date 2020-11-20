# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UpdateAssignment.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class UpdateAssignment(object):
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.id_text = QtWidgets.QLineEdit(self.centralwidget)
        self.id_text.setText("")
        self.id_text.setObjectName("id_text")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.id_text)
        spacerItem = QtWidgets.QSpacerItem(40, 150, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.name_text = QtWidgets.QLineEdit(self.centralwidget)
        self.name_text.setObjectName("name_text")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.name_text)
        spacerItem1 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.group_text = QtWidgets.QLineEdit(self.centralwidget)
        self.group_text.setObjectName("group_text")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.group_text)
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
        self.label.setText(_translate("MainWindow", "Update a assignment by the id"))
        self.label_2.setText(_translate("MainWindow", "ID:"))
        self.label_3.setText(_translate("MainWindow", "New Description:"))
        self.label_4.setText(_translate("MainWindow", "New Deadline(yyyy-mm-dd):"))
        self.submit.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
