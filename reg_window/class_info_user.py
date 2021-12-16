from PyQt5.QtWidgets import QWidget
from .reg_form_py import Ui_Form
from sqlite3 import connect


class InfoUser(QWidget, Ui_Form):

    def __init__(self):
        super(InfoUser, self).__init__()
        self.setupUi(self)

        self.setMinimumSize(self.size())
        self.setMaximumSize(self.size())

        self.lineEdit_login.textChanged.connect(self.check_login)
        self.lineEdit_weight.textChanged.connect(self.check_weight)
        self.lineEdit_hight.textChanged.connect(self.check_hight)
        self.lineEdit_age.textChanged.connect(self.check_age)
        self.lineEdit_keyword.textChanged.connect(self.check_keyword)

        self.pushButton_cancel.clicked.connect(self.close)
        self.pushButton_calc.clicked.connect(self.calc)
        self.pushButton_ok.clicked.connect(self.save)

        self.connection = connect('../users.db')

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

        elif h.replace(".", "").replace(",", "").isnumeric() and not 80 < float(h.replace(",", ".")) < 215:
            self.warning.setText("Введённое значение роста некорректно")

        elif h.replace(".", "").replace(",", "").isnumeric():
            self.warning.setText(" ")
            return True

    def check_weight(self):

        w = self.lineEdit_weight.text()
        if not w.replace(".", "").replace(",", "").isnumeric():
            self.warning.setText("Вес должен быть числом")
            return False

        elif w.replace(".", "").replace(",", "").isnumeric() and not 30 < float(w.replace(",", ".")) < 350:
            self.warning.setText("Введённое значение веса некорректно ")
            return False

        elif w.replace(".", "").replace(",", "").isnumeric():
            if self.warning.text() in ["Вес должен быть числом", "Введённое значение веса некорректно"]:
                self.warning.setText(" ")
            return True

    def check_age(self):

        self.warning.setText(" ")
        a = self.lineEdit_age.text().strip()

        if not a.isnumeric():
            self.warning.setText("Возраст должен быть числом")
            return False

        elif a.isnumeric() and not \
            12 < int(a) < 110:
            self.warning.setText("Введённое значение возраста \nнекорректно")
            print(int(a))

        elif a.isnumeric():

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
        pass

    def save(self):
        pass