from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sqlite3
from .AddWord import UI_AddWord

class AddWord(QMainWindow, UI_AddWord):
    def __init__(self, *args, **kwargs):
        super(AddWord, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.db_connection = sqlite3.connect('alias_game.db')
        self.load_categories()
        self.update_button.clicked.connect(self.update_data)

    def onChangeBackgroundClicked(self):
        fileName,  = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (.png.jpg *.bmp)")
        if fileName:
            self.setStyleSheet(f"QWidget {{ background-image: url('{fileName}'); }}")

    
    def load_categories(self, status = None):        
        cursor = self.db_connection.cursor()
        cursor.execute('SELECT DISTINCT Category FROM Words')
        categories = [category[0] for category in cursor.fetchall()]
        self.category_input.addItems(categories)
        if status != None:
            self.category_input.setCurrentIndex(categories.index(status))

    def update_data(self):
        word = self.word_input.text()
        category = self.category_input.currentText()
        ExplanationOfWord = self.ExplanationOfWord_input.text()

        if word and category and ExplanationOfWord:
            cursor = self.db_connection.cursor()
            cursor.execute('INSERT INTO Words  (Category, Word, ExplanationOfWord) VALUES (?, ?, ?)',
                           (category, word, ExplanationOfWord))
            self.db_connection.commit()
            self.word_input.clear()
            self.category_input.clear()
            self.ExplanationOfWord_input.clear()
            self.load_categories(category)
        self.parent().load_categories(category)
        self.parent().select_category()

    def closeEvent(self, event):
        event.accept()

