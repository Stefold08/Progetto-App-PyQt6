import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("La mia prima vera app")
        self.resize(600, 400)
        self.label = QLabel("Benvenuto Nella mia app")
        self.Button = QPushButton("Premi Questo Pulsante")
        self.Button.clicked.connect(self.change_text)
        layout = QVBoxLayout()
        
        layout.addWidget(self.label)
        layout.addWidget(self.Button)
        
        self.setLayout(layout)
        
    def change_text(self):
        self.label.setText("Bottone Premuto")
        
app = QApplication(sys.argv)

window = Window()
window.show()

app.exec()
