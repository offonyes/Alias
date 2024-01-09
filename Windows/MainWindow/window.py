from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import json, random
from .MainWindow import Ui_MainWindow
from ..SettingsWindow.window import MainSettings

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.Team = 0
        self.setupUi(self)
        self.textBrowser.hide()
        self.widget.setCurrentIndex(0)
        self.Play_btn.clicked.connect(self.Category_menu)
        self.Settings_btn.clicked.connect(self.settings_menu)
        self.Exit_btn.clicked.connect(self.close)
        self.Select_btn.clicked.connect(lambda: self.chageState(2)) 
        self.Discard_btn.clicked.connect(lambda: self.chageState(False))
        self.MainM_btn.clicked.connect(self.Main_menu)
        self.StartG_btn.clicked.connect(self.Start_menu)
        self.Hint_btn.clicked.connect(self.ShowHintOfWord)
        self.StartGame_btn.clicked.connect(self.StartGame)
        self.BackToMM_btn.clicked.connect(self.Main_menu)
        self.Counted_btn.clicked.connect(lambda: self.CountPoint(1))
        self.NotCounted_btn.clicked.connect(lambda: self.CountPoint(0))
        self.Hide()

    def ShowHintOfWord(self):
        self.textBrowser.show()
        self.timer.stop()
    
    def ChooseWord(self, dct):
        randomWord = random.choice(list(dct.keys()))
        self.ShowingWord.setText(randomWord)
        self.textBrowser.setText(self.WordExpl[randomWord])
        self.WordExpl.pop(randomWord)

    def CountPoint(self, point):
        self.timer.start()
        self.textBrowser.hide()
        self.TeamPoints[self.Team] = self.TeamPoints[self.Team] + point
        print(self.TeamPoints)
        self.TeamName[self.Team].setText(f"{self.TeamNameFF[self.Team]} | Points: {self.TeamPoints[self.Team]}")
        self.ChooseWord(self.WordExpl)

    def Hide(self):
        self.Counted_btn.hide()
        self.NotCounted_btn.hide()
        self.Hint_btn.hide()
        self.ShowingWord.hide()
        self.StartGame_btn.show()
        self.timer_widget.display(self.time_valueRaw)       
        self.timer.stop()

    def StartGame(self):
        self.ChooseWord(self.WordExpl)
        self.StartGame_btn.hide()
        self.Counted_btn.show()
        self.NotCounted_btn.show()
        self.ShowingWord.show()
        self.Hint_btn.show()
        self.timer.start(1)
        for i in range(self.TeamNum):
            if i == self.Team:
                self.TeamWords[i].setStyleSheet("background-color: #ff90e6fc;")
            else:
                self.TeamWords[i].setStyleSheet("")
        

    def Start_menu(self):
        self.TeamNameFF = []
        self.WordExpl = {}
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)
        with open("Windows\\settings.json", "r") as file:
            settings = json.load(file)
            self.TeamNameFF.append(settings.get("Team_Names", [{}])[0].get("First_Team_Name"))
            self.TeamNameFF.append(settings.get("Team_Names", [{}])[0].get("Second_Team_Name"))
            self.TeamNameFF.append(settings.get("Team_Names", [{}])[0].get("Third_Team_Name"))
            self.TeamNameFF.append(settings.get("Team_Names", [{}])[0].get("Fourth_Team_Name"))
            self.TeamNameFF.append(settings.get("Team_Names", [{}])[0].get("Fifth_Team_Name"))
        for i in range(self.TeamNum):
            self.TeamName[i].setText(f"{self.TeamNameFF[i]} | Points: 0")
            
        self.SellCateg = [checkbox.text() for checkbox in self.checkbox if checkbox.checkState() == 2]

        cursor = self.db_connection.cursor()
        for n in self.SellCateg:
        # Find words for category
            cursor.execute("SELECT Word, ExplanationOfWord FROM Words WHERE Category=?", (n,))
            words_data = cursor.fetchall()
            for word, explanation in words_data:
                self.WordExpl[word] = explanation
        
        
    def Main_menu(self):
        self.widget.setCurrentIndex(0)

    def chageState(self, status):
        for checkbox in self.checkbox:
            checkbox.setCheckState(status)

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

    def Timer_func(self):
        if not self.time_value.isNull():
            self.time_value = self.time_value.addMSecs(-1)
            self.timer_widget.display(self.time_value.toString("mm:ss:zzz"))
        if self.time_value.toString("mm:ss:zzz") == "00:00:000":
            self.Team +=1     
            self.Hide()
            self.blinkTimer.stop()
            self.timer_widget.setStyleSheet("")
            self.time_value = QTime.fromString(self.time_valueRaw, "mm:ss:zzz")    
        if self.widget.currentIndex() != 2:
            self.Hide()
            self.TeamWords[self.Team].setStyleSheet("")
            self.blinkTimer.stop()
            self.timer_widget.setStyleSheet("")
            self.time_value = QTime.fromString(self.time_valueRaw, "mm:ss:zzz")    
            self.TeamPoints = [0 for _ in range(self.TeamNum)]
        if self.time_value.toString("mm:ss:zzz") <= "00:10:000" and not self.blinkTimer.isActive():
            self.blinkTimer.start(500)  # Мигание каждые 500 мс

            
    def blinkTimerFunction(self):
    # Мигание таймера путем изменения стиля
        current_style = self.timer_widget.styleSheet()
        if "background-color: red;" in current_style:
            self.timer_widget.setStyleSheet("background-color: none;")
        else:
            self.timer_widget.setStyleSheet("background-color: red;")

