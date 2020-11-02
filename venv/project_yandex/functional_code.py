import numpy as np
import matplotlib.pyplot as plt
import sys
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PIL import Image
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import pyqtSignal


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('project.ui', self)  # делал конкретный путь, можно заменить
        self.pushButton.clicked.connect(self.painting)

    def painting(self):
        plt.ioff()
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_title('Graph:', fontsize=12)
        plt.axis([-10, 10, -10, 10])
        x = np.arange(-10, 10, 0.01)
        y = eval(self.lineEdit.text())  # планирую сделать безопасный eval, с проверкой на содержимое lineEdit'а
        ax.grid(color='grey',  # цвет линий # Сетка графика
                linewidth=1,  # толщина # Сетка графика
                linestyle='-')  # начертание # Сетка графика
        plt.plot(x, y, "g-")  # Построение графика
        # X - axis
        ax.axhline(y=0, color='k')
        # Y - axis
        ax.axvline(x=0, color='k')
        plt.savefig('abc.png')
        image = Image.open('abc.png')
        new_image = image.resize((491, 491))
        new_image.save('a1b1c1.png')
        self.graphic_label.setPixmap(QPixmap('a1b1c1.png'))


class Autorization(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('authorization.ui', self)
        self.mainMenu = None
        self.bd = dict()
        self.check = False

        self.registerButton.clicked.connect(self.register)
        self.loginButton.clicked.connect(self.login)

    def addBd(self, bd):
        self.bd = bd

    def getBd(sefl):
        return self.bd

    def register(self):
        name = self.nickEdit.text()
        password = self.passEdit.text()
        if (name in self.bd.keys()):
            if (len(name) < 4 and len(password) < 4):
                self.warningLabel.setText("Short Nickname or password")
            else:
                self.warningLabel.setText("Username is taken!")
        else:
            if (len(name) < 4 and len(password) < 4):
                self.warningLabel.setText("Short Nickname or password")
            else:
                self.bd[name] = password
                self.mainMenu.setEnabled(True)
                self.close()
                return True

    def login(self):                                                ###адаптировать под SQL
        name = self.nickEdit.text()
        password = self.passEdit.text()
        if (name in self.bd.keys() and len(name) > 3):
            if (self.bd[name] != password and len(password) < 4):
                self.warningLabel.setText("Wrong Password!")
            else:
                self.chek = True
                self.mainMenu.setEnabled(True)
                self.close()
        else:
            self.warningLabel.setText("Wrong Nickname!")

    def checkAutorization(self):
        return self.check

    def addMenu(self, menu):
        self.mainMenu = menu


class FuncPunk(QObject):
    def __init__(self):
        super().__init__()
        self.mainMenu = MyWidget()
        self.mainMenu.show()
        self.mainMenu.setEnabled(False)

        self.bd = dict()                                            ###адаптировать под SQL
        self.bd["1234"] = "1234"

        self.autorization = Autorization()
        self.autorization.addMenu(self.mainMenu)
        self.autorization.addBd(self.bd)
        self.autorization.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FuncPunk()
    sys.exit(app.exec_())
