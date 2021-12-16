from .class_info_user import InfoUser


class CalcCalories(InfoUser):

    def __init__(self, obj):

        super(CalcCalories, self).__init__()

        self.obj = obj
        self.label_reg.hide()
        self.lineEdit_login.setText(self.obj.login)
        self.lineEdit_login.setEnabled(False)
        self.set_pas()


    def save(self):

        cursor = self.connection.cursor()
        calories = self.lineEdit_calories.text().strip()
        print(self.obj.login, calories)
        cursor.execute(f"UPDATE user SET calories={calories} WHERE id_user='{self.obj.login}'")
        self.connection.commit()
        self.warning.setText("Данные обновлены!")

    def set_pas(self):
        cursor = self.connection.cursor()
        pas = cursor.execute(f"SELECT keyword FROM user WHERE id_user='{self.obj.login}'").fetchone()
        self.lineEdit_keyword.setText(str(pas[0]))
        self.lineEdit_keyword.setEnabled(False)

    def calc(self):

        check = self.check_age() and self.check_hight() and self.check_weight()

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