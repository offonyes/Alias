from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sqlite3
from .ShowWords import Ui_ShowWords
from ..AddWord.window import AddWord

class ShowWords(QMainWindow, Ui_ShowWords):
    def __init__(self, *args, **kwargs):
        super(ShowWords, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.db_connection = sqlite3.connect('alias_game.db')
        self.create_table()
        self.load_categories()
        self.select_btn.clicked.connect(self.select_category)
        self.back_btn.clicked.connect(self.close_windows)# CHANGE TO BACK
        self.words_list.customContextMenuRequested.connect(self.show_context_menu)
        self.delete_action.triggered.connect(self.remove_item)
        self.add_action.triggered.connect(self.update_database)

    def close_windows(self):
        self.close()

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

    def remove_item(self):
        #! TODO ADD REMOWE FROM DB
        selected_item = self.words_list.currentItem()
        if selected_item is not None:
            self.words_list.takeItem(self.words_list.row(selected_item))
            
    def show_context_menu(self,position):
        self.menu.exec_(self.words_list.mapToGlobal(position))

    def update_database(self):
        self.AWwindow = AddWord(self)
        self.AWwindow.show()

    def load_categories(self, status = None):
        self.category_combobox.clear()
        cursor = self.db_connection.cursor()
        cursor.execute('SELECT DISTINCT Category FROM Words')
        categories = [category[0] for category in cursor.fetchall()]
        self.category_combobox.addItems(categories)
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

    def closeEvent(self, event):
        if hasattr(self, 'AWwindow') and self.AWwindow.isVisible():
            self.AWwindow.close()
        self.parent().setEnabled(True)
        event.accept()

