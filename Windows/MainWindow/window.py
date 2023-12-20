from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from .MainWindow import Ui_MainWindow
from ..SettingsWindow.Settings.window import MainSettings
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.Play_btn.clicked.connect(self.play_menu)
        self.Settings_btn.clicked.connect(self.settings_menu)
        self.Exit_btn.clicked.connect(self.close)

    def play_menu(self):
        print("play")

    def settings_menu(self):
        self.MSetwindow = MainSettings(self)
        self.MSetwindow.show()
        self.setEnabled(False)
        self.MSetwindow.setEnabled(True)

    def on_MSetwindow_closed(self):
        self.setEnabled(True)

    def closeEvent(self, event):
        # Обработка закрытия главного окна
        if hasattr(self, 'MSetwindow') and self.MSetwindow.isVisible():
            self.MSetwindow.close()


    def close(self):
        QApplication.quit()



def run_app():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_app()

