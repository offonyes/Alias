from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Ui_AliasAbout(object):
    def setupUi(self, Form):
        Form.setWindowTitle("About")
        Form.setFixedSize(380, 150)

        self.pushButton = QPushButton("Ok",Form)
        self.pushButton.setGeometry(QRect(290, 117, 82, 25))

        self.label = QLabel(Form)
        self.label.setGeometry(QRect(190, 27, 91, 16))
        self.label.setText("Alias ver. alpha1")

        self.label_2 = QLabel(Form)
        self.label_2.setGeometry(QRect(130, 62, 231, 16))
        self.label_2.setText("By Dimitri Katranidis and Grigori Gunumjiani")

        self.label_3 = QLabel(Form)
        self.label_3.setGeometry(QRect(180, 82, 131, 16))
        self.label_3.setText(" for Zura Vashalomidze")


        self.logo_lable = QLabel(Form)
        self.logo_lable.setGeometry(QRect(10, 30, 81, 71))
        self.logo_lable.setPixmap(QPixmap("assets\\Alias_logo.png"))
        self.logo_lable.setScaledContents(True)
