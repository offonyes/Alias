from PyQt5.QtWidgets import QVBoxLayout, QWidget, QPushButton, QComboBox, QLabel, QListWidget, QMenu, QAction
from PyQt5.QtCore import Qt

class Ui_ShowWords(object):
    def setupUi(self, Form):

        Form.setWindowTitle("Category selection")
        Form.setGeometry(100, 100, 300, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label = QLabel("Select a category:")
        self.layout.addWidget(self.label)

        self.category_combobox = QComboBox()
        self.layout.addWidget(self.category_combobox)

        self.select_btn = QPushButton("Load")
        self.layout.addWidget(self.select_btn)

        self.words_list = QListWidget()
        self.layout.addWidget(self.words_list)

        self.central_widget.setLayout(self.layout)
        self.back_btn = QPushButton("Back")
        self.layout.addWidget(self.back_btn)

        self.central_widget.setLayout(self.layout)

        self.menu = QMenu()
        self.add_action = QAction("Add", self.words_list)
        self.delete_action = QAction("Delete", self.words_list)
        self.menu.addAction(self.add_action)
        self.menu.addAction(self.delete_action)
        self.words_list.setContextMenuPolicy(Qt.CustomContextMenu)
