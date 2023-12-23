from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Ui_TeamConfig(object):
    def setupUi(self, Form):
        Form.setWindowTitle("Team Config")
        Form.setFixedSize(380,220)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.gridLayout = QGridLayout()
        font = QFont()
        font.setBold(True)
        font.setWeight(75)

        # Add column headers
        self.First_Header = QLabel("№")
        self.First_Header.setFont(font)
        self.First_Header.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.First_Header, 0, 0, 1, 1)

        self.Second_Header = QLabel("Name")
        self.Second_Header.setFont(font)
        self.Second_Header.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.Second_Header, 0, 1, 1, 1)

        self.Third_Header = QLabel("Color")
        self.Third_Header.setFont(font)
        self.Third_Header.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.Third_Header, 0, 2, 1, 1)

        self.FirstTeamle = QLineEdit()
        self.SecondTeamle = QLineEdit()
        self.ThirdTeamle = QLineEdit()
        self.FourthTeamle = QLineEdit()
        self.FifthTeamle = QLineEdit()

        self.ColorFirstbtn = QPushButton("Select Color")
        self.ColorSecondbtn = QPushButton("Select Color")
        self.ColorThirdbtn = QPushButton("Select Color")
        self.ColorFourthbtn = QPushButton("Select Color")
        self.ColorFifthbtn = QPushButton("Select Color")


        # Create a list of labels, line edits, and color buttons
        self.lineEdits = [self.FirstTeamle, self.SecondTeamle, self.ThirdTeamle, self.FourthTeamle, self.FifthTeamle]
        self.colorButtons = [self.ColorFirstbtn, self.ColorSecondbtn, self.ColorThirdbtn, self.ColorFourthbtn, self.ColorFifthbtn]

        for i in range(0,5):
            label = QLabel(f"Team {i+1}")
            label.setFont(font)
            label.setAlignment(Qt.AlignCenter)
            self.gridLayout.addWidget(label, i+1, 0, 1, 1)

            self.lineEdits[i].setFont(font)
            self.gridLayout.addWidget(self.lineEdits[i], i+1, 1, 1, 1)

            self.colorButtons[i].setFont(font)
            self.gridLayout.addWidget(self.colorButtons[i], i+1, 2, 1, 1)
            self.colorButtons[i].clicked.connect(lambda _, button=self.colorButtons[i]: self.selectColor(button))

        self.Save_btn = QPushButton("Save")
        self.Save_btn.setFixedWidth(90)
        self.Save_btn.setLayoutDirection(Qt.RightToLeft)
        self.gridLayout.addWidget(self.Save_btn, 6, 1, 1, 1)

        self.Cancel_btn = QPushButton("Cancel")
        self.Cancel_btn .setFixedWidth(90)
        self.gridLayout.addWidget(self.Cancel_btn, 6, 2, 1, 1)
        self.central_widget.setLayout(self.gridLayout)
