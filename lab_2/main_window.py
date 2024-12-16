import sys
import os

from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

import first_script
import second_script
import third_script
import iterator


class Window(QMainWindow):
    def read_directory(self, elem: str) -> None:
        """Read directory file and print text on labal opinion"""
        directory = elem.split(",")
        with open(directory[1], "r", encoding="utf-8") as f:
            text = f.read()
        text = text.split("\n")
        spisok = []
        for element in text:
            for i in range(1, (len(element) // 100) + 1):
                if element[100 * i - 1] != " ":
                    j = 100 * i - 1
                    while element[j] != " ":
                        j = j - 1
                    element = element[:j] + "\n" + element[j:]
                else:
                    element = element[:100 * i - 1] + "\n" + element[100 * i - 1:]
            spisok.append(element)
        # бинарный поиск
        self.title_opinion.clear()
        self.plus_opinion.clear()
        self.minus_opinion.clear()
        self.text_opinion.clear()

        self.title_opinion.setText(spisok[0])
        self.plus_opinion.setText(spisok[2])
        self.minus_opinion.setText(spisok[3])
        self.text_opinion.setText(spisok[4])

        self.title_opinion.adjustSize()
        self.plus_opinion.adjustSize()
        self.minus_opinion.adjustSize()
        self.text_opinion.adjustSize()

    def click_button_first_star(self) -> None:
        """first star button and work iterat1"""
        elem = str(next(self.iterat_1))
        if elem == "['Абсолютный путь к файлу,Относительный путь к файлу,номер звезды']":
            elem = str(next(self.iterat_1))
        self.read_directory(elem)

    def click_button_second_star(self) -> None:
        """second star button and work iterat2"""
        elem = str(next(self.iterat_2))
        if elem == "['Абсолютный путь к файлу,Относительный путь к файлу,номер звезды']":
            elem = str(next(self.iterat_2))
        self.read_directory(elem)

    def click_button_third_star(self) -> None:
        """"third star button and work iterat3"""
        elem = str(next(self.iterat_3))
        if elem == "['Абсолютный путь к файлу,Относительный путь к файлу,номер звезды']":
            elem = str(next(self.iterat_3))
        self.read_directory(elem)

    def click_button_fourth_star(self) -> None:
        """fourth star button and work iterat4"""
        elem = str(next(self.iterat_4))
        if elem == "['Абсолютный путь к файлу,Относительный путь к файлу,номер звезды']":
            elem = str(next(self.iterat_4))
        self.read_directory(elem)

    def click_button_fifth_star(self) -> None:
        """"click fifth star button and work iterat5"""
        elem = str(next(self.iterat_5))
        if elem == "['Абсолютный путь к файлу,Относительный путь к файлу,номер звезды']":
            elem = str(next(self.iterat_5))
        self.read_directory(elem)

    def __init__(self) -> None:
        """"create a window object"""
        super(Window, self).__init__()
        if os.path.exists('classmates1.csv') == False:
            first_script.first_script("")

        self.iterat_1 = iterator.Iterator("classmates1.csv", 1)
        self.iterat_2 = iterator.Iterator("classmates1.csv", 2)
        self.iterat_3 = iterator.Iterator("classmates1.csv", 3)
        self.iterat_4 = iterator.Iterator("classmates1.csv", 4)
        self.iterat_5 = iterator.Iterator("classmates1.csv", 5)

        self.folderpath_dataset = ""
        while self.folderpath_dataset == "":
            self.folderpath_dataset = QtWidgets.QFileDialog.getExistingDirectory(
                self, 'Выберите путь до dataset')
        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Путь до dataset:" + self.folderpath_dataset)
        self.main_text.move(0, 575)
        self.main_text.adjustSize()
        self.main_text.setFont(QFont("Times", 36))

        self.button_succesesful = QtWidgets.QLabel(self)

        self.title_opinion = QtWidgets.QLabel(self)
        self.title_opinion.move(0, 275)

        self.plus_opinion = QtWidgets.QLabel(self)
        self.plus_opinion.move(0, 325)

        self.minus_opinion = QtWidgets.QLabel(self)
        self.minus_opinion.move(0, 375)

        self.text_opinion = QtWidgets.QLabel(self)
        self.text_opinion.move(0, 425)

        self.button_create_dataset = QtWidgets.QPushButton(self)
        self.button_create_dataset.move(0, 30)
        self.button_create_dataset.setText("Создать dataset")
        self.button_create_dataset.setFixedWidth(200)
        self.button_create_dataset.clicked.connect(first_script.first_script)

        self.button_recreate_dataset = QtWidgets.QPushButton(self)
        self.button_recreate_dataset.move(0, 90)
        self.button_recreate_dataset.setText("Перекопировать dataset")
        self.button_recreate_dataset.setFixedWidth(200)
        self.button_recreate_dataset.clicked.connect(second_script.second_script)

        self.button_copy_random_dataset = QtWidgets.QPushButton(self)
        self.button_copy_random_dataset.move(0, 150)
        self.button_copy_random_dataset.setText("Перемешать элементы")
        self.button_copy_random_dataset.setFixedWidth(200)
        self.button_copy_random_dataset.clicked.connect(third_script.third_script)

        self.button_first_star = QtWidgets.QPushButton(self)
        self.button_second_star = QtWidgets.QPushButton(self)
        self.button_third_star = QtWidgets.QPushButton(self)
        self.button_fourth_star = QtWidgets.QPushButton(self)
        self.button_fifth_star = QtWidgets.QPushButton(self)

        self.button_first_star.move(700, 30)
        self.button_second_star.move(700, 60)
        self.button_third_star.move(700, 90)
        self.button_fourth_star.move(700, 120)
        self.button_fifth_star.move(700, 150)

        self.button_first_star.setText("⭐    ")
        self.button_second_star.setText("⭐⭐   ")
        self.button_third_star.setText("⭐⭐⭐  ")
        self.button_fourth_star.setText("⭐⭐⭐⭐ ")
        self.button_fifth_star.setText("⭐⭐⭐⭐⭐")

        self.button_first_star.clicked.connect(self.click_button_first_star)
        self.button_second_star.clicked.connect(self.click_button_second_star)
        self.button_third_star.clicked.connect(self.click_button_third_star)
        self.button_fourth_star.clicked.connect(self.click_button_fourth_star)
        self.button_fifth_star.clicked.connect(self.click_button_fifth_star)

        self.style_text = ""
        self.style_button = "background-color: rgb(55, 6, 181);"
        self.button_copy_random_dataset.setStyleSheet(self.style_button)
        self.button_create_dataset.setStyleSheet(self.style_button)
        self.button_recreate_dataset.setStyleSheet(self.style_button)
        self.button_first_star.setStyleSheet(self.style_button)
        self.button_second_star.setStyleSheet(self.style_button)
        self.button_third_star.setStyleSheet(self.style_button)
        self.button_fourth_star.setStyleSheet(self.style_button)
        self.button_fifth_star.setStyleSheet(self.style_button)

        self.title_opinion.setFont(QFont("Times", 13))
        self.main_text.setFont(QFont("Times", 13))
        self.plus_opinion.setFont(QFont("Times", 13))
        self.minus_opinion.setFont(QFont("Times", 13))
        self.text_opinion.setFont(QFont("Times", 13))


def application() -> None:
    """"Start aplication mainwindow"""
    app = QApplication(sys.argv)
    window = Window()
    window.setFixedSize(800, 600)
    window.setObjectName("MainWindow")
    window.setStyleSheet(
        "#MainWindow{border-image:url(phon.jpg)}")
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()