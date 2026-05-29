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
        
        home_layout.addWidget(QLabel("Benvenuto nella Home"))
        
        home_page.setLayout(home_layout)
        
        #Page settings
        settings_page = QWidget()
        settings_layout = QVBoxLayout()
        
        settings_layout.addWidget(QLabel("Impostazioni"))
        
        settings_page.setLayout(settings_layout)
        
        self.pages.addWidget(home_page)
        self.pages.addWidget(settings_page)
        
        #Bottoni Di Navigazione
        self.home_btn.clicked.connect(lambda: self.pages.setCurrentIndex(0))
        
        self.settings_btn.clicked.connect(lambda: self.pages.setCurrentIndex(1))
        
        #Layout Finale
        main_layout.addLayout(sidebar)
        main_layout.addWidget(self.pages)
        
        self.setLayout(main_layout)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()