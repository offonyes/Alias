from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from .AliasAbout import Ui_AliasAbout

#Create GUI and connect functions
class AliasAbout(QMainWindow, Ui_AliasAbout):
    def __init__(self, *args, **kwargs):
        super(AliasAbout, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.close) 
