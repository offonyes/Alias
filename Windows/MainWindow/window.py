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
        self.Counted_btn.clicked.connect(lambda: self.CountPoint(True))
        self.NotCounted_btn.clicked.connect(lambda: self.CountPoint(False))
        self.Hide()

    def ShowHintOfWord(self):
        self.textBrowser.show()
        self.timer.stop()
    
    def ChooseWord(self, dct):
        try:
            self.randomWord = random.choice(list(dct.keys()))
            self.ShowingWord.setText(self.randomWord)
            self.textBrowser.setText(self.WordExpl[self.randomWord])
            self.WordExpl.pop(self.randomWord)
        except Exception as e:
            error_message = ("The words have run out.\nReturn to the main page and add words to the database!")
            self.show_error_message(error_message)

    def CountPoint(self, point):
        self.timer.start()
        self.textBrowser.hide()
        print(self.TeamPoints)
        randomWordItem = QListWidgetItem(self.randomWord)  # Create QListWidgetItem
        if point:
            self.TeamPoints[self.Team] += point
            self.TeamName[self.Team].setText(f"{self.TeamNameFF[self.Team]} | Points: {self.TeamPoints[self.Team]}")
            randomWordItem.setForeground(QColor("green"))  # Set the foreground color
        else:
            randomWordItem.setForeground(QColor("red"))  # Set the foreground color

        self.TeamWords[self.Team].addItem(randomWordItem)  # Add the item to QListWidget
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
        self.SellCateg = [checkbox.text() for checkbox in self.checkbox if checkbox.checkState() == 2]
        if not self.SellCateg:
            error_message = ("You forgot to choose category!\nChoose One")
            self.show_error_message(error_message)
        else:
            for team_word_list in self.TeamWords:
                team_word_list.clear()
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

    def show_error_message(self, message):
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Warning)
        error_box.setWindowIcon(QIcon('assets\\Alias_logo.png'))
        error_box.setWindowTitle("Error")
        error_box.setText(message)
        error_box.setStandardButtons(QMessageBox.Ok)
        error_box.exec_()