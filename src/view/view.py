from PyQt5.QtWidgets import QDialog, QMainWindow, QMessageBox
from PyQt5.uic import loadUi

from .view_designer import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def find_and_replace(self):
        dialog = FindReplaceDialog(self)
        dialog.exec()

    def about(self):
        QMessageBox.about(
            self,
            "About Sample Editor",
            "<p>A sample text editor app built with:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>",
        )

    def show_text(self, text):
        self.textEdit.setText(text)


class FindReplaceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("../view/ui_files/dialog.ui", self)
