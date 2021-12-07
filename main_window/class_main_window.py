import sys
from sqlite3 import connect

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QMainWindow, QApplication, QHeaderView, QVBoxLayout, QTableWidgetItem
from .main_window_py import Ui_MainWindow
from .add_form.class_add_form import AddWindow
from .calendar_window.class_calendar import Calendar

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from numpy import array

from datetime import datetime


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, calories, login):
        super().__init__()
        self.setupUi(self)

        self.login = login
        self.label_login.setText(f"Логин: {login}")

        self.connection = connect(r"..\users.db")
        self.dict_tab_tables = {0: self.tableWidget_breakfast,
                                1: self.tableWidget_lunch,
                                2: self.tableWidget_dinner,
                                3: self.tableWidget_meal}

        self.pushButton_break_add.clicked.connect(self.add_product)
        self.pushButton_lunch_add.clicked.connect(self.add_product)
        self.pushButton_din_add.clicked.connect(self.add_product)
        self.pushButton_meal_add.clicked.connect(self.add_product)

        self.pushButton_break_del.clicked.connect(self.del_product)
        self.pushButton_lunch_del.clicked.connect(self.del_product)
        self.pushButton_din_del.clicked.connect(self.del_product)
        self.pushButton_meal_del.clicked.connect(self.del_product)

        self.set_headers()

        self.quality_proteins = 0
        self.quality_fats = 0
        self.quality_carbohydrates = 0
        self.quality_calories = 0
        self.calories_day = calories
        self.label_cal_day.setText(f"Норма калорий: {str(self.calories_day)}")

        self.count_change = 0
        self.tableWidget_breakfast.itemChanged.connect(self.check_change)
        self.tableWidget_lunch.itemChanged.connect(self.check_change)
        self.tableWidget_dinner.itemChanged.connect(self.check_change)
        self.tableWidget_meal.itemChanged.connect(self.check_change)

        self.dict_months = {'01': "января", '02': "февраля", '03': "марта", '04': "апреля", '05': "мая",
                            '06': "июня", '07': "июля", '08': "августа", '09': "сентября", '10': "октября",
                            '11': "ноября", '12': "декабря"}

        self.dict_week = {'0': "Понедельник", '1': "Втроник", '2': "Среда", '3': "Четверг",
                          '4': "Пятница", '5': "Суббота", '6': "Воскресенье"}

        self.day = datetime.now().date()
        self.day_list = str(datetime.now().date()).split("-")
        self.label_day.setText(f"{self.day_list[-1].replace('0', '')} {self.dict_months[self.day_list[1]]}, "
                               f"{self.dict_week[str(self.day.weekday())]}")

        self.pushButton_get_day.clicked.connect(self.get_date)


        self.fig, self.ax = plt.subplots()
        self.ax.pie(array([1]), radius=1, wedgeprops=dict(width=0.3))
        self.ax.pie(array([[1], [1], [1]]).sum(axis=1), radius=1-0.3, wedgeprops=dict(width=0.3, edgecolor='w'))

        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self)

        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.canvas)

        self.setLayout(self.vbox)
        self.vbox.setGeometry(QRect(420, 20, 300, 300))

        self.load_tables()

    def getFigure(self):
        return self.fig

    def draw(self):

        if self.quality_calories > self.calories_day:

            self.ax.pie(array([self.quality_calories, self.quality_calories - self.calories_day]),
                        radius=1, wedgeprops=dict(width=0.3), colors=["c", "gray"])
            self.ax.pie(array([[self.quality_proteins], [self.quality_fats], [self.quality_carbohydrates]]).sum(axis=1),
                        radius=1-0.3, wedgeprops=dict(width=0.3, edgecolor='w'), colors=["silver", "darkorange", "dodgerblue"])

        elif self.calories_day > self.quality_calories and self.quality_calories != 0:

            self.ax.pie(array([self.quality_calories,  - self.quality_calories + self.calories_day]),
                        radius=1, wedgeprops=dict(width=0.3), colors=["c", "gray"])
            self.ax.pie(array([[self.quality_proteins], [self.quality_fats], [self.quality_carbohydrates]]).sum(axis=1),
                        radius=1-0.3, wedgeprops=dict(width=0.3, edgecolor='w'),
                        colors=["silver", "darkorange", "dodgerblue"])

        elif self.quality_calories == 0:
            self.ax.pie(array([1]),
                        radius=1, wedgeprops=dict(width=0.3), colors=["c"])
            self.ax.pie(array([[1], [1], [1]]).sum(axis=1),
                        radius=1-0.3, wedgeprops=dict(width=0.3, edgecolor='w'),
                        colors=["silver", "darkorange", "dodgerblue"])

        self.canvas.draw()

    def add_product(self):

        self.add_window = AddWindow(self.dict_tab_tables[self.tabWidget_menu.currentIndex()], self.day, self.login,
                                    self.dict_tab_tables[self.tabWidget_menu.currentIndex()].objectName().split("_")[-1])
        self.add_window.show()

    def calc_calories(self):
        try:
            self.count_change = 0
            i = self.tabWidget_menu.currentIndex()
            count_row = self.dict_tab_tables[i].rowCount()
            self.quality_calories += float(self.dict_tab_tables[i].item(count_row - 1, 2).text())
            self.quality_proteins += float(self.dict_tab_tables[i].item(count_row - 1, 3).text())
            self.quality_fats += float(self.dict_tab_tables[i].item(count_row - 1, 4).text())
            self.quality_carbohydrates += float(self.dict_tab_tables[i].item(count_row - 1, 5).text())
        except AttributeError:
            return

        self.draw()

    def check_change(self):

        if self.count_change == 5:
            self.calc_calories()
        else:
            self.count_change += 1
            print("done")

    def load_tables(self):

        self.tableWidget_lunch.clear()
        self.tableWidget_breakfast.clear()
        self.tableWidget_dinner.clear()
        self.tableWidget_meal.clear()

        self.tableWidget_meal.setRowCount(0)
        self.tableWidget_lunch.setRowCount(0)
        self.tableWidget_dinner.setRowCount(0)
        self.tableWidget_breakfast.setRowCount(0)

        self.set_headers()

        cursor = self.connection.cursor()
        data = cursor.execute(f"SELECT * FROM food_day WHERE id_user='{self.login}' AND day='{str(self.day)}'").fetchall()
        print("-"* 30)
        if len(data) == 0:

            self.quality_calories = 0
            self.quality_proteins = 0
            self.quality_fats = 0
            self.quality_carbohydrates = 0

            self.draw()

            return

        else:
            self.quality_calories = sum(map(lambda x: x[6], data))
            self.quality_proteins = sum(map(lambda x: x[7], data))
            self.quality_fats = sum(map(lambda x: x[8], data))
            self.quality_carbohydrates = sum(map(lambda x: x[9], data))
            self.draw()

            names, data = list(map(lambda x: x[3], data)), list(map(lambda x: x[4:], data))
            name_tables = ["breakfast", "lunch", "dinner", "meal"]

            for i in range(len(names)):
                table = self.dict_tab_tables[name_tables.index(names[i])]
                k = table.rowCount()
                table.setRowCount(table.rowCount() + 1)
                for j, elem in enumerate(data[i]):
                    table.setItem(k, j, QTableWidgetItem(str(elem)))

        self.quality_calories /= 2
        self.quality_proteins /= 2
        self.quality_fats /= 2
        self.quality_carbohydrates /= 2
        print(self.quality_calories, self.quality_proteins, self.quality_fats, self.quality_carbohydrates)

    def get_date(self):

        self.calendar = Calendar(self.day, self)
        self.calendar.show()

    def set_headers(self):
        self.tableWidget_lunch.setColumnCount(6)
        self.tableWidget_lunch.setHorizontalHeaderLabels(["Название", "Масса", "Калории", "Белки", "Жиры", "Углеводы"])
        self.tableWidget_lunch.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.tableWidget_breakfast.setColumnCount(6)
        self.tableWidget_breakfast.setHorizontalHeaderLabels(
            ["Название", "Масса", "Калории", "Белки", "Жиры", "Углеводы"])
        self.tableWidget_breakfast.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.tableWidget_dinner.setColumnCount(6)
        self.tableWidget_dinner.setHorizontalHeaderLabels(["Название", "Масса", "Калории", "Белки", "Жиры", "Углеводы"])
        self.tableWidget_dinner.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.tableWidget_meal.setColumnCount(6)
        self.tableWidget_meal.setHorizontalHeaderLabels(["Название", "Масса", "Калории", "Белки", "Жиры", "Углеводы"])
        self.tableWidget_meal.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def del_product(self):

        dct_tables = {"break": "breakfast", "lunch": "lunch", "din": "dinner", "meal": "meal"}
        per = dct_tables[self.sender().objectName().split("_")[1]]
        table = self.dict_tab_tables[["breakfast", "lunch", "dinner", "meal"].index(per)]
        select_item = table.selectedItems()

        cursor = self.connection.cursor()

        for i in range(len(select_item)):
            item = select_item[i]
            info = []
            for c in range(6):
                info.append(table.item(item.row(), c).text())

            cursor.execute(f"DELETE FROM food_day WHERE id_user='{self.login}' AND day='{self.day}' AND period='{per}'"
                           f"AND product_name='{info[0]}' AND product_weight={float(info[1])}")
            self.connection.commit()

            self.quality_calories -= float(info[2])
            self.quality_proteins -= float(info[3])
            self.quality_fats -= float(info[4])
            self.quality_carbohydrates -= float(info[5])
            self.load_tables()
            self.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())