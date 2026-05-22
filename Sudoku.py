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
        clear_btn = QPushButton("Pulisci")
        
        check_btn.clicked.connect(self.check_board)
        clear_btn.clicked.connect(self.clear_board)
        main_layout.addWidget(check_btn)
        main_layout.addWidget(clear_btn)

        self.setLayout(main_layout)
        
    def validate_input(self, cell):
        text = cell.text()
        
        if text and text not in "123456789":
            cell.setText("")
            
    def get_board(self):
        board = []
        
        for row in self.cells:
            
            values = []
            
            for cell in row:
                
                value = cell.text()
                
                values.append(int(value) if value else 0)
                
            board.append(values)

        return board
    
    def valid_group(self, numbers):
        
        values = [n for n in numbers if n != 0]
        
        return len(values) == len(set(values))
    
    def check_board(self):
        bouard = self.get_board()
        
        for row in board:
            if not self.valid_group(row):
                self.message.setText("Errore nelle righe")
                return
            
        for col in range(9):
            
            values = []