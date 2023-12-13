from sys import argv, exit
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UI(object):
    def setupUi(self, UI):
        UI.setObjectName("UI")
        UI.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(UI)
        self.centralwidget.setObjectName("centralwidget")
        self.draw_button = QtWidgets.QPushButton(self.centralwidget)
        self.draw_button.setGeometry(QtCore.QRect(650, 510, 141, 41))
        self.draw_button.setObjectName("draw_button")
        UI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        UI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UI)
        self.statusbar.setObjectName("statusbar")
        UI.setStatusBar(self.statusbar)

        self.retranslateUi(UI)
        QtCore.QMetaObject.connectSlotsByName(UI)

    def retranslateUi(self, UI):
        _translate = QtCore.QCoreApplication.translate
        UI.setWindowTitle(_translate("UI", "Git и желтые окружности"))
        self.draw_button.setText(_translate("UI", "Нарисовать окружность"))


class MyWidget(QMainWindow, Ui_UI):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setupUi(self)
        self.r = 0
        self.flag = False
        self.draw_button.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            qp.setBrush(color)
            qp.setPen(color)
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