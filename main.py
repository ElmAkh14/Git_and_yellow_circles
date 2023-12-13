from sys import argv, exit
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        uic.loadUi('UI.ui', self)
        self.r = 0
        self.flag = False
        self.draw_button.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            qp.setPen(QColor(255, 255, 0))
            self.draw_ellipse(qp)
            qp.end()
        self.flag = False

    def paint(self):
        self.flag = True
        self.update()

    def draw_ellipse(self, qp):
        self.r = randint(1, 100)
        qp.drawEllipse(randint(100, 700), randint(100, 500), self.r, self.r)


if __name__ == '__main__':
    app = QApplication(argv)
    window = MyWidget()
    window.show()
    exit(app.exec())