import sys

from PyQt5.QtWidgets import QWidget, QApplication
from .calendar_window_py import Ui_Form
from datetime import datetime


class Calendar(QWidget, Ui_Form):

    def __init__(self, day, main_obj):
        super(Calendar, self).__init__()
        self.setupUi(self)

        self.setMinimumSize(self.size())
        self.setMaximumSize(self.size())

        self.obj = day
        self.main_obj = main_obj

        self.calendarWidget.setSelectedDate(day)
        self.dateEdit.setDate(self.calendarWidget.selectedDate())

        self.calendarWidget.selectionChanged.connect(lambda: self.dateEdit.setDate(self.calendarWidget.selectedDate()))
        self.pushButton_ok.clicked.connect(self.return_and_close)
        self.pushButton_show.clicked.connect(self.show_date)

    def show_date(self):
        self.calendarWidget.setSelectedDate(self.dateEdit.date())

    def return_and_close(self):

         self.obj = self.calendarWidget.selectedDate()
         self.main_obj.day = datetime.strptime("-".join([str(self.obj.year()),
                                                         str(self.obj.month()), str(self.obj.day())]), "%Y-%m-%d").date()
         self.main_obj.day_list = str(self.main_obj.day).split("-")
         self.main_obj.set_day()
         self.main_obj.load_tables()
         self.close()


