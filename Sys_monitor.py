import sys
import psutil

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QLabel,
    QMessageBox,
    QHBoxLayout
)
from PyQt6.QtCore import QTimer

class TaskManager(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Task Manager")
        self.resize(900, 600)
        
        main_layout = QVBoxLayout()
        
        title = QLabel("Task Manager")
        title.setStyleSheet(""" font-size: 28px; font-weight: bold;""")
        
        main_layout.addWidget(title)
        
        self.table = QTableWidget()
        
        self.table.setColumnCount(4)
        
        self.table.setHorizontalHeaderLabels([
            "Nome",
            "PID", 
            "CPU %",
            "RAM MB"
        ])
        
        self.table.horizontalHeader().setStretchLastSection(True)
        
        main_layout.addWidget(self.table)
        
        button_layout = QHBoxLayout()
        
        self.refresh_btn = QPushButton("Aggiorna")
        self.kill_btn = QPushButton("Termina Processo")
        
        main_layout.addLayout(button_layout)
        
        self.setLayout(main_layout)
        
        self.refresh_btn.clicked.connect(self.load_processes)
        self.kill_btn.clicked.connect(self.kill_process)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.load_processes)
        self.timer.start(3000)
        
        #Stile
        self.setStyleSheet(""" 
            QWidget {
                background-color: #1e1e2e;
                color: white;
                font-size: 14px;
            }
            
            QTableWidget {
                background-color: #2b2b3a;
                grindline-color: #444
            }
            
            QPushButton {
                background-color: #7289da;
                border: none;
                border-radius: 8px;
                padding: 10px;
            }
            
            QPushButton:hover {
                background-color: #5b6eae;
            }      
        """)
        
        self.load_processes()
        
    def load_processes(self):
        processes = []
        
        for process in psutil.process_iter([
            'pid',
            'name', 
            'cpu_percet', 
            'memory_info'
        ]):
            try:
                pid = process.info['pid']
                name = process.info['name']
                cpu = process.info['cpu_percent']
                
                memory = process.info['memory_info'].rss
                memory_mb = round(memory / 1024 / 1024, 2)
                
                processes.append([
                    name,
                    pid,
                    cpu,
                    memory_mb
                ])
            except:
                pass
            
        self.table.setRowCount(len(processes))
        
        for row, process in enumerate(processes):
            for column, vale in enumerate(processes):
                
                item = QTableWidgetItem(str(vale))
                
                self.table.setItem(row, column, item)
                
    def kill_process(self):
         
        select_row = self.tabel.currentRow()
        
        if select_row == -1:
            QMessageBox.warning(
                self,
                "Errore",
                "Seleziona un proceso"
            )
            return
        
        pid_item = self.table.item(select_row, 1)
        
        pid = int(pid_item.text())
        
        try:
            process = psutil.Process(pid)
            process.terminate()
            
            QMessageBox.information(
                self,
                "Successo",
                f"Processo {pid} terminato"
            )
            
            self.load_processes()
            
        except Exception as error:
            QMessageBox.critical(
                self,
                "Errore",
                str(error)
            )
            
app = QApplication(sys.argv)

window = TaskManager()
window.show()

app.exec()