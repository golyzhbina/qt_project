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
        Form.resize(258, 527)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 60, 231, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_keyword = QtWidgets.QLabel(self.layoutWidget)
        self.label_keyword.setObjectName("label_keyword")
        self.verticalLayout_2.addWidget(self.label_keyword)
        self.lineEdit_keyword = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_keyword.setObjectName("lineEdit_keywod")
        self.verticalLayout_2.addWidget(self.lineEdit_keyword)
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 110, 231, 41))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_age = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_age.setObjectName("label_age")
        self.verticalLayout_3.addWidget(self.label_age)
        self.lineEdit_age = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_age.setObjectName("lineEdit_age")
        self.verticalLayout_3.addWidget(self.lineEdit_age)
        self.pushButton_calc = QtWidgets.QPushButton(Form)
        self.pushButton_calc.setGeometry(QtCore.QRect(10, 360, 75, 23))
        self.pushButton_calc.setObjectName("pushButton_calc")
        self.layoutWidget_5 = QtWidgets.QWidget(Form)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 310, 231, 41))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_purpose = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_purpose.setObjectName("label_activity_2")
        self.verticalLayout_9.addWidget(self.label_purpose)
        self.comboBox_purpose = QtWidgets.QComboBox(self.layoutWidget_5)
        self.comboBox_purpose.setObjectName("comboBox_purpose")
        self.verticalLayout_9.addWidget(self.comboBox_purpose)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 231, 41))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_login = QtWidgets.QLabel(self.widget)
        self.label_login.setObjectName("label_login")
        self.verticalLayout.addWidget(self.label_login)
        self.lineEdit_login = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.verticalLayout.addWidget(self.lineEdit_login)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(10, 160, 231, 43))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_weight = QtWidgets.QLabel(self.widget1)
        self.label_weight.setObjectName("label_weight")
        self.verticalLayout_4.addWidget(self.label_weight)
        self.lineEdit_weight = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_weight.setObjectName("lineEdit_weight")
        self.verticalLayout_4.addWidget(self.lineEdit_weight)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_hight = QtWidgets.QLabel(self.widget1)
        self.label_hight.setObjectName("label_hight")
        self.verticalLayout_5.addWidget(self.label_hight)
        self.lineEdit_hight = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_hight.setObjectName("lineEdit_hight")
        self.verticalLayout_5.addWidget(self.lineEdit_hight)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.widget2 = QtWidgets.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(10, 210, 74, 40))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_sex = QtWidgets.QLabel(self.widget2)
        self.label_sex.setObjectName("label_sex")
        self.verticalLayout_6.addWidget(self.label_sex)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_f = QtWidgets.QRadioButton(self.widget2)
        self.radioButton_f.setObjectName("radioButton_f")
        self.horizontalLayout_2.addWidget(self.radioButton_f)
        self.radioButton_m = QtWidgets.QRadioButton(self.widget2)
        self.radioButton_m.setObjectName("radioButton_m")
        self.horizontalLayout_2.addWidget(self.radioButton_m)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.widget3 = QtWidgets.QWidget(Form)
        self.widget3.setGeometry(QtCore.QRect(10, 260, 231, 41))
        self.widget3.setObjectName("widget3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_activity = QtWidgets.QLabel(self.widget3)
        self.label_activity.setObjectName("label_activity")
        self.verticalLayout_7.addWidget(self.label_activity)
        self.comboBox_activity = QtWidgets.QComboBox(self.widget3)
        self.comboBox_activity.setObjectName("comboBox_activity")
        self.verticalLayout_7.addWidget(self.comboBox_activity)
        self.widget4 = QtWidgets.QWidget(Form)
        self.widget4.setGeometry(QtCore.QRect(10, 390, 231, 41))
        self.widget4.setObjectName("widget4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget4)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.widget4)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.lineEdit_calories = QtWidgets.QLineEdit(self.widget4)
        self.lineEdit_calories.setObjectName("lineEdit_6")
        self.verticalLayout_8.addWidget(self.lineEdit_calories)
        self.widget5 = QtWidgets.QWidget(Form)
        self.widget5.setGeometry(QtCore.QRect(80, 450, 158, 25))
        self.widget5.setObjectName("widget5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_ok = QtWidgets.QPushButton(self.widget5)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout_3.addWidget(self.pushButton_ok)
        self.pushButton_cancel = QtWidgets.QPushButton(self.widget5)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_3.addWidget(self.pushButton_cancel)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_keyword.setText(_translate("Form", "Введите пароль:"))
        self.label_age.setText(_translate("Form", "Введитe ваш возраст:"))
        self.pushButton_calc.setText(_translate("Form", "Рассчитать"))
        self.label_purpose.setText(_translate("Form", "Выберете вашу цель"))
        self.label_login.setText(_translate("Form", "Введите логин:"))
        self.label_weight.setText(_translate("Form", "Введите ваш вес:"))
        self.label_hight.setText(_translate("Form", "Введите ваш рост:"))
        self.label_sex.setText(_translate("Form", "Выберете пол"))
        self.radioButton_f.setText(_translate("Form", "Ж"))
        self.radioButton_m.setText(_translate("Form", "М"))
        self.label_activity.setText(_translate("Form", "Укажите вашу активность"))
        self.label_8.setText(_translate("Form", "Ваша дневная норма калорий:"))
        self.pushButton_ok.setText(_translate("Form", "Ок"))
        self.pushButton_cancel.setText(_translate("Form", "Отмена"))