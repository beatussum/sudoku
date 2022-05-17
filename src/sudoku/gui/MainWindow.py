from sudoku.core import sudoku_grid
from sudoku.gui import AboutWindow

from sudoku.gui.Ui_MainWindow import Ui_MainWindow

from PyQt5 import QtCore, QtWidgets

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent: QtWidgets.QWidget = None) -> None:
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

        self.about_action.triggered.connect(self.about)
        self.clear_button.clicked.connect(self.sudoku_grid.clear)
        self.solve_button.clicked.connect(self.sudoku_grid.solve)

    @QtCore.pyqtSlot()
    def about(self) -> None:
        about_window = AboutWindow(self)
        about_window.show()
