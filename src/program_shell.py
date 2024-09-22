import random
import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox


class Ui_MainWindow(object):

    def __init__(self):
        super().__init__()
        self.random_number = self.__get_random_number()
        self.__count = 9  # добавить количествао попыток

    def setupUi(self, MainWindow) -> None:
        """Тело программы"""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(0, 0, 331, 80))
        self.lcdNumber.setStyleSheet(
            "background-color: qradialgradient(spread:pad, cx:0.511682,"
            " cy:0.488, radius:0.984, fx:0.517, fy:0.488636, stop:0.170455"
            " rgba(0, 143, 137, 61), stop:0.431818 rgba(0, 143, 137, 153),"
            " stop:0.4375 rgba(0, 143, 137, 153), stop:1 rgba(0, 0, 0, 255));"
        )
        self.lcdNumber.setObjectName("lcdNumber")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 0, 310, 480))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(
            "background-color: qradialgradient(spread:pad, cx:0.511682,"
            " cy:0.488, radius:0.984, fx:0.517, fy:0.488636, stop:0.170455"
            " rgba(0, 143, 137, 61), stop:0.431818 rgba(0, 143, 137, 153),"
            " stop:0.4375 rgba(0, 143, 137, 153), stop:1 rgba(0, 0, 0, 255));"
        )
        self.label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.label.setObjectName("label")
        self.pbn_1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pbn_1.setGeometry(QtCore.QRect(0, 280, 110, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(56)
        font.setBold(True)
        font.setWeight(75)
        self.pbn_1.setFont(font)
        self.pbn_1.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background-color: qradialgradient(spread:pad,"
            " cx:0.511682, cy:0.488, radius:0.865905, fx:0.511364,"
            " fy:0.482955, stop:0.1875 rgba(0, 143, 137, 255),"
            " stop:1 rgba(255, 255, 255, 255));"
        )
        self.pbn_1.setObjectName("pbn_1")
        self.pbn_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pbn_2.setGeometry(QtCore.QRect(110, 280, 110, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(56)
        font.setBold(True)
        font.setWeight(75)
        self.pbn_2.setFont(font)
        self.pbn_2.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background-color: qradialgradient(spread:pad, cx:0.511682,"
            " cy:0.488, radius:0.865905, fx:0.511364, fy:0.482955,"
            " stop:0.1875 rgba(0, 143, 137, 255), stop:1 rgba(255, 255, 255, 255));"
        )
        self.pbn_2.setObjectName("pbn_2")
        self.pbn_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pbn_3.setGeometry(QtCore.QRect(220, 280, 110, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(56)
        font.setBold(True)
        font.setWeight(75)
        self.pbn_3.setFont(font)
        self.pbn_3.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background-color: qradialgradient(spread:pad, cx:0.511682,"
            " cy:0.488, radius:0.865905, fx:0.511364, fy:0.482955,"
            " stop:0.1875 rgba(0, 143, 137, 255), stop:1 rgba(255, 255, 255, 255));"
        )
        self.pbn_3.setObjectName("pbn_3")
        self.pbn_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pbn_4.setGeometry(QtCore.QRect(0, 180, 110, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(56)
        font.setBold(True)
        font.setWeight(75)
        self.pbn_4.setFont(font)
        self.pbn_4.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background-color: qradialgradient(spread:pad, cx:0.511682,"
            " cy:0.488, radius:0.865905, fx:0.511364, fy:0.482955,"
            " stop:0.1875 rgba(0, 143, 137, 255), stop:1 rgba(255, 255, 255, 255));"
        )
        self.pbn_4.setObjectName("pbn_4")
        self.pbn_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pbn_5.setGeometry(QtCore.QRect(110, 180, 110, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(56)
        font.setBold(True)
        font.setWeight(75)
        self.pbn_5.setFont(font)
        self.pbn_5.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background-color: qradialgradient(spread:pad, cx:0.511682,"
            " cy:0.488, radius:0.865905, fx:0.511364, fy:0.482955,"
            " stop:0.1875 rgba(0, 143, 137, 255), stop:1 rgba(255, 255, 255, 255));"
        )
        self.pbn_5.setObjectName("pbn_5")
        self.pbn_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pbn_6.setGeometry(QtCore.QRect(220, 180, 110, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(56)
        font.setBold(True)
        font.setWeight(75)
        self.pbn_6.setFont(font)
        self.pbn_6.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background-color: qradialgradient(spread:pad, cx:0.511682,"
            " cy:0.488, radius:0.865905, fx:0.511364, fy:0.482955,"
            " stop:0.1875 rgba(0, 143, 137, 255), stop:1 rgba(255, 255, 255, 255));"
        )
        self.pbn_6.setObjectName("pbn_6")
        self.pbn_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pbn_7.setGeometry(QtCore.QRect(0, 80, 110, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(56)
        font.setBold(True)
        font.setWeight(75)
        self.pbn_7.setFont(font)
        self.pbn_7.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background-color: qradialgradient(spread:pad, cx:0.511682,"
            " cy:0.488, radius:0.865905, fx:0.511364, fy:0.482955,"
            " stop:0.1875 rgba(0, 143, 137, 255), stop:1 rgba(255, 255, 255, 255));"
        )
        self.pbn_7.setObjectName("pbn_7")
        self.pbn_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pbn_8.setGeometry(QtCore.QRect(110, 80, 110, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(56)
        font.setBold(True)
        font.setWeight(75)
        self.pbn_8.setFont(font)
        self.pbn_8.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background-color: qradialgradient(spread:pad, cx:0.511682,"
            " cy:0.488, radius:0.865905, fx:0.511364, fy:0.482955,"
            " stop:0.1875 rgba(0, 143, 137, 255), stop:1 rgba(255, 255, 255, 255));"
        )
        self.pbn_8.setObjectName("pbn_8")
        self.pbn_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pbn_9.setGeometry(QtCore.QRect(220, 80, 110, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(56)
        font.setBold(True)
        font.setWeight(75)
        self.pbn_9.setFont(font)
        self.pbn_9.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background-color: qradialgradient(spread:pad, cx:0.511682,"
            " cy:0.488, radius:0.865905, fx:0.511364, fy:0.482955,"
            " stop:0.1875 rgba(0, 143, 137, 255), stop:1 rgba(255, 255, 255, 255));"
        )
        self.pbn_9.setObjectName("pbn_9")
        self.pbn_zero = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pbn_zero.setGeometry(QtCore.QRect(110, 380, 110, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(56)
        font.setBold(True)
        font.setWeight(75)
        self.pbn_zero.setFont(font)
        self.pbn_zero.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background-color: qradialgradient(spread:pad, cx:0.511682,"
            " cy:0.488, radius:0.865905, fx:0.511364, fy:0.482955,"
            " stop:0.1875 rgba(0, 143, 137, 255), stop:1 rgba(255, 255, 255, 255));"
        )
        self.pbn_zero.setObjectName("pbn_zero")
        self.pbn_enter = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pbn_enter.setGeometry(QtCore.QRect(220, 380, 110, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.pbn_enter.setFont(font)
        self.pbn_enter.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background-color: qradialgradient(spread:pad, cx:0.511682,"
            " cy:0.488, radius:0.865905, fx:0.511364, fy:0.482955,"
            " stop:0.1875 rgba(0, 143, 137, 255), stop:1 rgba(255, 255, 255, 255));"
        )
        self.pbn_enter.setObjectName("pbn_enter")
        self.pbn_clear = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pbn_clear.setGeometry(QtCore.QRect(0, 380, 110, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.pbn_clear.setFont(font)
        self.pbn_clear.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background-color: qradialgradient(spread:pad, cx:0.511682,"
            " cy:0.488, radius:0.865905, fx:0.511364, fy:0.482955,"
            " stop:0.1875 rgba(0, 143, 137, 255), stop:1 rgba(255, 255, 255, 255));"
        )
        self.pbn_clear.setObjectName("pbn_clear")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow) -> None:
        """Присвоение названий кнопкам"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "bull_cow"))
        self.label.setText(_translate("MainWindow", "Результаты."))
        self.pbn_1.setText(_translate("MainWindow", "1"))
        self.pbn_2.setText(_translate("MainWindow", "2"))
        self.pbn_3.setText(_translate("MainWindow", "3"))
        self.pbn_4.setText(_translate("MainWindow", "4"))
        self.pbn_5.setText(_translate("MainWindow", "5"))
        self.pbn_6.setText(_translate("MainWindow", "6"))
        self.pbn_7.setText(_translate("MainWindow", "7"))
        self.pbn_8.setText(_translate("MainWindow", "8"))
        self.pbn_9.setText(_translate("MainWindow", "9"))
        self.pbn_zero.setText(_translate("MainWindow", "0"))
        self.pbn_enter.setText(_translate("MainWindow", "Enter"))
        self.pbn_clear.setText(_translate("MainWindow", "Clear"))

    def click_button(self) -> None:
        """Возвращение значения при нажатии на кнопку"""
        self.pbn_1.clicked.connect(lambda: self.add_digit(1))
        self.pbn_2.clicked.connect(lambda: self.add_digit(2))
        self.pbn_3.clicked.connect(lambda: self.add_digit(3))
        self.pbn_4.clicked.connect(lambda: self.add_digit(4))
        self.pbn_5.clicked.connect(lambda: self.add_digit(5))
        self.pbn_6.clicked.connect(lambda: self.add_digit(6))
        self.pbn_7.clicked.connect(lambda: self.add_digit(7))
        self.pbn_8.clicked.connect(lambda: self.add_digit(8))
        self.pbn_9.clicked.connect(lambda: self.add_digit(9))
        self.pbn_zero.clicked.connect(lambda: self.add_digit(0))
        self.pbn_enter.clicked.connect(lambda: self.add_digit(self.pbn_enter.text()))
        self.pbn_clear.clicked.connect(lambda: self.add_digit(self.pbn_clear.text()))

    def _new_windows_error(self, name_window: str, message: str) -> None:
        """Всплывающее окно ошибки"""
        message_window = QMessageBox()
        message_window.setWindowTitle(name_window)
        message_window.setText(message)
        message_window.setIcon(QMessageBox.Icon.Warning)
        message_window.exec()

    def _windows_message(self, name_window: str, message: str) -> None:
        """Всплывающее окно выбора условия"""
        message_window = QMessageBox()
        message_window.setWindowTitle(name_window)
        message_window.setText(message)
        message_window.setIcon(QMessageBox.Icon.Information)
        message_window.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Close)
        message_window.buttonClicked.connect(self.__action_press)
        message_window.exec()

    def __action_press(self, btn) -> None:
        """Проверка нажатия на кнопку всплывающего окна
        Ok: Продолжение работы, обнуление данных
        Close: Выход из программы"""
        if btn.text() == "OK":
            self.random_number = self.__get_random_number()
            self.__count = 10
            self.label.setText("")
        else:
            sys.exit()

    def add_print_display_text(self, text: str) -> None:
        "Вывод текста в информационное поле"
        self.label.setText(self.label.text() + text)

    def add_digit(self, digit: int | str) -> None:
        """Вывод значение в цифровое поле"""
        current_number = self.lcdNumber.value()
        if digit == "Enter":
            # вставить фунцию проверки current_number на быков
            self.input_number = str(round(current_number))
            self._logic_answer()
            digit = 0
            current_number = 0
        if digit == "Clear":
            new_number = current_number // 10
        else:
            new_number = current_number * 10 + digit
        if new_number < 10000:
            self.lcdNumber.display(new_number)

    def __get_random_number(self) -> int:
        """Рандомное четырехзначное число"""
        random_number = random.randint(1000, 9999)
        return random_number

    def __guess_number(self, number, input_number) -> tuple:
        """Логика выдачи подсказок"""
        bull = []
        cow = []
        number = str(number)
        for i in range(4):
            if input_number[i] == number[i]:
                bull.append(input_number[i])
            elif number[i] in input_number:
                cow.append(number[i])
        return bull, cow

    def _logic_answer(self) -> None:
        """Основная логика выдачи ответов"""
        # print(self.random_number)  # убрать в конце
        if len(self.input_number) == 4:
            bull, cow = self.__guess_number(self.random_number, self.input_number)
            answer_string = (
                f"\nЧисло: {self.input_number} Быки:{len(bull)} Коровы:{len(cow)}\nПопыток осталось: {self.__count}"
            )
            self.add_print_display_text(answer_string)
            if len(bull) == 4:
                message_win = (f"Поздравляю вы угадали число!!!\n"
                               f" Загаданное число: {self.random_number}"
                               f"\n Желаете начать новую игру?")
                self._windows_message("ПОБЕДА!", message_win)
            if self.__count == 0:
                message_lose = (f"Загаданное число: {self.random_number}"
                                f"\n Желаете начать новую игру?")
                self._windows_message("ВЫ ПРОИГРАЛИ!", message_lose)
            self.__count -= 1
        else:
            self._new_windows_error("Неверный ввод", "Водите 4-х значное число!")
