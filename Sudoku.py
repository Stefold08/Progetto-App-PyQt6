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
                
                cell.setStyleSheet("""font-size:22px; background:#ffffff;""")
                
                cell.textChanged.connect(lambda text, c=cell: self.validate_input(c))
                
                grid.addWidget(cell, row, col)
                
                row_cells.append(cell)
                
            self.cells.append(row_cells)
            
        main_layout.addLayout(grid)
        
        self.message = QLabel("")
        self.message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        main_layout.addWidget(self.message)
        
        check_btn = QPushButton("Controlla")
        check_btn = QPushButton("Pulisci")
        
                