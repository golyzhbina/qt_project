import sys

from sqlite3 import connect

from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHeaderView, QTableWidgetItem
from add_form import Ui_Form
from main_window.add_form.class_add_form import AddWindow


class AddProduct(QWidget, Ui_Form):

    def __init__(self, login):
        super(AddProduct, self).__init__()
        self.setupUi(self)

        pal = self.waring.palette()
        pal.setColor(QPalette.WindowText, QColor(255, 255, 255))
        self.waring.setPalette(pal)

        self.connection_prod = connect(r"C:\Users\Lenovo\PycharmProject\qt_project\product_base.db")

        self.login = login
        self.flag_value = False

        self.quality_proteins = 0
        self.quality_fats = 0
        self.quality_carbohydrates = 0
        self.quality_calories = 0
        self.quality_weight = 0

        self.set_combobox()

        self.pushButton_cancel.clicked.connect(self.close)
        self.pushButton_add.clicked.connect(self.save_product)
        self.pushButton_add_rec.clicked.connect(self.add_product_in_rec)
        self.pushButton_del_rec.clicked.connect(self.del_ingredient)
        self.pushButton_save.clicked.connect(self.save_rec)
        self.pushButton_del.clicked.connect(self.del_product)
        self.pushButton_del_pos.clicked.connect(self.del_recipe)

        self.lineEdit_name.textChanged.connect(lambda: self.waring.setText(" "))
        self.lineEdit_proteins.textChanged.connect(self.check_value)
        self.lineEdit_fats.textChanged.connect(self.check_value)
        self.lineEdit_carbohydrates.textChanged.connect(self.check_value)

        self.comboBox_myprod.currentIndexChanged.connect(self.load_prod)
        self.comboBox_myrec.currentIndexChanged.connect(self.load_rec)

        self.tableWidget_rec.setColumnCount(6)
        self.tableWidget_rec.setHorizontalHeaderLabels(["Название", "Масса", "Калории", "Белки", "Жиры", "Углеводы"])
        self.tableWidget_rec.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_rec.itemClicked.connect(self.select_row)

        self.set_info()
    def check_value(self):

        sender: QLineEdit = self.sender()
        value = sender.text().replace(",", "").replace(".", "")
        if not value.isnumeric() and len(value) != 0:
            self.waring.setText("Количество белков, жиров и углеводов должно быть\nзадано числом")
            self.flag_value = False

        elif value.isnumeric():
            self.waring.setText(" ")
            self.flag_value = True

    def save_product(self):

        if len(self.lineEdit_name.text().strip()) == 0:
            self.waring.setText("Введите название продукта")

        elif len(self.lineEdit_name.text().strip()) > 0 and self.flag_value:

            name = self.lineEdit_name.text().strip()
            cursor = self.connection_prod.cursor()
            calories = self.lineEdit_calories.text().replace(",", ".").strip()
            proteins = self.lineEdit_proteins.text().replace(",", ".").strip()
            fats = self.lineEdit_fats.text().replace(",", ".").strip()
            carb = self.lineEdit_carbohydrates.text().replace(",", ".").strip()

            flag = self.check_name(name)
            if not flag:

                cursor.execute("INSERT INTO user_product(id_user, product_name, calories, proteins, fats, carbohydrates) "
                               "VALUES(?, ?, ?, ?, ?, ?)", [self.login, name, calories, proteins, fats, carb])
                self.connection_prod.commit()

                self.waring.setText("Продукт успешно добавлен!")

            else:
                cursor.execute(f"UPDATE user_product SET calories={calories}, proteins={proteins}, fats={fats},"
                               f"carbohydrates={carb} WHERE id_user='{self.login}' and product_name='{name}'")
                self.connection_prod.commit()

                self.waring.setText("Обновления сохранены!")

            self.flag_value = False
            self.lineEdit_name.clear()
            self.lineEdit_proteins.clear()
            self.lineEdit_fats.clear()
            self.lineEdit_carbohydrates.clear()
            self.lineEdit_calories.clear()
            self.set_combobox()

    def save_rec(self):

        if len(self.lineEdit_name_rec.text().strip()) == 0:
            self.waring.setText("Введите название продукта")
            return

        else:

            name = self.lineEdit_name_rec.text().strip()
            flag = self.check_name(name)

            cur_cal = round(self.quality_calories * 100 / self.quality_weight, 1)
            cur_pro = round(self.quality_proteins * 100 / self.quality_weight, 1)
            cur_fat = round(self.quality_fats * 100 / self.quality_weight, 1)
            cur_carb = round(self.quality_carbohydrates * 100 / self.quality_weight, 1)

            cursor = self.connection_prod.cursor()

            if flag:
                cursor.execute(f"DELETE FROM user_product WHERE id_user='{self.login}' AND product_name='{name}'")
                cursor.execute(f"DELETE FROM user_rec WHERE id_user='{self.login}' AND name_rec='{name}'")
                self.connection_prod.commit()
                self.waring.setText("Обновления сохранены!")

            cursor.execute("INSERT INTO user_product(id_user, product_name, calories, proteins, fats, carbohydrates) "
                           "VALUES(?, ?, ?, ?, ?, ?)", [self.login, name, cur_cal, cur_pro, cur_fat, cur_carb])
            self.connection_prod.commit()

            rows = self.tableWidget_rec.rowCount()

            for row in (range(rows)):
                info = []
                for column in range(6):
                    info.append(self.tableWidget_rec.item(row, column).text())

                cursor.execute("INSERT INTO user_rec(id_user, name_rec, name, weight, calories, "
                               "proteins, fats, carbohydrates) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                               [self.login, name, *info])
                self.connection_prod.commit()
            if not flag:
                self.waring.setText("Продукт успешно добавлен!")

            self.flag_value = False

            self.quality_proteins = 0
            self.quality_fats = 0
            self.quality_carbohydrates = 0
            self.quality_calories = 0
            self.quality_weight = 0

            self.tableWidget_rec.clear()
            self.tableWidget_rec.setRowCount(0)
            self.tableWidget_rec.setColumnCount(6)
            self.tableWidget_rec.setHorizontalHeaderLabels(["Название", "Масса", "Калории", "Белки", "Жиры", "Углеводы"])
            self.tableWidget_rec.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

            self.label_info_rec.setText(" ")
            self.lineEdit_name_rec.clear()
            self.set_combobox()

    def add_product_in_rec(self):
        self.add_wind = AddWindow(self.tableWidget_rec, self)
        self.add_wind.show()

    def del_ingredient(self):
        items = self.tableWidget_rec.selectedItems()[::6]

        for item in items:
            row = item.row()

            for i in range(6):

                if i == 1:
                    self.quality_weight -= float(self.tableWidget_rec.item(row, i).text())
                elif i == 2:
                    self.quality_calories -= float(self.tableWidget_rec.item(row, i).text())
                elif i == 3:
                    self.quality_proteins -= float(self.tableWidget_rec.item(row, i).text())
                elif i == 4:
                    self.quality_fats -= float(self.tableWidget_rec.item(row, i).text())
                elif i == 5:
                    self.quality_carbohydrates -= float(self.tableWidget_rec.item(row, i).text())

            self.tableWidget_rec.removeRow(row)
        self.set_info()

    def select_row(self):

        select_item = self.tableWidget_rec.selectedItems()[0]
        row = select_item.row()

        for i in range(6):
            self.tableWidget_rec.item(row, i).setSelected(True)

    def set_info(self):

        if self.quality_weight == 0:
            cur_cal = 0.0
            cur_pro = 0.0
            cur_fat = 0.0
            cur_carb = 0.0
        else:
            cur_cal = round(self.quality_calories * 100 / self.quality_weight, 1)
            cur_pro = round(self.quality_proteins * 100 / self.quality_weight, 1)
            cur_fat = round(self.quality_fats * 100 / self.quality_weight, 1)
            cur_carb = round(self.quality_carbohydrates * 100 / self.quality_weight, 1)

        self.label_info_rec.setText(f"Масса всего блюда: {self.quality_weight} грамм\n"
                                f"На всё блюдо:\nKалории: {self.quality_calories}   "
                                f"Белки: {self.quality_proteins}   "
                                f"Жиры: {self.quality_fats}   "
                                f"Углеводы: {self.quality_carbohydrates}\n"
                                f"На 100 грамм блюда:\nKалории: {cur_cal}   "
                                f"Белки: {cur_pro}   "
                                f"Жиры: {cur_fat}   "
                                f"Углеводы: {cur_carb}")

    def calc(self):

        row = self.tableWidget_rec.rowCount()
        for i in range(6):

            if i == 1:
                self.quality_weight += float(self.tableWidget_rec.item(row - 1, i).text())
            elif i == 2:
                self.quality_calories += float(self.tableWidget_rec.item(row - 1, i).text())
            elif i == 3:
                self.quality_proteins += float(self.tableWidget_rec.item(row - 1, i).text())
            elif i == 4:
                self.quality_fats += float(self.tableWidget_rec.item(row - 1, i).text())
            elif i == 5:
                self.quality_carbohydrates += float(self.tableWidget_rec.item(row - 1, i).text())
        self.set_info()

    def set_combobox(self):

        cursor = self.connection_prod.cursor()
        data = cursor.execute(f"SELECT product_name FROM user_product WHERE id_user='{self.login}'").fetchall()
        data = list(map(lambda x: x[0], data))

        self.comboBox_myprod.clear()
        self.comboBox_myprod.addItem("Выбрать")
        if len(data) != 0:
            for name in data:
                self.comboBox_myprod.addItem(name)

        data = cursor.execute(f"SELECT name_rec FROM user_rec WHERE id_user='{self.login}'").fetchall()
        data = list(set(map(lambda x: x[0], data)))
        data.sort()
        self.comboBox_myrec.clear()
        self.comboBox_myrec.addItem("Выбрать")
        if len(data) != 0:

            for name in data:
                self.comboBox_myrec.addItem(name)

    def load_prod(self):

        ind = self.comboBox_myprod.currentIndex()
        if ind == 0:
            self.lineEdit_name.clear()
            self.lineEdit_proteins.clear()
            self.lineEdit_fats.clear()
            self.lineEdit_carbohydrates.clear()
            self.lineEdit_calories.clear()
        else:
            name = self.comboBox_myprod.currentText()
            cursor = self.connection_prod.cursor()
            data = cursor.execute(f"SELECT * FROM user_product WHERE product_name='{name}'").fetchone()

            if data:
                for i, elem in enumerate(data):

                    if i == 2:
                        self.lineEdit_name.setText(elem)
                    elif i == 3:
                        self.lineEdit_calories.setText(str(elem))
                    elif i == 4:
                        self.lineEdit_proteins.setText(str(elem))
                    elif i == 5:
                        self.lineEdit_fats.setText(str(elem))
                    elif i == 6:
                        self.lineEdit_carbohydrates.setText(str(elem))

                self.flag_change = True

    def check_name(self, name):

        cursor = self.connection_prod.cursor()
        data = cursor.execute(f"SELECT product_name FROM user_product WHERE id_user='{self.login}'")
        data = list(map(lambda x: x[0], data))
        if name in data:
            return True
        else:
            return False

    def load_rec(self):

        self.tableWidget_rec.clear()
        self.tableWidget_rec.setRowCount(0)
        self.tableWidget_rec.setColumnCount(6)
        self.tableWidget_rec.setHorizontalHeaderLabels(["Название", "Масса", "Калории", "Белки", "Жиры", "Углеводы"])
        self.tableWidget_rec.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.lineEdit_name_rec.clear()

        self.quality_proteins = 0
        self.quality_fats = 0
        self.quality_carbohydrates = 0
        self.quality_calories = 0
        self.quality_weight = 0

        self.set_info()

        ind = self.comboBox_myrec.currentIndex()
        if ind == 0:
            return
        else:
            name = self.comboBox_myrec.currentText()
            self.lineEdit_name_rec.setText(name)
            cursor = self.connection_prod.cursor()
            data = cursor.execute(f"SELECT * FROM user_rec WHERE id_user='{self.login}' AND name_rec='{name}'").fetchall()

            if data:
                data = list(map(lambda x: x[3:], data))

                for i, row in enumerate(data):
                    self.tableWidget_rec.setRowCount(
                        self.tableWidget_rec.rowCount() + 1)

                    for j, elem in enumerate(row):
                        self.tableWidget_rec.setItem(i, j, QTableWidgetItem(str(elem)))

                        if i % 2 == 0:
                            self.tableWidget_rec.item(i, j).setBackground(QColor(245, 245, 245))
                        else:
                            self.tableWidget_rec.item(i, j).setBackground(QColor(225, 225, 225))

                    self.calc()

    def del_product(self):

        name = self.comboBox_myprod.currentText()
        self.del_pos(name)

    def del_recipe(self):

        name = self.comboBox_myrec.currentText()
        self.del_pos(name)

    def del_pos(self, name):

        cursor = self.connection_prod.cursor()
        cursor.execute(f"DELETE FROM user_product WHERE id_user='{self.login}' AND product_name='{name}'")
        self.connection_prod.commit()

        data = cursor.execute(f"SELECT name_rec FROM user_rec WHERE id_user='{self.login}'").fetchall()
        data = list(map(lambda x: x[0], data))

        if name in data:
            cursor.execute(f"DELETE FROM user_rec WHERE id_user='{self.login}' AND name_rec='{name}'")
            self.connection_prod.commit()

        self.set_combobox()
sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddProduct("golub")
    ex.show()
    sys.exit(app.exec())