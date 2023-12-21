from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from .a_rc import *
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
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
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
