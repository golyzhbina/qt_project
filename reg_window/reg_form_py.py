# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reg_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(280, 602)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 120, 251, 49))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_keyword = QtWidgets.QLabel(self.layoutWidget)
        self.label_keyword.setStyleSheet("font: 10pt \"Book Antiqua\";")
        self.label_keyword.setObjectName("label_keyword")
        self.verticalLayout_2.addWidget(self.label_keyword)
        self.lineEdit_keyword = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_keyword.setStyleSheet("font: 10pt \"Book Antiqua\";")
        self.lineEdit_keyword.setObjectName("lineEdit_keywod")
        self.verticalLayout_2.addWidget(self.lineEdit_keyword)
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 170, 251, 49))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_age = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_age.setStyleSheet("font: 10pt \"Book Antiqua\";")
        self.label_age.setObjectName("label_age")
        self.verticalLayout_3.addWidget(self.label_age)
        self.lineEdit_age = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_age.setStyleSheet("font: 10pt \"Book Antiqua\";")
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.verticalLayout_3.addWidget(self.lineEdit_age)
        self.pushButton_calc = QtWidgets.QPushButton(Form)
        self.pushButton_calc.setGeometry(QtCore.QRect(10, 420, 75, 23))
        self.pushButton_calc.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"font: 9pt \"Book Antiqua\";")
        self.pushButton_calc.setObjectName("pushButton_calc")
        self.layoutWidget_5 = QtWidgets.QWidget(Form)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 370, 251, 46))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_activity_2 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_activity_2.setStyleSheet("font: 10pt \"Book Antiqua\";")
        self.label_activity_2.setObjectName("label_activity_2")
        self.verticalLayout_9.addWidget(self.label_activity_2)
        self.comboBox_purpose = QtWidgets.QComboBox(self.layoutWidget_5)
        self.comboBox_purpose.setStyleSheet("background-color: rgb(218, 218, 218);font: 9pt \"Book Antiqua\";")
        self.comboBox_purpose.setObjectName("comboBox_activity_2")
        self.verticalLayout_9.addWidget(self.comboBox_purpose)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 70, 251, 49))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_login = QtWidgets.QLabel(self.layoutWidget1)
        self.label_login.setStyleSheet("font: 10pt \"Book Antiqua\";")
        self.label_login.setObjectName("label_login")
        self.verticalLayout.addWidget(self.label_login)
        self.lineEdit_login = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_login.setStyleSheet("font: 10pt \"Book Antiqua\";")
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.verticalLayout.addWidget(self.lineEdit_login)
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 220, 251, 51))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_weight = QtWidgets.QLabel(self.layoutWidget2)
        self.label_weight.setStyleSheet("font: 10pt \"Book Antiqua\";")
        self.label_weight.setObjectName("label_weight")
        self.verticalLayout_4.addWidget(self.label_weight)
        self.lineEdit_weight = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_weight.setStyleSheet("font: 10pt \"Book Antiqua\";")
        self.lineEdit_weight.setObjectName("lineEdit_weight")
        self.verticalLayout_4.addWidget(self.lineEdit_weight)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_hight = QtWidgets.QLabel(self.layoutWidget2)
        self.label_hight.setStyleSheet("font: 10pt \"Book Antiqua\";")
        self.label_hight.setObjectName("label_hight")
        self.verticalLayout_5.addWidget(self.label_hight)
        self.lineEdit_hight = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_hight.setStyleSheet("font: 10pt \"Book Antiqua\";")
        self.lineEdit_hight.setObjectName("lineEdit_hight")
        self.verticalLayout_5.addWidget(self.lineEdit_hight)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.layoutWidget3 = QtWidgets.QWidget(Form)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 273, 91, 46))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_sex = QtWidgets.QLabel(self.layoutWidget3)
        self.label_sex.setStyleSheet("font: 10pt \"Book Antiqua\";")
        self.label_sex.setObjectName("label_sex")
        self.verticalLayout_6.addWidget(self.label_sex)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_f = QtWidgets.QRadioButton(self.layoutWidget3)
        self.radioButton_f.setStyleSheet("font: 8pt \"Book Antiqua\";\n"
"")
        self.radioButton_f.setObjectName("radioButton_f")
        self.horizontalLayout_2.addWidget(self.radioButton_f)
        self.radioButton_m = QtWidgets.QRadioButton(self.layoutWidget3)
        self.radioButton_m.setStyleSheet("font: 8pt \"Book Antiqua\";")
        self.radioButton_m.setObjectName("radioButton_m")
        self.horizontalLayout_2.addWidget(self.radioButton_m)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.layoutWidget4 = QtWidgets.QWidget(Form)
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 320, 251, 46))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_activity = QtWidgets.QLabel(self.layoutWidget4)
        self.label_activity.setStyleSheet("font: 10pt \"Book Antiqua\";")
        self.label_activity.setObjectName("label_activity")
        self.verticalLayout_7.addWidget(self.label_activity)
        self.comboBox_activity = QtWidgets.QComboBox(self.layoutWidget4)
        self.comboBox_activity.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"font: 9pt \"Book Antiqua\";")
        self.comboBox_activity.setObjectName("comboBox_activity")
        self.verticalLayout_7.addWidget(self.comboBox_activity)
        self.layoutWidget5 = QtWidgets.QWidget(Form)
        self.layoutWidget5.setGeometry(QtCore.QRect(10, 450, 251, 49))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_8.setStyleSheet("font: 10pt \"Book Antiqua\";")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget5)
        self.lineEdit_6.setStyleSheet("font: 10pt \"Book Antiqua\";")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_8.addWidget(self.lineEdit_6)
        self.layoutWidget6 = QtWidgets.QWidget(Form)
        self.layoutWidget6.setGeometry(QtCore.QRect(80, 510, 158, 26))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_ok = QtWidgets.QPushButton(self.layoutWidget6)
        self.pushButton_ok.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"font: 9pt \"Book Antiqua\";")
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout_3.addWidget(self.pushButton_ok)
        self.pushButton_cancel = QtWidgets.QPushButton(self.layoutWidget6)
        self.pushButton_cancel.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"font: 9pt \"Book Antiqua\";")
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_3.addWidget(self.pushButton_cancel)
        self.warning = QtWidgets.QLabel(Form)
        self.warning.setGeometry(QtCore.QRect(10, 550, 231, 31))
        self.warning.setStyleSheet("font: 10pt \"Book Antiqua\";")
        self.warning.setObjectName("waring")
        self.waring_2 = QtWidgets.QLabel(Form)
        self.waring_2.setGeometry(QtCore.QRect(20, 20, 231, 31))
        self.waring_2.setStyleSheet("font: 10pt \"Book Antiqua\";")
        self.waring_2.setObjectName("waring_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "  "))
        self.label_keyword.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#0055ff;\">Введите пароль:</span></p></body></html>"))
        self.label_age.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#0055ff;\">Введиет ваш возраст:</span></p></body></html>"))
        self.pushButton_calc.setText(_translate("Form", "Рассчитать"))
        self.label_activity_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#0055ff;\">Выберете вашу цель</span></p></body></html>"))
        self.label_login.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#0055ff;\">Введите логин:</span></p></body></html>"))
        self.label_weight.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#0055ff;\">Введите ваш вес:</span></p></body></html>"))
        self.label_hight.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#0055ff;\">Введите ваш рост:</span></p></body></html>"))
        self.label_sex.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#0055ff;\">Выберете пол</span></p></body></html>"))
        self.radioButton_f.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#0055ff;\">Ж</span></p></body></html>"))
        self.radioButton_f.setText(_translate("Form", "Ж"))
        self.radioButton_m.setText(_translate("Form", "М"))
        self.label_activity.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#0055ff;\">Укажите вашу активность</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#0055ff;\">Ваша дневная норма калорий:</span></p></body></html>"))
        self.pushButton_ok.setText(_translate("Form", "Ок"))
        self.pushButton_cancel.setText(_translate("Form", "Отмена"))
        self.warning.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#2b2b2b;\">TextLabel</span></p></body></html>"))
        self.waring_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#933100;\">Регистрация</span></p></body></html>"))