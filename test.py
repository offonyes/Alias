import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Главное окно')
        self.setWindowIcon(QIcon('path/to/your/icon.png'))

        self.central_widget = QPushButton('Открыть подокно', self)
        self.central_widget.clicked.connect(self.open_dialog)
        self.setCentralWidget(self.central_widget)

    def open_dialog(self):
        self.dialog = SubWindow(self)
        self.dialog.setWindowIcon(QIcon('path/to/your/icon.png'))
        self.dialog.show()
        self.setEnabled(False)
        self.dialog.setEnabled(True)

    def on_dialog_closed(self):
        self.setEnabled(True)

    def closeEvent(self, event):
        # Обработка закрытия главного окна
        if hasattr(self, 'dialog') and self.dialog.isVisible():
            self.dialog.close()

class SubWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Подокно')

        self.close_button = QPushButton('Закрыть', self)
        self.close_button.clicked.connect(self.close)

    def closeEvent(self, event):
        self.parent().setEnabled(True)
        event.accept()

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
