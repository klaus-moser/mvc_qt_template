from PyQt5.QtWidgets import QDialog, QMainWindow, QMessageBox
from PyQt5.uic import loadUi

from .view_designer import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connect_signals_slots()

    def connect_signals_slots(self):
        self.action_Exit.triggered.connect(self.close)
        self.action_Find_and_Repleace.triggered.connect(self.find_and_replace)
        self.action_About.triggered.connect(self.about)

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


class FindReplaceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("../view/ui_files/dialog.ui", self)
