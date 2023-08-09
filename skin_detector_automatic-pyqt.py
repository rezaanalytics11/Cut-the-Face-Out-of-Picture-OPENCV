from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider
import numpy as np
import cv2
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel, QFormLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import numpy as np
from PyQt5.QtWidgets import (QApplication, QWidget,
  QPushButton, QVBoxLayout, QHBoxLayout,QGridLayout)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):


        self.label1 = QLabel('', self)
        self.label2 = QLabel('', self)
        self.label3 = QLabel('', self)
        self.label4 = QLabel('', self)
        self.label5 = QLabel('', self)
        self.label6 = QLabel('', self)

        mySlider1 = QSlider(Qt.Vertical, self)
        mySlider1.setRange(0, 255)
        mySlider1.valueChanged.connect(self.changeValue1)
        mySlider1.setValue(100)

        mySlider2 = QSlider(Qt.Vertical, self)
        mySlider2.setRange(0, 255)
        mySlider2.valueChanged.connect(self.changeValue2)
        mySlider2.setValue(100)

        mySlider3 = QSlider(Qt.Vertical, self)
        mySlider3.setRange(0, 255)
        mySlider3.valueChanged.connect(self.changeValue3)
        mySlider3.setValue(100)

        mySlider4 = QSlider(Qt.Vertical, self)
        mySlider4.setRange(0, 255)
        mySlider4.valueChanged.connect(self.changeValue4)
        mySlider4.setValue(100)

        mySlider5 = QSlider(Qt.Vertical, self)
        mySlider5.setRange(0, 255)
        mySlider5.valueChanged.connect(self.changeValue5)
        mySlider5.setValue(100)

        mySlider6 = QSlider(Qt.Vertical, self)
        mySlider6.setRange(0, 255)
        mySlider6.valueChanged.connect(self.changeValue6)
        mySlider6.setValue(100)





        Button = QPushButton('Proceed')
        #cancelButton = QPushButton('Cancel')
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(Button)
        # hbox.addWidget(cancelButton)
        Button.clicked.connect(self.draw)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.label1)
        hbox2.addWidget(self.label2)
        hbox2.addWidget(self.label3)
        hbox2.addWidget(self.label4)
        hbox2.addWidget(self.label5)
        hbox2.addWidget(self.label6)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(mySlider1)
        hbox3.addWidget(mySlider2)
        hbox3.addWidget(mySlider3)
        hbox3.addWidget(mySlider4)
        hbox3.addWidget(mySlider5)
        hbox3.addWidget(mySlider6)


        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        vbox.setAlignment(Qt.AlignCenter)
        self.setGeometry(400, 400, 300, 250)
        self.setWindowTitle('Box layout example, QHBoxLayout, QVBoxLayout')
        self.show()


    def changeValue1(self,value):
        print(value)
        self.value1=value
        self.label1.setText(f'R: {value}')
        #pass

    def changeValue2(self, value):
        print(value)
        self.value2 = value
        self.label2.setText(f'R: {value}')



    def changeValue3(self,value):
        print(value)
        #self.value3 = value
        self.value3 = value
        self.label3.setText(f'R: {value}')


    def changeValue4(self,value):
        print(value)
        #self.value4 = value
        self.value4 = value
        self.label4.setText(f'R: {value}')


    def changeValue5(self,value):
        print(value)
        #self.value5 = value
        self.value5 = value
        self.label5.setText(f'R: {value}')



    def changeValue6(self,value):
        print(value)
        #self.value6 = value
        self.value6 = value
        self.label6.setText(f'R: {value}')



    def draw(self):

        img = cv2.imread(r'C:\Users\Ariya Rayaneh\Desktop\human4.jpg')
        img = cv2.resize(img, (0, 0), fx=4, fy=4)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


        lower = np.array([self.value1, self.value2, self.value3])
        upper = np.array([self.value4, self.value5, self.value6])
        print(upper)

        mask = cv2.inRange(hsv, lower, upper)

        res = cv2.bitwise_or(img, img, mask=mask)

        # cv2.imshow('frame',img)
        # cv2.imshow('mask',mask)
        cv2.imshow('res', res)
        cv2.imwrite(r'C:\Users\Ariya Rayaneh\Desktop\human_face_only.jpg', res)
        cv2.waitKey()


if __name__ == '__main__':
 app = QApplication(sys.argv)
 ex = Example()
 sys.exit(app.exec_())