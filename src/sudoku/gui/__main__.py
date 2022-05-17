from sudoku.gui import MainWindow

from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

main = MainWindow()
main.show()

app.exec()
