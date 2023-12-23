from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sqlite3
from .AddWord import UI_AddWord

#Create GUI and connect functions
class AddWord(QMainWindow, UI_AddWord):
    def __init__(self, *args, **kwargs):
        super(AddWord, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.db_connection = sqlite3.connect('alias_game.db')
        self.load_categories()
        self.update_button.clicked.connect(self.update_data)

#Loads category from db   
    def load_categories(self, status = None):        
        #Find category
        cursor = self.db_connection.cursor()
        cursor.execute('SELECT DISTINCT Category FROM Words')
        categories = [category[0] for category in cursor.fetchall()]
        self.category_input.addItems(categories)
        #Check status, if its not NONE than combobox saves his status
        if status != None:
            self.category_input.setCurrentIndex(categories.index(status))
#Updates db
    def update_data(self):
        word = self.word_input.text()
        category = self.category_input.currentText()
        ExplanationOfWord = self.ExplanationOfWord_input.text()
        #Adds word, category and explanation of word to bd if them aren't NONE
        if word and category and ExplanationOfWord:
            cursor = self.db_connection.cursor()
            cursor.execute('INSERT INTO Words  (Category, Word, ExplanationOfWord) VALUES (?, ?, ?)',
                           (category, word, ExplanationOfWord))
            self.db_connection.commit()
            #Clears every inputs
            self.word_input.clear()
            self.category_input.clear()
            self.ExplanationOfWord_input.clear()
            self.load_categories(category)
        #Updates the parent GUI
        self.parent().load_categories(category)
        self.parent().select_category()

    def closeEvent(self, event):
        event.accept()

