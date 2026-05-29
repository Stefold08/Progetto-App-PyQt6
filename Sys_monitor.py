import sys 
import psutil

from PyQt6.QtCore import Qt, QTime
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,QStackedWidget, QTableWidget, QTableWidgetItem, QFrame, QProgressBar

class SidebarButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        
        self.setMinimumHeight(48)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
    
class MetricCard(QFrame):
    def __init__(self, title, value):
        super().__init__()
        
        self.setObjectName("Card")
        
        layout = QVBoxLayout(self)
        
        self.title = QLabel(title)
        self.title.setObjectName("cardTitle")
        
        self.value = QLabel(value)
        self.value.setObjectName("CardValue")
        
        layout.addWidget(self.title)
        layout.addWidget(self.value)
        
    def set_value(self, text):
        self.value.setText(text)
        