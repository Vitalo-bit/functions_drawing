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
from math import sin, cos, tan, sqrt


class Function_draw(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('project.ui', self)
        self.drawButton.clicked.connect(self.painting)
        self.backButton.clicked.connect(self.exit)
        self.mainMenu = None

    def painting(self):
        plt.ioff()
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_title('Graph:', fontsize=12)
        if self.lineEdit.text() == '' and self.NoneRadioButton.isChecked():
            self.error_Label.setText('Write a func')
        elif self.SinRadioButton.isChecked():
            plt.axis([-10, 10, -10, 10])
            x = np.arange(-10, 4 * np.pi, 0.1)  # start,stop,step
            try:
                y = np.sin(eval(self.lineEdit.text()))
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
            except:
                self.error_Label.setText('Try again')
        elif self.TanRadioButton.isChecked():
            plt.axis([-10, 10, -10, 10])
            x = np.arange(-10, 4 * np.pi, 0.1)  # start,stop,step
            try:
                y = np.tan(eval(self.lineEdit.text()))
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
            except:
                self.error_Label.setText('Try again')
        elif self.CosRadioButton.isChecked():
            plt.axis([-10, 10, -10, 10])
            x = np.arange(-10, 4 * np.pi, 0.1)  # start,stop,step
            try:
                y = np.cos(eval(self.lineEdit.text()))
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
            except:
                self.error_Label.setText('Try again')
        else:
            try:
                x = np.arange(-10, 10, 0.01)
                y = eval(self.lineEdit.text())  # планирую сделать безопасный eval, с проверкой на содержимое lineEdit'а
                specials = {'sqrt': sqrt}
                plt.axis([x[0], x[-1], min(y) - y[len(y) // 2], max(y) + y[len(y) // 2]]) #min(y) - 10, #max(y) + 10
                # не работает для sin, cos и тригонометрических функций
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
            except:
                self.error_Label.setText('Try again')

    def exit(self):
        self.close()
        self.mainMenu.show()

    def addMainMenu(self, mainMenu):
        self.mainMenu = mainMenu


class Diagram_draw(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('diagram.ui', self)  # делал конкретный путь, можно заменить
        self.backButton.clicked.connect(self.exit)
        self.mainMenu = None

    def exit(self):
        self.close()
        self.mainMenu.show()

    def addMainMenu(self, mainMenu):
        self.mainMenu = mainMenu


class Autorization(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('authorization.ui', self)
        self.mainMenu = None
        self.check = False
        self.registerButton.clicked.connect(self.user_registration)
        self.loginButton.clicked.connect(self.user_login)
        self.count = 0
        self.changebutton.clicked.connect(self.passchange)
        self.changeLabel.hide()
        self.lineEdit.hide()
        self.changebutton.hide()

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
        else:
            sql.execute(f"""SELECT PASSWORD FROM users WHERE password = '{user_password}' AND login = '{user_login}'""")
            if sql.fetchone() is None:
                self.warningLabel.setText('Wrong password')
                self.count += 1
                if self.count < 3:
                    self.changeLabel.hide()
                    self.lineEdit.hide()
                    self.changebutton.hide()
                elif self.count >= 3:
                    self.changeLabel.show()
                    self.lineEdit.show()
                    self.changebutton.show()
            else:
                self.check = True
                self.mainMenu.setEnabled(True)
                self.count = 0
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

    def passchange(self):
        db = sqlite3.connect('accounts.sqlite')
        sql = db.cursor()  # work with database
        user_login = self.nickEdit.text()
        user_password = self.lineEdit.text()
        print(user_password, user_login)
        if len(user_password) > 4:
            sql.execute(f"""UPDATE users SET password = '{user_password}' WHERE login = '{user_login}'""")
            db.commit()
            self.check = True
            self.mainMenu.setEnabled(True)
            self.close()
        else:
            self.labelSymb.setText('Less than 5 symbols')

    def checkAutorization(self):
        return self.check

    def addMenu(self, menu):
        self.mainMenu = menu


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('mainMenu.ui', self)

        self.function_draw = None
        self.diagram_draw = None

        self.startButton.clicked.connect(self.startFunc)
        self.exitButton.clicked.connect(self.exit)
        self.pushButton.clicked.connect(self.startDiagram)

    def exit(self):
        sys.exit()

    def startFunc(self):
        self.close()
        self.function_draw.show()
        self.function_draw.setEnabled(True)

    def addFunc(self, function_draw):
        self.function_draw = function_draw

    def addDiagram(self, diagram_draw):
        self.diagram_draw = diagram_draw

    def startDiagram(self):
        self.close()
        self.diagram_draw.show()
        self.diagram_draw.setEnabled(True)


class FuncPunk(QObject):
    def __init__(self):
        super().__init__()
        self.fuction_draw = Function_draw()
        self.fuction_draw.hide()
        self.fuction_draw.setEnabled(False)

        self.mainMenu = MainMenu()
        self.mainMenu.addFunc(self.fuction_draw)
        self.mainMenu.show()
        self.mainMenu.setEnabled(False)
        self.fuction_draw.addMainMenu(self.mainMenu)

        self.autorization = Autorization()
        self.autorization.addMenu(self.mainMenu)
        self.autorization.show()

        self.diagram_draw = Diagram_draw()
        self.diagram_draw.addMainMenu(self.mainMenu)
        self.mainMenu.addDiagram(self.diagram_draw)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FuncPunk()
    sys.exit(app.exec_())
