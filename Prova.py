import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("La mia prima vera app")
        self.resize(600, 400)
        self.label = QLabel("Benvenuto")
        self.label1 = QLabel("come stai oggi?")
        self.Button = QPushButton("Sto Bene!")
        self.Button1 = QPushButton("sto male")
        self.Button.clicked.connect(self.change_text_bene)
        self.Button1.clicked.connect(self.change_text_male)
        layout = QVBoxLayout()
        
        layout.addWidget(self.label)
        layout.addWidget(self.label1)
        layout.addWidget(self.Button1)
        layout.addWidget(self.Button)
        
        self.setLayout(layout)
        
    def change_text_bene(self):
        self.label.setText("Sono contento, Spero te passi una buona giornata")
        
    def change_text_male(self):
        self.label.setText("mi dispiace tanto, spero te possa migliorare la tua giornata")
        
app = QApplication(sys.argv)

window = Window()
window.show()

app.exec()
