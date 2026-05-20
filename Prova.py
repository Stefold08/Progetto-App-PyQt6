import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Calcolatrice")
        self.setFixedSize(300, 400)
        
        self.expression = ""
        
        #Display
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 24px; padding: 10px;")
        
        #Layout Principale
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)
        
        grid = QGridLayout()
        
        buttons = [ 
            "7", "8", "9", "/", 
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]
        
        positions = [(i, j) for i in range(4) for j in range(4)]
        
        for position, button_text in zip(positions, buttons):
            button = QPushButton(button_text)
            button.setSyleSheet("font-size: 18px; padding: 10px;")
            
            button.clicked.connect(lambda _, text=button_text: self.on_click(text))
            grid.addWidget(button, *position)
            
        main_layout.addLayout(grid)
        self.setLayout(main_layout)
        
        def on_click(self, text):
            if text == "C":
                self.expression = ""
                self.display.setText("")
                return
            
            if text == "=":
                try:
                    result = eval(self.expression)
                    self.display.setText(str(result))
                    self.expression = str(result)
                except:
                    self.display.setText("Errore")
                    self.expression = ""
                return
                
            self.expression += text
            self.display.setText(self.expression)
            
app = QApplication(sys.argv)
window = Calculator()
window.show()
app.exec()
            