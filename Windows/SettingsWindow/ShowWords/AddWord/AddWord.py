from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QComboBox

class UI_AddWord(object):
    def setupUi(self, Form):

        Form.setWindowTitle("Add New Words")
        Form.setFixedSize(400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        self.category_label = QLabel("Category:")
        self.category_input = QComboBox()

        self.category_input.setEditable(True)  
        self.layout.addWidget(self.category_label)
        self.layout.addWidget(self.category_input)

        self.word_label = QLabel("Word:")
        self.word_input = QLineEdit()
        self.layout.addWidget(self.word_label)
        self.layout.addWidget(self.word_input)

        self.ExplanationOfWord_label = QLabel("Explanation Of Word level:")
        self.ExplanationOfWord_input = QLineEdit()
        self.layout.addWidget(self.ExplanationOfWord_label)
        self.layout.addWidget(self.ExplanationOfWord_input)
        #! add word meaning

        self.update_button = QPushButton("Update")
        self.layout.addWidget(self.update_button)

        self.central_widget.setLayout(self.layout)
