import sys
import sqlite3

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from hello_window_py import Ui_Form
from main_window.class_main_window import MainWindow
from reg_window.class_reg_window import RegistrationWindow


class HelloWindow(QWidget, Ui_Form):

    def __init__(self):
        super(HelloWindow, self).__init__()
        self.setupUi(self)

        self.setMinimumSize(self.size())
        self.setMaximumSize(self.size())

        self.connection = sqlite3.connect(r"../users.db")

        self.pushButton_reg.clicked.connect(self.registration)
        self.pushButton_ex.clicked.connect(self.ex)

    def registration(self):

        self.reg_window = RegistrationWindow(self)
        self.reg_window.show()
        self.hide()

    def ex(self):
        cursor = self.connection.cursor()

        login = self.lineEdit_log.text().strip()

        logins = cursor.execute("SELECT id_user FROM user").fetchall()
        logins = list(map(lambda x: x[0], logins))

        if login not in logins:
            self.waring.setText("Неверно введён логин")
        elif login in logins:

            password = self.lineEdit_pas.text().strip()

            tru_pass = cursor.execute(f"SELECT keyword FROM user WHERE id_user='{login}'").fetchall()[0][0]

            if password != str(tru_pass):
                self.waring.setText("Неверно введен пароль")

            else:
                calories = cursor.execute(f"SELECT calories FROM user WHERE id_user='{login}'").fetchall()[0][0]
                self.main_window = MainWindow(calories, login, self)
                self.main_window.show()
                self.lineEdit_pas.clear()
                self.lineEdit_log.clear()
                self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HelloWindow()
    ex.show()
    sys.exit(app.exec())




