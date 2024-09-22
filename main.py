import sys
from PyQt6 import QtWidgets

from src.program_shell import Ui_MainWindow

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.click_button()
    MainWindow.show()
    sys.exit(app.exec())
