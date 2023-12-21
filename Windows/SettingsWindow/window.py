from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from .MainSettings import Ui_MainSettings
from .ShowWords.window import ShowWords
from .About.window import AliasAbout
class MainSettings(QMainWindow, Ui_MainSettings):
    def __init__(self, *args, **kwargs):
        super(MainSettings, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.LW_btn.clicked.connect(self.open_list_words)
        self.ok_btn.clicked.connect(self.close)
        self.NT_btn.clicked.connect(self.onChangeBackgroundClicked)
        self.about_btn.clicked.connect(self.open_about)

    def onChangeBackgroundClicked(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (.png.jpg *.bmp)")
        if fileName:
            self.setStyleSheet(f"QWidget {{ background-image: url('{fileName}'); }}")
    

    def open_list_words(self):
        self.SWwindow = ShowWords(self)
        self.SWwindow.show()
        self.setEnabled(False)
        self.SWwindow.setEnabled(True)

    def open_about(self):
        self.Aboutwindow = AliasAbout(self)
        self.Aboutwindow.show()

    def closeEvent(self, event):
        if hasattr(self, 'SWwindow') and self.SWwindow.isVisible():
            self.SWwindow.close()
        if hasattr(self, 'Aboutwindow') and self.Aboutwindow.isVisible():
            self.Aboutwindow.close()
        
        self.parent().setEnabled(True)
        event.accept()

    
        

