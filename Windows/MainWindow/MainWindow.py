from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from .a_rc import *
from .CSbg_rc import *
import sqlite3, json

class Ui_MainWindow(object):
    def setupUi(self, Form):
        Form.setWindowTitle("lias")
        Form.resize(890, 600)
        Form.setWindowIcon(QIcon('assets\\Alias_logo.png'))
        
        styleFile = QFile("assets\\styles.qss")
        styleFile.open(QFile.ReadOnly | QFile.Text)
        styleSheet = str(styleFile.readAll(), encoding='utf-8')
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet("QWidget [objectName=\"MM\"]{border-image:url(:/newPrefix/assets/Alias.png);}")
        Form.setStyleSheet("QWidget [objectName=\"CS\"]{border-image:url(:/newPrefix/AliasBG.png);}")
        self.widget = QStackedWidget()
        self.centralwidget = QWidget()
        self.setCentralWidget(self.widget)
        self.centralwidget.setObjectName("MM")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        font = QFont()
        font.setPointSize(23)
        self.gridLayout = QGridLayout()
        self.gridLayout_2 = QGridLayout()

        self.Exit_btn = QPushButton("Exit")
        self.Exit_btn.setSizePolicy(sizePolicy)        
        self.Exit_btn.setMinimumSize(QSize(255, 55))
        self.Exit_btn.setMaximumSize(QSize(380, 90))
        self.Exit_btn.setFont(font)


        self.gridLayout_2.addWidget(self.Exit_btn, 4, 3, 1, 1)
        spacerItem = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 5, 3, 1, 1)
        spacerItem1 = QSpacerItem(150, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 4, 1, 1)
        spacerItem2 = QSpacerItem(20, 350, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem2, 0, 3, 1, 1)
        spacerItem3 = QSpacerItem(150, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 3, 0, 1, 1)

        self.Settings_btn = QPushButton("Settings")
        self.Settings_btn.setSizePolicy(sizePolicy)
        self.Settings_btn.setMinimumSize(QSize(255, 55))
        self.Settings_btn.setMaximumSize(QSize(380, 90))
        self.Settings_btn.setFont(font)
        self.gridLayout_2.addWidget(self.Settings_btn, 3, 3, 1, 1)

        self.Play_btn = QPushButton("Play")
        self.Play_btn.setSizePolicy(sizePolicy)
        self.Play_btn.setMinimumSize(QSize(255, 55))
        self.Play_btn.setMaximumSize(QSize(380, 90))
        self.Play_btn.setFont(font)

        self.gridLayout_2.addWidget(self.Play_btn, 2, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.centralwidget.setLayout(self.gridLayout)
        self.centralwidget.setStyleSheet(styleSheet)

        self.db_connection = sqlite3.connect('alias_game.db')
        cursor = self.db_connection.cursor()
        cursor.execute('SELECT DISTINCT Category FROM Words')
        self.categories = [category[0] for category in cursor.fetchall()]
        
        #Page for category selector
        self.centralwidget_2 = QWidget()
        self.centralwidget_2.setObjectName("CS")
        self.centralwidget_2.setStyleSheet(styleSheet)

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        self.gridLayout_3 = QGridLayout(self.centralwidget_2)

        spacerItem4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 6, 5, 1, 1)
        spacerItem6 = QSpacerItem(10, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 6, 0, 1, 1)
        spacerItem7 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 2, 4, 1, 1)

        
        self.horizontalWidget = QWidget(self.centralwidget_2)
        self.horizontalWidget.setMaximumSize(QSize(16777215, 60))

        self.horizontalLayout_7 = QHBoxLayout(self.horizontalWidget)

        self.Discard_btn = QPushButton("Discard All", self.horizontalWidget)
        sizePolicy.setHeightForWidth(self.Discard_btn.sizePolicy().hasHeightForWidth())
        self.Discard_btn.setSizePolicy(sizePolicy)
        self.Discard_btn.setFont(font)
        self.Discard_btn.setMinimumSize(QSize(255, 45))
        self.Discard_btn.setMaximumSize(QSize(365000, 90))
        self.horizontalLayout_7.addWidget(self.Discard_btn)

        self.Select_btn = QPushButton("Select All", self.horizontalWidget)
        sizePolicy.setHeightForWidth(self.Select_btn.sizePolicy().hasHeightForWidth())
        self.Select_btn.setSizePolicy(sizePolicy)
        self.Select_btn.setFont(font)
        self.Select_btn.setMinimumSize(QSize(255, 45))
        self.Select_btn.setMaximumSize(QSize(365000, 90))
        self.horizontalLayout_7.addWidget(self.Select_btn)

        self.gridLayout_3.addWidget(self.horizontalWidget, 1, 3, 1, 1)
        spacerItem8 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 2, 1, 1, 1)
        spacerItem9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 0, 3, 1, 1)

        count = 5
        max_per_row = 7
        self.checkbox = []
        while self.categories:
            count +=1
            current_row_categories = self.categories[:max_per_row]
            self.categories = self.categories[max_per_row:]

            row_widget = QWidget(self.centralwidget_2)
            row_widget.setMaximumSize(QSize(60, 60))

            row_layout = QHBoxLayout(row_widget)
            row_layout.setSizeConstraint(QLayout.SetMinAndMaxSize)
            row_layout.setContentsMargins(25, -1, -1, -1)
            row_layout.setSpacing(0)

            # Calculate the number of empty spaces for centering
            num_empty_spaces = max_per_row - len(current_row_categories)
            left_spaces = num_empty_spaces // 2
            right_spaces = left_spaces

            # Add empty spaces for centering
            for _ in range(left_spaces):
                row_layout.addWidget(QWidget(row_widget))

            # Add checkboxes to the layout
            for category in current_row_categories:
                checkbox = QCheckBox(category, row_widget)
                checkbox.setFont(font)
                self.checkbox.append(checkbox)
                row_layout.addWidget(checkbox)

            # Add remaining empty spaces for centering
            for _ in range(right_spaces):
                row_layout.addWidget(QWidget())
            self.gridLayout_3.addWidget(row_widget, count,1,1,4)


        spacerItem10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem10, count + 2, 3, 1, 1)
        spacerItem11 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem11, count + 3, 0, 1, 1)

        self.horizontalWidget_2 = QWidget(self.centralwidget_2)
        self.horizontalWidget_2.setMaximumSize(QSize(16777215, 90))

        self.horizontalLayout_8 = QHBoxLayout(self.horizontalWidget_2)

        self.MainM_btn = QPushButton("Main Menu", self.horizontalWidget_2)
        self.MainM_btn.setSizePolicy(sizePolicy)
        self.MainM_btn.setFont(font)
        self.MainM_btn.setMinimumSize(QSize(255, 60))
        self.MainM_btn.setMaximumSize(QSize(365000, 90))
        self.horizontalLayout_8.addWidget(self.MainM_btn)

        self.StartG_btn = QPushButton("Start Game", self.horizontalWidget_2)
        sizePolicy.setHeightForWidth(self.StartG_btn.sizePolicy().hasHeightForWidth())
        self.StartG_btn.setSizePolicy(sizePolicy)
        self.StartG_btn.setFont(font)
        self.StartG_btn.setMinimumSize(QSize(255, 60))
        self.StartG_btn.setMaximumSize(QSize(365000, 90))

        self.horizontalLayout_8.addWidget(self.StartG_btn)

        self.gridLayout_3.addWidget(self.horizontalWidget_2, count+3, 3, 1, 1)

        self.centralwidget_3 = QWidget()
        self.centralwidget_3.setStyleSheet("QLabel {\n"
"    color: #FFFFFF; /* Белый цвет текста */\n"
"    background-color: #3498db; /* Фоновый цвет - синий (замените этот код на нужный) */\n"
"    border: 2px solid #2980b9; /* Цвет рамки (замените этот код на нужный) */\n"
"    border-radius: 8px; /* Закругление углов */\n"
"    padding: 10px; /* Отступы внутри виджета */\n"
"    font-size: 14px; /* Размер шрифта */\n"
"    font-weight: bold; /* Жирный текст */\n"
"}\n"
"")
        # Page for Game
        self.gridLayout_4 = QGridLayout(self.centralwidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)

        self.gridLayout_5 = QGridLayout()
        self.TeamName = []
        with open("Windows\\settings.json", "r") as file:
            settings = json.load(file)
            self.TeamNum = settings.get("slider_position", 0)
            self.time_valueRaw = settings.get("time_value", "00:00:000")
            self.time_value = QTime.fromString(self.time_valueRaw, "mm:ss:zzz")
           
        self.TeamPoints = [0 for _ in range(self.TeamNum)]
        self.TeamWords = []

        for i in range(self.TeamNum):
            TeamName = QLabel(self.centralwidget_3)
            sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
            sizePolicy.setHeightForWidth(TeamName.sizePolicy().hasHeightForWidth())
            TeamName.setSizePolicy(sizePolicy)
            TeamName.setMinimumSize(QSize(172, 41))
            TeamName.setMaximumSize(QSize(16777215, 60))
            TeamName.setAlignment(Qt.AlignCenter)
            self.TeamName.append(TeamName)
            self.gridLayout_5.addWidget(TeamName, 1, i, 1, 1)

            TeamWord = QListWidget(self.centralwidget_3)
            sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            sizePolicy.setHeightForWidth(TeamWord.sizePolicy().hasHeightForWidth())
            TeamWord.setSizePolicy(sizePolicy)
            TeamWord.setMinimumSize(QSize(0, 100))
            TeamWord.setMaximumSize(QSize(16777215, 250))
            self.TeamWords.append(TeamWord)
            self.gridLayout_5.addWidget(TeamWord, 2, i, 1, 1)

        self.gridLayout_4.addLayout(self.gridLayout_5, 11, 0, 1, 5)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(0)

        self.ShowingWord = QLabel("Word", self.centralwidget_3)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHeightForWidth(self.ShowingWord.sizePolicy().hasHeightForWidth())
        self.ShowingWord.setSizePolicy(sizePolicy)
        self.ShowingWord.setMinimumSize(QSize(350, 0))
        self.ShowingWord.setMaximumSize(QSize(390, 80))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ShowingWord.setFont(font)
        self.ShowingWord.setAlignment(Qt.AlignCenter)
        self.ShowingWord.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.gridLayout_5.addWidget(self.ShowingWord, 2, 0, 1, 2)

        self.Hint_btn = QPushButton("Hint", self.centralwidget_3)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHeightForWidth(self.Hint_btn.sizePolicy().hasHeightForWidth())
        self.Hint_btn.setSizePolicy(sizePolicy)
        self.Hint_btn.setMinimumSize(QSize(175, 0))
        self.Hint_btn.setMaximumSize(QSize(195, 50))
        self.gridLayout_5.addWidget(self.Hint_btn, 3, 1, 1, 1)

        self.NotCounted_btn = QPushButton("Not Counted",self.centralwidget_3)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHeightForWidth(self.NotCounted_btn.sizePolicy().hasHeightForWidth())
        self.NotCounted_btn.setSizePolicy(sizePolicy)
        self.NotCounted_btn.setMinimumSize(QSize(175, 0))
        self.NotCounted_btn.setMaximumSize(QSize(195, 50))
        self.gridLayout_5.addWidget(self.NotCounted_btn, 3, 0, 1, 1)

        self.Counted_btn = QPushButton("Counted",self.centralwidget_3)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHeightForWidth(self.Counted_btn.sizePolicy().hasHeightForWidth())
        self.Counted_btn.setSizePolicy(sizePolicy)
        self.Counted_btn.setMinimumSize(QSize(350, 0))
        self.Counted_btn.setMaximumSize(QSize(390, 50))
        self.gridLayout_5.addWidget(self.Counted_btn, 1, 0, 1, 2)

        self.StartGame_btn = QPushButton("Start", self.centralwidget_3)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHeightForWidth(self.StartGame_btn.sizePolicy().hasHeightForWidth())
        self.StartGame_btn.setMinimumSize(QSize(350, 50))
        self.StartGame_btn.setMaximumSize(QSize(39990, 100))
        self.gridLayout_4.addWidget(self.StartGame_btn, 5, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_5, 5, 2, 1, 1)

        self.BackToMM_btn = QPushButton("Main menu", self.centralwidget_3)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy.setHeightForWidth(self.BackToMM_btn.sizePolicy().hasHeightForWidth())
        self.BackToMM_btn.setSizePolicy(sizePolicy)
        self.BackToMM_btn.setMinimumSize(QSize(145, 30))
        self.BackToMM_btn.setMaximumSize(QSize(255, 45))
        self.BackToMM_btn.setObjectName("BackToMM_btn")
        self.gridLayout_4.addWidget(self.BackToMM_btn, 1, 0, 1, 2)

        spacerItem12 = QSpacerItem(155, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem12, 5, 0, 1, 1)
        spacerItem13 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem13, 9, 2, 1, 1)
        spacerItem14 = QSpacerItem(20, 75, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout_4.addItem(spacerItem14, 4, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)

        spacerItem15 = QSpacerItem(237, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem15)

        self.timer_widget = QLCDNumber(self.centralwidget_3)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHeightForWidth(self.timer_widget.sizePolicy().hasHeightForWidth())
        self.timer_widget.setMinimumSize(QSize(170, 128))
        self.timer_widget.setMaximumSize(QSize(99999, 128))
        font = QFont()
        font.setKerning(True)
        self.timer_widget.setFont(font)
        self.timer_widget.setFrameShape(QFrame.NoFrame)
        self.timer_widget.setDigitCount(9)
        self.horizontalLayout_2.addWidget(self.timer_widget)

        self.timer = QTimer()
        self.timer.timeout.connect(self.Timer_func)
        self.blinkTimer = QTimer()
        self.blinkTimer.timeout.connect(self.blinkTimerFunction)

        spacerItem16 = QSpacerItem(237, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem16)

        self.gridLayout_4.addLayout(self.horizontalLayout_2, 2, 0, 1, 5)

        spacerItem17 = QSpacerItem(105, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem17, 5, 3, 1, 1)
        spacerItem18 = QSpacerItem(155, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem18, 5, 4, 1, 1)
        spacerItem19 = QSpacerItem(105, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem19, 5, 1, 1, 1)

        self.textBrowser = QTextBrowser(self.centralwidget_3)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QSize(350, 50))
        self.textBrowser.setMaximumSize(QSize(16777215, 100))
        self.textBrowser.append("HELLO GREGORI")
        self.gridLayout_4.addWidget(self.textBrowser, 6, 1, 1, 3)

        self.widget.addWidget(self.centralwidget)
        self.widget.addWidget(self.centralwidget_2)
        self.widget.addWidget(self.centralwidget_3)