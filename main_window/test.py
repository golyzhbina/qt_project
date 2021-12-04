import sys

from PyQt5.QtWidgets import QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QWidget, QVBoxLayout


class MatplotlibWidget(QWidget):
    """
    Implements a Matplotlib figure inside a QWidget.
    Use getFigure() and redraw() to interact with matplotlib.

    Example::

        mw = MatplotlibWidget()
        subplot = mw.getFigure().add_subplot(111)
        subplot.plot(x,y)
        mw.draw()
    """

    def __init__(self, vals, object):
        super().__init__()
        # self.fig = Figure(size, dpi=dpi)

        ax.pie(vals, wedgeprops=dict(width=0.5))
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(object)

        self.vbox = QVBoxLayout(object)
        self.vbox.addWidget(self.canvas)

        self.setLayout(self.vbox)


    def getFigure(self):
        return self.fig

    def draw(self):
        self.canvas.draw()

sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook
