import sys
import sqlite3

from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem, QHeaderView, QAbstractItemView

from .add_form_py import Ui_Form


class AddWindow(QWidget, Ui_Form):

    def __init__(self, main_table):
        super().__init__()
        self.setupUi(self)

        self.main_table = main_table
        self.connection = None
        self.cursor = None

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.load_data("""SELECT * FROM product""")
        self.flag_change = True

        self.text_search.textChanged.connect(lambda: self.search()
        if len(self.text_search.toPlainText()) and self.flag_change else None)

        self.table.cellClicked.connect(lambda: self.print_name(self.table.selectedItems()[0])
        if self.table.selectedItems()[0].column() == 0 else None)

        self.textEdit_weight.textChanged.connect(self.set_text_info)

        self.button_cancel.clicked.connect(self.close)
        self.button_add.clicked.connect(self.add_product)

    def load_data(self, query):

        self.connection = sqlite3.connect(r"C:\Users\Lenovo\PycharmProject\qt_project\create_sql_database\product_base.db")
        self.cursor = self.connection.cursor()
        data = self.cursor.execute(query).fetchall()
        self.load_table(data)

    def load_table(self, data):
        data = list(map(lambda x: x[1:], data))
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Название", "Белки", "Жиры", "Углеводы", "Калории"])
        self.table.setRowCount(0)

        for i, row in enumerate(data):
            self.table.setRowCount(
                self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(elem)))

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def search(self):
        text = self.text_search.toPlainText()
        self.load_data(f"""SELECT * FROM product WHERE name LIKE '%{text.capitalize()}%' 
        OR name LIKE '%{text.lower()}%' OR name LIKE '%{text.lower()}%'""")

    def print_name(self, item):

        self.flag_change = False
        self.text_search.clear()
        self.text_search.setText(item.text())
        self.textEdit_weight.setText("100")
        self.set_text_info()
        self.flag_change = True

    def set_text_info(self):

        name = self.text_search.toPlainText()
        try:
            weight = float(self.textEdit_weight.toPlainText()) / 100
        except ValueError:
            weight = 0
        try:
            data = self.cursor.execute(f"""SELECT * FROM product WHERE name LIKE '{name}'""").fetchall()[0]
            self.label_info.setText(f"Калории: {round(data[-1] * weight, 1)}\n"
                                    f"Белки: {round(data[2] * weight, 1)}\n"
                                    f"Жиры: {round(data[3] * weight, 1)}\n"
                                    f"Углеводы: {round(data[4] * weight, 1)}")
        except IndexError:
            return

    def add_product(self):

        info = self.label_info.text().split('\n')
        info = list(map(lambda x: x.split()[-1], info))
        data = [self.text_search.toPlainText(), self.textEdit_weight.toPlainText(), *info]
        row = self.main_table.rowCount()
        self.main_table.setRowCount(row + 1)
        for i in range(6):
            self.main_table.setItem(row, i, QTableWidgetItem(data[i]))
        self.close()



sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddWindow()
    ex.show()
    sys.exit(app.exec())