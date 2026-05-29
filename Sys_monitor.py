import sys 
import psutil

from PyQt6.QtCore import Qt, QTimer
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
        
class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout(self)
        layout.setSpacing(16)
        
        title = QLabel("Dashboard")
        title.setObjectName("PageTitle")
        
        layout.addWidget(title)
        
        cards_layout = QHBoxLayout()
        
        self.cpu_card = MetricCard("CPU", "0%")
        self.ram_card = MetricCard("RAM", "0%")
        self.process_card = MetricCard("Processi", "0")
        
        cards_layout.addWidget(self.cpu_card)
        cards_layout.addWidget(self.ram_card)
        cards_layout.addWidget(self.process_card)
        
        layout.addLayout(cards_layout)
        
        self.cpu_bar = QProgressBar()
        self.cpu_bar.setValue(0)
        
        self.ram_bar = QProgressBar()
        self.ram_bar.setValue(0)
        
        layout.addWidget(QLabel("CPU Usage"))
        layout.addWidget(self.cpu_bar)
        
        layout.addWidget(QLabel("RAM Usage"))
        layout.addWidget(self.ram_bar)
        
        layout.addStretch()
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000)
        
        self.update_stats()
        
    def update_stats(self):
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        processes = len(psutil.pids())
        
        self.cpu_card.set_value(f"{cpu}%")
        self.ram_card.set_value(f"{ram}%")
        self.process_card.set_value(str(processes))
        
        self.cpu_bar.setValue(int(cpu))
        self.ram_bar.setValue(int(ram))
        
        
class ProcessesPage(QWidget):
    def __int__(self):
        super().__init__()
        
        layout = QVBoxLayout(self)
        
        title = QLabel("Processi")
        title.setObjectName("PageTitle")
        
        layout.addWidget(title)
        
        self.table = QTableWidget()
        
        self.table = QTableWidget()
        
        self.table.setColumnCount(4)
        