import numpy as np
import matplotlib.pyplot as plt
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PIL import Image

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'D:\functions_drawing\venv\project_yandex\project.ui', self)
        self.pushButton.clicked.connect(self.painting)
    def painting(self):
        plt.ioff()
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_title('Graph:', fontsize=12)
        plt.axis([-10, 10, -10, 10])
        x = np.arange(-10, 10, 0.01)
        y = eval(self.lineEdit.text())
        ax.grid(color='grey',   # цвет линий # Сетка графика
                linewidth=1,    # толщина # Сетка графика
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



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
    