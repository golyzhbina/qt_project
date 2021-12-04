import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from reg_form_py import Ui_Form
from sqlite3 import connect


class RegistrationWindow(QWidget, Ui_Form):

    def __init__(self):
        super(RegistrationWindow, self).__init__()
        self.setupUi(self)

        self.lineEdit_login.textChanged.connect(self.check_login)
        self.lineEdit_weight.textChanged.connect(self.check_weight)
        self.lineEdit_hight.textChanged.connect(self.check_hight)
        self.lineEdit_age.textChanged.connect(self.check_age)
        self.lineEdit_keyword.textChanged.connect(self.check_keyword)

        self.pushButton_cancel.clicked.connect(self.close)
        self.pushButton_calc.clicked.connect(self.calc)
        self.pushButton_ok.clicked.connect(self.save)

        self.connection = connect('users.db')
        self.warning = QLabel(self)
        self.warning.setGeometry(10, 475, 200, 40)

        for st in ["Выбрать", "Сидячий образ жизни",
                                "Умеренная активность (занятия 1-3 раз в неделю)",
                                "Средняя активность (занятия 3-5 раз в неделю)",
                                "Активные люди (занятия 6-7 раз в неделю)",
                                "Спортсмены(6-7 раз в неделю)"]:
            self.comboBox_activity.addItem(st)

        self.coef_activity = {"Сидячий образ жизни": 1.2,
                              "Умеренная активность (занятия 1-3 раз в неделю)": 1.375,
                              "Средняя активность (занятия 3-5 раз в неделю)": 1.55,
                              "Активные люди (занятия 6-7 раз в неделю)": 1.725,
                              "Спортсмены(6-7 раз в неделю)": 1.9,
                              "Выбрать": None}

        for st in ["Выбрать", "Похудение", "Поддержание веса", "Набор"]:
            self.comboBox_purpose.addItem(st)

        self.coef_purpose = {"Похудение": 0.85, "Поддержание веса": 1.0, "Набор": 1.15, "Выбрать": None}

    def check_login(self):
        login = self.lineEdit_login.text()

        if not login.isalnum():
            self.warning.setText("Логин должен содержать только\nцифры и латинские буквы")

        elif len(self.lineEdit_login.text()) < 3:
            self.warning.setText("Логин должен быть не менее четырех символов")
            return False

        elif login.isalnum():
            if self.warning.text() == "Логин должен быть не менее четырех символов" or \
                self.warning.text() == "Логин должен содержать только\nцифры и латинские буквы":

                self.warning.setText(" ")

            cursor = self.connection.cursor()
            check = bool(cursor.execute(f"SELECT * FROM user WHERE id_user='{login}'").fetchall())

            if check:
                self.warning.setText("Такой логин уже существует")
                return False
            else:
                if self.warning.text() == "Такой логин уже существует":
                    self.warning.setText(" ")
                return True

    def check_hight(self):

        h = self.lineEdit_hight.text()
        if not h.replace(".", "").replace(",", "").isnumeric():
            self.warning.setText("Рост должен быть числом")
            return False

        elif h.replace(".", "").replace(",", "").isnumeric() and not 0.8 < float(h.replace(".", "").replace(",", "")) < 2.15:
            self.warning.setText("Введённое значение роста некорректно")

        elif h.replace(".", "").replace(",", "").isnumeric():
            if self.warning.text() in ["Рост должен быть числом", "Введённое значение роста некорректно"]:
                self.warning.setText(" ")
            self.warning.setText(" ")
            return True

    def check_weight(self):

        w = self.lineEdit_weight.text()
        if not w.replace(".", "").replace(",", "").isnumeric():
            self.warning.setText("Вес должен быть числом")
            return False

        elif w.replace(".", "").replace(",", "").isnumeric() and not 30 < float(w.replace(".", "").replace(",", "")) < 350:
            self.warning.setText("Введённое значение веса некорректно ")
            return False

        elif w.replace(".", "").replace(",", "").isnumeric():
            if self.warning.text() in ["Вес должен быть числом", "Введённое значение веса некорректно"]:
                self.warning.setText(" ")
            return True

    def check_age(self):

        a = self.lineEdit_age.text()
        if not a.replace(".", "").replace(",", "").isnumeric():
            self.warning.setText("Возраст должен быть числом")
            return False

        elif a.replace(".", "").replace(",", "").isnumeric() and not \
            12 < int(a.replace(".", "").replace(",", "").isnumeric()) < 110:
            self.warning.setText("Введённое значение возраста некорректно")

        elif a.replace(".", "").replace(",", "").isnumeric():

            if self.warning.text() in ["Введённое значение возраста некорректно", "Возраст должен быть числом"]:
                self.warning.setText(" ")

            return True

    def check_keyword(self):
        if " " in set(self.lineEdit_keyword.text()):
            self.warning.setText("Пароль не должен содержать пробел")
            return False
        elif len(self.lineEdit_keyword.text()) < 3:
            self.warning.setText("Пароль должен содержать не менее\nтрёх символов")
            return False

        if self.warning.text() in ["Пароль не должен содержать пробел","Пароль должен содержать не менее\nтрёх символов"]:
            self.warning.setText(" ")
        return True

    def calc(self):

        check = self.check_age() and self.check_login() and self.check_hight() and self.check_weight()

        if bool(self.coef_activity[self.comboBox_activity.currentText()]) is False:
            self.warning.setText("Выберете вашу активность")
            return

        if check:
            if bool(self.coef_purpose[self.comboBox_purpose.currentText()]) is False:
                self.warning.setText("Выберете цель")
                return

            if not self.radioButton_f.isChecked() and not self.radioButton_m.isChecked():
                self.warning.setText("Выберете пол")
                return

            high = float(self.lineEdit_hight.text().replace(",", ".").strip())
            weight = float(self.lineEdit_weight.text().replace(",", ".").strip())
            age = float(self.lineEdit_age.text().strip())
            coef_activity = self.coef_activity[self.comboBox_activity.currentText()]
            coef_purpose = self.coef_purpose[self.comboBox_purpose.currentText()]

            if self.radioButton_f.isChecked():
                calories = (447.593 + 9.247 * weight + 3.098 * high - 4.330 * age) * coef_activity * coef_purpose
            elif self.radioButton_m:
                calories = (88.362 + 13.397 * weight + 4.799 * high - 5.677 * age) * coef_activity * coef_purpose

            self.lineEdit_calories.setText(str(int(calories)))

    def save(self):

        if len(self.lineEdit_calories.text()) == 0:
            self.calc()
        elif self.check_keyword():
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO user(id_user, keyword, calories) VALUES (?, ?, ?)",
                               (self.lineEdit_login.text().strip(),
                            self.lineEdit_keyword.text().strip(),
                            self.lineEdit_calories.text().strip()))
            self.connection.commit()
            self.close()
        else:
            return



sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RegistrationWindow()
    ex.show()
    sys.exit(app.exec())