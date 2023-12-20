from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Ui_MainSettings(object):
    def setupUi(self, Form):
        Form.setWindowTitle("Settings")
        Form.setFixedSize(480, 190)
        font = QFont()
        font.setPointSize(10)
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        self.gridLayout = QGridLayout()

        self.NamTeams_lbl = QLabel("Name of teams")
        self.NamTeams_lbl.setFont(font)
        self.gridLayout.addWidget(self.NamTeams_lbl, 3, 0, 1, 1)

        self.TimSet_lbl = QLabel("Timer settings:")
        self.TimSet_lbl.setFont(font)
        self.gridLayout.addWidget(self.TimSet_lbl, 1, 0, 1, 1)

        self.NumTeams_lbl = QLabel("Number of teams:")
        self.NumTeams_lbl.setFont(font)
        self.gridLayout.addWidget(self.NumTeams_lbl, 2, 0, 1, 1)

        self.ListWord_lbl = QLabel("List of words")
        self.ListWord_lbl.setFont(font)
        self.gridLayout.addWidget(self.ListWord_lbl, 4, 0, 1, 1)

        self.Cacnel_btn = QPushButton("About")
        self.Cacnel_btn.setMaximumSize(QSize(80, 25))
        self.Cacnel_btn.setFont(font)
        self.gridLayout.addWidget(self.Cacnel_btn, 5, 3, 1, 1)

        self.NT_btn = QPushButton("Open")
        self.NT_btn.setFont(font)
        self.gridLayout.addWidget(self.NT_btn, 3, 1, 1, 3)

        self.LW_btn = QPushButton("Open")
        self.LW_btn.setFont(font)
        self.gridLayout.addWidget(self.LW_btn, 4, 1, 1, 3)

        self.ok_btn = QPushButton("Ok")
        self.ok_btn.setMaximumSize(QSize(80, 25))
        self.ok_btn.setFont(font)
        self.gridLayout.addWidget(self.ok_btn, 5, 2, 1, 1)

        self.timeEdit = QTimeEdit(Form)
        self.timeEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.timeEdit.setMaximumTime(QTime(0, 59, 59))
        self.timeEdit.setDisplayFormat("mm:ss")
        self.timeEdit.setCurrentSection(QDateTimeEdit.SecondSection)
        self.timeEdit.setCurrentSectionIndex(1)
        self.timeEdit.setTime(QTime(0, 1, 0))
        self.gridLayout.addWidget(self.timeEdit, 1, 1, 1, 3)

        self.horizontalSlider = QSlider(Qt.Horizontal, Form)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(5)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setSliderPosition(2)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider.setToolTip("Minimum 1 team. Maximum 5 team.")
        self.horizontalSlider.setTickInterval(1)
        self.gridLayout.addWidget(self.horizontalSlider, 2, 1, 1, 3)

        self.centralwidget.setLayout(self.gridLayout)


# if __name__ == "__main__":
#     import sys
#     app = QApplication(sys.argv)
#     Form = QWidget()
#     ui = Ui_MainSettings()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
