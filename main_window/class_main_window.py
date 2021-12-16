from sqlite3 import connect

from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QColor, QBrush, QPalette, QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QHeaderView, QVBoxLayout, QTableWidgetItem
from .main_form_py import Ui_MainWindow
from .add_form.class_add_form import AddWindow
from .calendar_window.class_calendar import Calendar

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from numpy import array

from datetime import datetime


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, calories, login, hello_wind):
        super().__init__()
        self.setupUi(self)

        self.setMinimumSize(self.size())
        self.setMaximumSize(self.size())

        self.hello_wind = hello_wind
        self.login = login
        self.label_login.setText(f"Логин: {login}  ")
        self.label_login.setFont(QFont("Book Antiqua", 11, QFont.Bold))
        palette = self.label_login.palette()
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        self.label_login.setPalette(palette)
        self.label_login.setAlignment(Qt.AlignRight)

        self.tabWidget_menu.setCurrentIndex(0)

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

        self.pushButton_ex.clicked.connect(self.ex)

        self.set_headers()

        self.quality_proteins = 0
        self.quality_fats = 0
        self.quality_carbohydrates = 0
        self.quality_calories = 0

        self.calories_day = calories
        palette = self.label_cal_day.palette()
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        self.label_cal_day.setPalette(palette)
        self.label_cal_day.setText(f"Норма калорий: {str(self.calories_day)}  ")
        self.label_cal_day.setFont(QFont("Book Antiqua", 11, QFont.Bold))
        self.label_cal_day.setAlignment(Qt.AlignRight)

        self.tableWidget_breakfast.itemClicked.connect(self.select_row)
        self.tableWidget_lunch.itemClicked.connect(self.select_row)
        self.tableWidget_dinner.itemClicked.connect(self.select_row)
        self.tableWidget_meal.itemClicked.connect(self.select_row)

        self.dict_months = {'01': "января", '02': "февраля", '03': "марта", '04': "апреля", '05': "мая",
                            '06': "июня", '07': "июля", '08': "августа", '09': "сентября", '10': "октября",
                            '11': "ноября", '12': "декабря"}

        self.dict_week = {'0': "Понедельник", '1': "Втроник", '2': "Среда", '3': "Четверг",
                          '4': "Пятница", '5': "Суббота", '6': "Воскресенье"}

        self.day = datetime.now().date()
        self.day_list = str(datetime.now().date()).split("-")

        self.set_day()
        self.set_info()

        self.pushButton_get_day.clicked.connect(self.get_date)

        self.fig, self.ax = plt.subplots()
        self.ax.pie(array([[1], [1], [1]]).sum(axis=1), radius=1, wedgeprops=dict(width=0.3, edgecolor='w'))

        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self)

        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.canvas)

        self.setLayout(self.vbox)
        self.vbox.setGeometry(QRect(420, 50, 250, 250))

        self.load_tables()

    def getFigure(self):
        return self.fig

    def draw(self):

        if self.quality_calories > self.calories_day:

            self.ax.pie(array([[self.quality_proteins], [self.quality_fats], [self.quality_carbohydrates]]).sum(axis=1),
                        radius=1, wedgeprops=dict(width=0.5, edgecolor='w'),
                        colors=["dimgray", "darkorange", "dodgerblue"])

        elif self.calories_day > self.quality_calories and self.quality_calories != 0:

            self.ax.pie(array([[self.quality_proteins], [self.quality_fats], [self.quality_carbohydrates]]).sum(axis=1),
                        radius=1, wedgeprops=dict(width=0.5, edgecolor='w'),
                        colors=["dimgray", "darkorange", "dodgerblue"])

        elif self.quality_calories == 0:

            self.ax.pie(array([[1], [1], [1]]).sum(axis=1),
                        radius=1, wedgeprops=dict(width=0.5, edgecolor='w'),
                        colors=["dimgray", "darkorange", "dodgerblue"])

        self.canvas.draw()

    def add_product(self):

        self.add_window = AddWindow(self.dict_tab_tables[self.tabWidget_menu.currentIndex()], self.day, self.login,
                            self.dict_tab_tables[self.tabWidget_menu.currentIndex()].objectName().split("_")[-1], self)
        self.add_window.show()

    def calc_calories(self):
        try:
            for i in range(4):
                table = self.dict_tab_tables[i]
                row = table.rowCount()
                for j in range(row):
                    if j == 2:
                        self.quality_calories += float(table.item(row, j).text())
                    elif j == 3:
                        self.quality_proteins += float(table.item(row, j).text())
                    elif j == 4:
                        self.quality_fats += float(table.item(row, j).text())
                    elif j == 5:
                        self.quality_carbohydrates += float(table.item(row, j).text())

            self.set_info()
        except AttributeError:
            return

        self.draw()

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
        if len(data) == 0:

            self.quality_calories = 0
            self.quality_proteins = 0
            self.quality_fats = 0
            self.quality_carbohydrates = 0
            self.set_info()
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
                    if j == 4:
                        table.item(k, j).setBackground(QColor(255, 120, 1))
                        table.item(k, j).setForeground(QBrush(QColor(255, 255, 255)))
                    elif j == 3:
                        table.item(k, j).setBackground(QColor(90, 90, 90))
                        table.item(k, j).setForeground(QBrush(QColor(255, 255, 255)))
                    elif j == 5:
                        table.item(k, j).setBackground(QColor(0, 143, 238))
                        table.item(k, j).setForeground(QBrush(QColor(255, 255, 255)))
        self.set_info()
        self.calc_calories()

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
        select_item = table.selectedItems()[::6]
        select_item = select_item[::-1]
        cursor = self.connection.cursor()

        for i in range(len(select_item)):
            item = select_item[i]
            info = []
            for c in range(6):
                info.append(table.item(item.row(), c).text())

            cursor.execute(f"DELETE FROM food_day WHERE id_user='{self.login}' AND day='{self.day}' AND period='{per}'"
                           f"AND product_name='{info[0]}' AND product_weight={float(info[1])}")
            self.connection.commit()

            row = select_item[i].row()
            table.removeRow(row)

            self.quality_calories -= float(info[2])
            self.quality_proteins -= float(info[3])
            self.quality_fats -= float(info[4])
            self.quality_carbohydrates -= float(info[5])
            self.draw()
            self.set_info()

    def select_row(self):
        per = self.sender().objectName().split("_")[1]
        table = self.dict_tab_tables[["breakfast", "lunch", "dinner", "meal"].index(per)]
        select_item = table.selectedItems()[0]
        row = select_item.row()
        for i in range(6):
            table.item(row, i).setSelected(True)

    def set_info(self):

        self.label_info.setText(f"Белки: {self.quality_proteins}\nЖиры: {self.quality_fats}\n"
                                f"Углеводы: {self.quality_carbohydrates}\nСъедено калорий: {self.quality_calories}\n"
                                f"Осталось калорий: {self.calories_day - self.quality_calories}")

    def ex(self):

        self.hello_wind.show()
        self.close()

    def set_day(self):

        palette = self.label_day.palette()
        palette.setColor(QPalette.WindowText, QColor(50, 50, 50))
        self.label_day.setPalette(palette)
        self.label_day.setText(f"{self.day_list[-1].replace('0', '')} {self.dict_months[self.day_list[1]]}, "
                               f"{self.dict_week[str(self.day.weekday())]}")