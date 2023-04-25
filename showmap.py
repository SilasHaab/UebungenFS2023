from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.uic import *

class UIFenster(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("showmap.ui", self)
        self.show()

        self.buttonkarte.clicked.connect(self.buttonclick)

    def buttonclick(self):
        google = "https://www.google.ch/maps/place/"
        a = self.laenge.text() + ',' + self.breite.text()
        link = google + a
        self.webEngineView.load(QUrl(link))


app = QApplication([])
win = UIFenster()

app.exec()


