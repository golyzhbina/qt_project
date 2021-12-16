import sys
from .class_info_user import InfoUser
from main_window.class_main_window import MainWindow



class RegistrationWindow(InfoUser):

    def __init__(self, hello_wind):
        super(RegistrationWindow, self).__init__()
        self.hello_wind = hello_wind
        self.pushButton_cancel.clicked.connect(self.close_)

    def save(self):

        if len(self.lineEdit_calories.text()) == 0:
            self.calc()
        elif self.check_keyword():

            cursor = self.connection.cursor()

            cursor.execute("INSERT INTO user(id_user, keyword, calories) VALUES (?, ?, ?)",
                           (self.lineEdit_login.text().strip(),
                            self.lineEdit_keyword.text().strip(),
                            self.lineEdit_calories.text().strip()))
            self.main_window = MainWindow(float(self.lineEdit_calories.text().strip()),
                                          self.lineEdit_login.text().strip())
            self.connection.commit()
            self.close()
        else:
            return

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

    def close_(self):
        self.hello_wind.show()
        self.close()






sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook


