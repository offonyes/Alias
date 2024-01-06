from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from .MainWindow import Ui_MainWindow
from ..SettingsWindow.window import MainSettings

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.widget.setCurrentIndex(0)
        self.Play_btn.clicked.connect(self.Category_menu)
        self.Settings_btn.clicked.connect(self.settings_menu)
        self.Exit_btn.clicked.connect(self.close)
        self.Select_btn.clicked.connect(self.sellectall) 
        self.Discard_btn.clicked.connect(self.discardall)
        self.MainM_btn.clicked.connect(self.Main_menu)
        self.StartG_btn.clicked.connect(self.Start_menu)
        self.Hint_btn.clicked.connect(self.ShowHintOfWord)
        self.StartGame_btn.clicked.connect(self.StartGame)
        self.BackToMM_btn.clicked.connect(self.Main_menu)

    def ShowHintOfWord(self):
        self.textBrowser.show()

    def StartGame(self):
        self.StartGame_btn.hide()
        self.Counted_btn.show()
        self.NotCounted_btn.show()
        self.ShowingWord.show()
        self.Hint_btn.show()

    def Start_menu(self):
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)

    def Main_menu(self):
        self.widget.setCurrentIndex(0)

    def sellectall(self):
        for checkbox in self.checkbox:
            checkbox.setCheckState(2)
    
    def discardall(self):
        for checkbox in self.checkbox:
            checkbox.setCheckState(False)

    def Category_menu(self):
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)
#Open Settings GUI
    def settings_menu(self):
        self.MSetwindow = MainSettings(self)
        self.MSetwindow.show()
        self.setEnabled(False)
        self.MSetwindow.setEnabled(True)

#Checks if this GUI is closed and of closed than closes his subwindow
    def closeEvent(self, event):
        if hasattr(self, 'MSetwindow') and self.MSetwindow.isVisible():
            self.MSetwindow.close()


