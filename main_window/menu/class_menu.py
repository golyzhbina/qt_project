import sys
from PyQt5.QtWidgets import QApplication, QWidget
from .menu_form_py import Ui_Form
from reg_window.class_calc import CalcCalories
from main_window.add_in_base.class_add_base import AddProduct



class Menu(QWidget, Ui_Form):

    def __init__(self, obj):
        super(Menu, self).__init__()
        self.setupUi(self)

        self.obj = obj
        self.login = self.obj.login

        self.pushButton_add_prod.clicked.connect(self.add_product)
        self.pushButton_calc.clicked.connect(self.calc)
        self.pushButton_ex.clicked.connect(self.ex)

    def add_product(self):

        self.add_wind = AddProduct(self.login)
        self.add_wind.show()

    def ex(self):
        self.obj.ex()
        self.close()

    def calc(self):

        self.calc_wind = CalcCalories(self.obj)
        self.calc_wind.show()

