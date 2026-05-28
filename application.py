import sys 
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QStackedWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Application MultiWindow")
        self.resize(800, 500)
        
        main_layout = QHBoxLayout()
        
        sidebar = QVBoxLayout()
        
        self.home_btn = QPushButton("Home")
        self.settings_btn = QPushButton("Settings")
        
        sidebar.addWidget(self.home_btn)
        sidebar.addWidget(self.settings_btn)
        
        self.pages = QStackedWidget()
        
        home_page = QWidget()
        home_layout = QVBoxLayout()
        
        home_layout.addWidget