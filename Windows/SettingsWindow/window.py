from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import json
from .MainSettings import Ui_MainSettings
from .ShowWords.window import ShowWords
from .About.window import AliasAbout
from .TeamConfig.window import TeamConfig

#Create GUI and connect functions
class MainSettings(QMainWindow, Ui_MainSettings):
    def __init__(self, *args, **kwargs):
        super(MainSettings, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.LW_btn.clicked.connect(self.open_list_words)
        self.NT_btn.clicked.connect(self.open_team_names)
        self.about_btn.clicked.connect(self.open_about)
        # Load previously saved settings
        self.load_settings()
        self.save_btn.clicked.connect(self.save_settings)

    def save_settings(self):
        with open("Windows\\settings.json", "r") as file:
            existing_settings = json.load(file)

        slider_position = self.horizontalSlider.value()
        time_value = self.timeEdit.time().toString("mm:ss:zzz")
        new_settings = {
            "slider_position": slider_position,
            "time_value": time_value
        }
        existing_settings.update(new_settings)
        with open("Windows\\settings.json", "w") as file:
            json.dump(existing_settings, file, indent=4)
        self.close()

    def load_settings(self):
        with open("Windows\\settings.json", "r") as file:
            settings = json.load(file)
            slider_position = settings.get("slider_position", 0)
            time_value = settings.get("time_value", "00:00:000")

            self.horizontalSlider.setValue(slider_position)
            self.timeEdit.setTime(QTime.fromString(time_value, "mm:ss:zzz"))

#?Maybe add in future
    def onChangeBackgroundClicked(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (.png.jpg *.bmp)")
        if fileName:
            self.setStyleSheet(f"QWidget {{ background-image: url('{fileName}'); }}")

#Open Team settings GUI
    def open_team_names(self):
        self.TSwindow = TeamConfig(self)
        self.TSwindow.show()
        self.setEnabled(False)
        self.TSwindow.setEnabled(True)
    
#Open GUI that shows dictionary
    def open_list_words(self):
        self.SWwindow = ShowWords(self)
        self.SWwindow.show()
        self.setEnabled(False)
        self.SWwindow.setEnabled(True)
        
#Open GUI that shows about 
    def open_about(self):
        self.Aboutwindow = AliasAbout(self)
        self.Aboutwindow.show()

#Checks if this GUI is closed and of closed than closes his subwindow
    def closeEvent(self, event):
        if hasattr(self, 'SWwindow') and self.SWwindow.isVisible():
            self.SWwindow.close()
        if hasattr(self, 'Aboutwindow') and self.Aboutwindow.isVisible():
            self.Aboutwindow.close()
        if hasattr(self, 'TSwindow') and self.TSwindow.isVisible():
            self.TSwindow.close()
        self.parent().setEnabled(True)
        event.accept()

    
        

