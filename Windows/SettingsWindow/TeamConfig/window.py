from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import json
from .TeamConfig import Ui_TeamConfig

class TeamConfig(QMainWindow, Ui_TeamConfig):
    def __init__(self, *args, **kwargs):
        super(TeamConfig, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.load_settings()
        self.Save_btn.clicked.connect(self.save_settings)
        self.Cancel_btn.clicked.connect(self.close)

#Opens Color SELECTOR
    def selectColor(self, button):
        self.color = QColorDialog.getColor()
        if self.color.isValid():
            button.setStyleSheet(f"background-color: {self.color.name()}")

#Load settings
    def load_settings(self):
        with open("Windows\\settings.json", "r") as file:
            settings = json.load(file)
            self.FirstTeamle.setText(settings.get("Team_Names", [{}])[0].get("First_Team_Name"))
            self.SecondTeamle.setText(settings.get("Team_Names", [{}])[0].get("Second_Team_Name"))
            self.ThirdTeamle.setText(settings.get("Team_Names", [{}])[0].get("Third_Team_Name"))
            self.FourthTeamle.setText(settings.get("Team_Names", [{}])[0].get("Fourth_Team_Name"))
            self.FifthTeamle.setText(settings.get("Team_Names", [{}])[0].get("Fifth_Team_Name"))
            self.ColorFirstbtn.setStyleSheet(f"{settings.get("Teams_colors", [{}])[0].get("First_Team_Color")}")
            self.ColorSecondbtn.setStyleSheet(f"{settings.get("Teams_colors", [{}])[0].get("Second_Team_Color")}")
            self.ColorThirdbtn.setStyleSheet(f"{settings.get("Teams_colors", [{}])[0].get("Third_Team_Color")}")
            self.ColorFourthbtn.setStyleSheet(f"{settings.get("Teams_colors", [{}])[0].get("Fourth_Team_Color")}")
            self.ColorFifthbtn.setStyleSheet(f"{settings.get("Teams_colors", [{}])[0].get("Fifth_Team_Color")}")

#Save settings
    def save_settings(self):
        with open("Windows\\settings.json", "r") as file:
            existing_settings = json.load(file)
        new_settings = {
            "Team_Names":[
                {
                    "First_Team_Name": self.FirstTeamle.text(),
                    "Second_Team_Name": self.SecondTeamle.text(),
                    "Third_Team_Name": self.ThirdTeamle.text(),
                    "Fourth_Team_Name": self.FourthTeamle.text(),
                    "Fifth_Team_Name": self.FifthTeamle.text()
                    }],
            "Teams_colors":[
                {
                    "First_Team_Color": self.ColorFirstbtn.styleSheet(),
                    "Second_Team_Color": self.ColorSecondbtn.styleSheet(),
                    "Third_Team_Color": self.ColorThirdbtn.styleSheet(),
                    "Fourth_Team_Color": self.ColorFourthbtn.styleSheet(),
                    "Fifth_Team_Color": self.ColorFifthbtn.styleSheet()
                    }]
        }
        existing_settings.update(new_settings)
        with open("Windows\\settings.json", "w") as file:
            json.dump(existing_settings, file, indent=4)

#Checks if this GUI is closed and of closed than closes his subwindow
    def closeEvent(self, event):
        self.parent().setEnabled(True)
        event.accept()
