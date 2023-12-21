from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sqlite3
from .ShowWords import Ui_ShowWords
from ..AddWord.window import AddWord

#Create GUI and connect functions
class ShowWords(QMainWindow, Ui_ShowWords):
    def __init__(self, *args, **kwargs):
        super(ShowWords, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.db_connection = sqlite3.connect('alias_game.db')
        self.create_table()
        self.load_categories()
        self.select_btn.clicked.connect(self.select_category)
        self.back_btn.clicked.connect(self.close)# CHANGE TO BACK
        self.words_list.customContextMenuRequested.connect(self.show_context_menu)
        self.delete_action.triggered.connect(self.remove_item)
        self.add_action.triggered.connect(self.update_database)

#! Move to another File
    def create_table(self):
        cursor = self.db_connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Words (
                            WordID INTEGER PRIMARY KEY,
                            Category TEXT NOT NULL,
                            Word TEXT NOT NULL,
                            ExplanationOfWord TEXT NOT NULL
                        )''')
        
        # cursor.execute('INSERT INTO Words  (Category, Word, ExplanationOfWord) VALUES (?, ?, ?)',
        #                    ("...", "...", "..."))
        self.db_connection.commit()

#Remove items from curent category
    def remove_item(self):
        selected_item = self.words_list.currentItem()
        cursor = self.db_connection.cursor()

#Removes only not NONE 
        if selected_item is not None:
            #Here find what word, category and explanation of word to remove
            word, explanationofword = selected_item.text().split(" - ")
            category = self.category_combobox.currentText()
            #Here removes that things
            cursor.execute('DELETE FROM Words WHERE Category = ? AND Word = ? AND ExplanationOfWord = ?',
               (category, word, explanationofword))
            #If word was last in this category than this function works and reload categories
            if self.words_list.count() == 1:
                self.load_categories()
            #Here removes from QListWidget
            self.words_list.takeItem(self.words_list.row(selected_item))
            #Here saves changes in db
            self.db_connection.commit()

#Show contex menu
    def show_context_menu(self,position):
        self.menu.exec_(self.words_list.mapToGlobal(position))

#Open GUI for adding word and explanation of word
    def update_database(self):
        self.AWwindow = AddWord(self)
        self.AWwindow.show()

#Loads category from db
    def load_categories(self, status = None):
        #Cleans combobox
        self.category_combobox.clear()
        #Find category
        cursor = self.db_connection.cursor()
        cursor.execute('SELECT DISTINCT Category FROM Words')
        categories = [category[0] for category in cursor.fetchall()]
        self.category_combobox.addItems(categories)
        #Check status, if its not NONE than combobox saves his status
        if status != None:
            self.category_combobox.setCurrentIndex(categories.index(status))

    def select_category(self):
        selected_category = self.category_combobox.currentText()
        cursor = self.db_connection.cursor()

        # Find words for category
        cursor.execute("SELECT Word, ExplanationOfWord FROM Words WHERE Category=?", (selected_category,))
        words_data = cursor.fetchall()

        # Clear old
        self.words_list.clear()

        # Show words from category
        for word, explanation in words_data:
            item = f"{word} - {explanation}"
            self.words_list.addItem(item)
        self.load_categories(selected_category)

#Checks if this GUI is closed and of closed than closes his subwindow
    def closeEvent(self, event):
        if hasattr(self, 'AWwindow') and self.AWwindow.isVisible():
            self.AWwindow.close()
        self.parent().setEnabled(True)
        event.accept()

