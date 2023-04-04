from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Fenster(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI-Programmierung")
        
        layout_top = QVBoxLayout()
        layout_bottom = QFormLayout()

        self.vorname = QLineEdit()
        self.name = QLineEdit()
        self.geburtstag = QDateEdit()
        self.geburtstag.setDisplayFormat("d/M/yyyy")
        self.adresse = QLineEdit()
        self.plz = QLineEdit()
        self.ort = QLineEdit()
        self.land = QComboBox()
        self.land.addItems(["Schweiz", "Deutschland", "Österreich"])
        self.save_button = QPushButton("Save")

        #Elemente hinzufügen
        layout_bottom.addRow("Vorname:", self.vorname)
        layout_bottom.addRow("Name:", self.name)
        layout_bottom.addRow("Geburtstag:", self.geburtstag)
        layout_bottom.addRow("Adresse:", self.adresse)
        layout_bottom.addRow("PostLeitzahl:", self.plz)
        layout_bottom.addRow("Ort:", self.ort)
        layout_bottom.addRow("Land:", self.land)
        layout_top.addLayout(layout_bottom)
        layout_top.addWidget(self.save_button)

        #Menubar hinzufügen
        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        menusave = QAction("Save", self)
        menuquit = QAction("Quit", self)
        
        filemenu.addAction(menusave)
        filemenu.addAction(menuquit)
     
        #connects
        self.save_button.clicked.connect(self.save)
        menusave.triggered.connect(self.save)
        menuquit.triggered.connect(self.quit)

        center = QWidget()
        center.setLayout(layout_top)

        self.setCentralWidget(center)

        self.show()
        self.raise_()

    def save(self):
        datum = self.geburtstag.date().toString("d/M/yyyy")
        file = open("output.txt", "a", encoding= "utf-8")
        file.write(f"{self.vorname.text()},{self.name.text()},{datum},{self.adresse.text()},{self.plz.text()},{self.ort.text()},{self.land.currentText()}\n")
        file.close()
        self.vorname.clear()
        self.name.clear()
        self.geburtstag.setDate(QDate(2000, 1, 1))
        self.adresse.clear()
        self.plz.clear()
        self.ort.clear()
    
    def quit(self):
        self.close()

app = QApplication([])
win = Fenster()
app.exec()
