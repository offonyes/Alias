from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from .a_rc import *
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, Form):
        Form.setWindowTitle("lias")
        Form.resize(887, 600)
        Form.setWindowIcon(QIcon('assets\\Alias_logo.png'))
        
        styleFile = QFile("assets\styles.qss")
        styleFile.open(QFile.ReadOnly | QFile.Text)
        styleSheet = str(styleFile.readAll(), encoding='utf-8')
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet("QWidget [objectName=\"centralwidget\"]{border-image:url(:/newPrefix/assets/Alias.png);}\n"
"\n"
"")
        self.widget = QStackedWidget()
        self.centralwidget = QWidget()
        self.setCentralWidget(self.widget)
        self.centralwidget.setObjectName("centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        font = QFont()
        font.setPointSize(23)
        self.gridLayout = QGridLayout()
        self.gridLayout_2 = QGridLayout()

        self.Exit_btn = QPushButton("Exit")
        self.Exit_btn.setSizePolicy(sizePolicy)        
        self.Exit_btn.setMinimumSize(QSize(256, 55))
        self.Exit_btn.setMaximumSize(QSize(377, 89))
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
        self.Settings_btn.setMinimumSize(QSize(256, 56))
        self.Settings_btn.setMaximumSize(QSize(377, 89))
        self.Settings_btn.setFont(font)
        self.gridLayout_2.addWidget(self.Settings_btn, 3, 3, 1, 1)

        self.Play_btn = QPushButton("Play")
        self.Play_btn.setSizePolicy(sizePolicy)
        self.Play_btn.setMinimumSize(QSize(256, 55))
        self.Play_btn.setMaximumSize(QSize(377, 89))
        self.Play_btn.setFont(font)

        self.gridLayout_2.addWidget(self.Play_btn, 2, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.centralwidget.setLayout(self.gridLayout)
        self.centralwidget.setStyleSheet(styleSheet)

        self.db_connection = sqlite3.connect('alias_game.db')
        cursor = self.db_connection.cursor()
        cursor.execute('SELECT DISTINCT Category FROM Words')
        self.categories = [category[0] for category in cursor.fetchall()]
        
        self.centralwidget_2 = QWidget()
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
        self.Discard_btn.setMinimumSize(QSize(250, 20))
        self.Discard_btn.setMaximumSize(QSize(365000, 45))
        self.horizontalLayout_7.addWidget(self.Discard_btn)

        self.Select_btn = QPushButton("Select All", self.horizontalWidget)
        sizePolicy.setHeightForWidth(self.Select_btn.sizePolicy().hasHeightForWidth())
        self.Select_btn.setSizePolicy(sizePolicy)
        self.Select_btn.setMinimumSize(QSize(250, 20))
        self.Select_btn.setMaximumSize(QSize(365000, 45))
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
        self.horizontalWidget_2.setMaximumSize(QSize(16777215, 60))

        self.horizontalLayout_8 = QHBoxLayout(self.horizontalWidget_2)

        self.MainM_btn = QPushButton("Main Menu", self.horizontalWidget_2)

        self.MainM_btn.setSizePolicy(sizePolicy)
        self.MainM_btn.setMinimumSize(QSize(250, 20))
        self.MainM_btn.setMaximumSize(QSize(365000, 45))
        self.horizontalLayout_8.addWidget(self.MainM_btn)

        self.StartG_btn = QPushButton("Start Game", self.horizontalWidget_2)
        sizePolicy.setHeightForWidth(self.StartG_btn.sizePolicy().hasHeightForWidth())
        self.StartG_btn.setSizePolicy(sizePolicy)
        self.StartG_btn.setMinimumSize(QSize(250, 20))
        self.StartG_btn.setMaximumSize(QSize(365000, 45))

        self.horizontalLayout_8.addWidget(self.StartG_btn)
        self.gridLayout_3.addWidget(self.horizontalWidget_2, count+3, 3, 1, 1)

        self.widget.addWidget(self.centralwidget)
        self.widget.addWidget(self.centralwidget_2)


