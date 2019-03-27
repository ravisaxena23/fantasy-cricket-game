# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate_teams.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_evaluate_window(object):
    def setupUi(self, evaluate_window):
        evaluate_window.setObjectName("evaluate_window")
        evaluate_window.resize(647, 556)
        evaluate_window.setStyleSheet("                        background-color: rgb(66,66,66);\n"
"")
        self.centralwidget = QtWidgets.QWidget(evaluate_window)
        self.centralwidget.setObjectName("centralwidget")
        self.team_2 = QtWidgets.QListView(self.centralwidget)
        self.team_2.setGeometry(QtCore.QRect(20, 110, 261, 351))
        self.team_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.team_2.setObjectName("team_2")
        self.team_1 = QtWidgets.QListView(self.centralwidget)
        self.team_1.setGeometry(QtCore.QRect(360, 110, 261, 351))
        self.team_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.team_1.setObjectName("team_1")
        self.columnView = QtWidgets.QColumnView(self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(20, 70, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.columnView.setFont(font)
        self.columnView.setStyleSheet("background-color: rgb(63, 81, 181);")
        self.columnView.setObjectName("columnView")
        self.columnView_2 = QtWidgets.QColumnView(self.centralwidget)
        self.columnView_2.setGeometry(QtCore.QRect(360, 70, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.columnView_2.setFont(font)
        self.columnView_2.setStyleSheet("background-color: rgb(63, 81, 181);")
        self.columnView_2.setObjectName("columnView_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 80, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"                        background-color: rgb(63, 81, 181);\n"
"                    ")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 80, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"                        background-color: rgb(63, 81, 181);\n"
"                    ")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 20, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"                        background-color: rgb(66,66,66);\n"
"                    ")
        self.label_3.setObjectName("label_3")
        self.evaluate_push = QtWidgets.QPushButton(self.centralwidget)
        self.evaluate_push.setGeometry(QtCore.QRect(270, 480, 101, 23))
        self.evaluate_push.setStyleSheet("color: rgb(255, 255, 255);")
        self.evaluate_push.setObjectName("evaluate_push")
        evaluate_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(evaluate_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 647, 20))
        self.menubar.setObjectName("menubar")
        evaluate_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(evaluate_window)
        self.statusbar.setObjectName("statusbar")
        evaluate_window.setStatusBar(self.statusbar)

        self.retranslateUi(evaluate_window)
        QtCore.QMetaObject.connectSlotsByName(evaluate_window)

    def retranslateUi(self, evaluate_window):
        _translate = QtCore.QCoreApplication.translate
        evaluate_window.setWindowTitle(_translate("evaluate_window", "MainWindow"))
        self.label.setText(_translate("evaluate_window", "Team 1"))
        self.label_2.setText(_translate("evaluate_window", "Team 2"))
        self.label_3.setText(_translate("evaluate_window", "EVALUATE TEAMS"))
        self.evaluate_push.setText(_translate("evaluate_window", "EVALUATE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    evaluate_window = QtWidgets.QMainWindow()
    ui = Ui_evaluate_window()
    ui.setupUi(evaluate_window)
    evaluate_window.show()
    sys.exit(app.exec_())

