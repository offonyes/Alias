from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from .MainSettings import Ui_MainSettings
from ..ShowWords.window import ShowWords

class MainSettings(QDialog, Ui_MainSettings):
    def __init__(self, *args, **kwargs):
        super(MainSettings, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # self.setEnabled(True)
        self.LW_btn.clicked.connect(self.open_list_words)
        self.ok_btn.clicked.connect(self.close)
    

    def open_list_words(self):
        SWwindow = ShowWords(self)
        SWwindow.show()

    
    def closeEvent(self, event):
        # При закрытии подокна, генерируется событие closeEvent
        self.accept()  # Эмитируем сигнал finished
        

