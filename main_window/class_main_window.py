import sys

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QMainWindow, QApplication, QHeaderView, QVBoxLayout
from main_window_py import Ui_MainWindow
from add_form.class_add_form import AddWindow

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from main_window.test import MatplotlibWidget


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.dict_tab_tables = {0: self.tableWidget_breakfast,
                                1: self.tableWidget_lunch,
                                2: self.tableWidget_dinner,
                                3: self.tableWidget_meal}

        self.pushButton_break_add.clicked.connect(self.add_product)
        self.pushButton_lunch_add.clicked.connect(self.add_product)
        self.pushButton_din_add.clicked.connect(self.add_product)
        self.pushButton_meal_add.clicked.connect(self.add_product)

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

        self.quality_proteins = 0
        self.quality_fats = 0
        self.quality_carbohydrates = 0
        self.quality_calories = 0

        self.count_change = 0
        self.tableWidget_breakfast.itemChanged.connect(self.check_change)


        self.fig, self.ax = plt.subplots()

        self.ax.pie([1, 1, 1], wedgeprops=dict(width=0.5,))

        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self)

        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.canvas)

        self.setLayout(self.vbox)
        self.vbox.setGeometry(QRect(450, 70, 200, 200))


    def getFigure(self):
        return self.fig

    def draw(self):
        self.ax.pie([self.quality_proteins, self.quality_fats, self.quality_carbohydrates], wedgeprops=dict(width=0.5,))
        self.canvas.draw()

    def add_product(self):

        self.add_window = AddWindow(self.dict_tab_tables[self.tabWidget_menu.currentIndex()])
        self.add_window.show()

    def calc_calories(self):

        i = self.tabWidget_menu.currentIndex()
        countRow = self.dict_tab_tables[i].rowCount()
        self.quality_calories += float(self.dict_tab_tables[i].item(countRow - 1, 2).text())
        self.quality_proteins += float(self.dict_tab_tables[i].item(countRow - 1, 3).text())
        self.quality_fats += float(self.dict_tab_tables[i].item(countRow - 1, 4).text())
        self.quality_carbohydrates += float(self.dict_tab_tables[i].item(countRow - 1, 5).text())

        self.count_change = 0

        self.draw()



    def check_change(self):

        if self.count_change == 5:
            self.calc_calories()
        else:
            self.count_change += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())