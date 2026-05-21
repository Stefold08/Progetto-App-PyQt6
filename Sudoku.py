import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QGridLayout, QVBoxLayout, QPushButton, QLineEdit, QLabel)
from PyQt6.QtCore import Qt

class Sudoku(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Sudoku")
        self.setFixedSize(550, 650)
        
        self.cells = []
        
        main_layout = QVBoxLayout()
        
        title = QLabel("Sudoku")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""font-size:28px; font-weight:bold;""")
        
        main_layout.addWidget(title)
        
        grid = QGridLayout()
        
        for row in range(9):
            row_cells = []
            
            for col in range(9):
                cell = QLineEdit()
                
                cell.setAlignment(Qt.AlignmentFlag.AlignCenter)
                cell.setMaxLength(1)
                
                