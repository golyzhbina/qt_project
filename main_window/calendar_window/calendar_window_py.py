# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(506, 352)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 10, 471, 301))
        self.calendarWidget.setStyleSheet("font: 8pt \"Book Antiqua\";\n"
"gridline-color: rgb(0, 85, 255);")
        self.calendarWidget.setObjectName("calendarWidget")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 320, 245, 26))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit.setStyleSheet("font: 9pt \"Book Antiqua\";\n"
"")
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout.addWidget(self.dateEdit)
        self.pushButton_show = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_show.setStyleSheet("font: 9pt \"Book Antiqua\";\n"
"background-color: rgb(218, 218, 218);")
        self.pushButton_show.setObjectName("pushButton_show")
        self.horizontalLayout.addWidget(self.pushButton_show)
        self.pushButton_ok = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_ok.setStyleSheet("font: 9pt \"Book Antiqua\";\n"
"background-color: rgb(218, 218, 218);")
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout.addWidget(self.pushButton_ok)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_show.setText(_translate("Form", "Показать"))
        self.pushButton_ok.setText(_translate("Form", "Ок"))
