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
import sqlite3

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
        self.check = False

        self.registerButton.clicked.connect(self.user_registration)
        self.loginButton.clicked.connect(self.user_login)


    def user_login(self):
        db = sqlite3.connect('accounts.sqlite')
        sql = db.cursor()  # work with database

        sql.execute("""CREATE TABLE IF NOT EXISTS users (
            login TEXT, 
            password TEXT 
        )""")

        db.commit()
        user_login = self.nickEdit.text()
        user_password = self.passEdit.text()
        # reg
        sql.execute(f"""SELECT LOGIN FROM users WHERE login = '{user_login}'""")
        if sql.fetchone() is None:
            self.warningLabel.setText('User is not registered')
            #sql.execute(f"""INSERT INTO users VALUES (?, ?)""", (user_login, user_password))
            #db.commit()
            #print('Your account is registered')
        else:
            sql.execute(f"""SELECT LOGIN FROM users WHERE login = '{user_password}'""")
            if sql.fetchone() is None:
                self.warningLabel.setText('Wrong password')
            else:
                self.check = True
                self.mainMenu.setEnabled(True)
                self.close()
    def user_registration(self):
        db = sqlite3.connect('accounts.sqlite')
        sql = db.cursor()  # work with database

        sql.execute("""CREATE TABLE IF NOT EXISTS users (
            login TEXT, 
            password TEXT 
        )""")

        db.commit()
        user_login = self.nickEdit.text()
        user_password = self.passEdit.text()
        # reg
        if len(user_login) < 4:
            self.warningLabel.setText('Too small login')
            self.nickEdit.setText('')
            self.passEdit.setText('')
        elif len(user_password) < 4:
            self.warningLabel.setText('Too small password')
            self.nickEdit.setText('')
            self.passEdit.setText('')
        else:
            sql.execute(f"""SELECT LOGIN FROM users WHERE login = '{user_login}'""")
            if sql.fetchone() is None:
                sql.execute(f"""INSERT INTO users VALUES (?, ?)""", (user_login, user_password))
                db.commit()
                self.check = True
                self.mainMenu.setEnabled(True)
                self.close()
            else:
                self.warningLabel.setText('User is already registered')
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


        self.autorization = Autorization()
        self.autorization.addMenu(self.mainMenu)
        self.autorization.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FuncPunk()
    sys.exit(app.exec_())
