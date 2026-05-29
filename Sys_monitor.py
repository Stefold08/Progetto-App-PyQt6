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

        # TITOLO
        title = QLabel("Task Manager")
        title.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
        """)

        main_layout.addWidget(title)

        # TABELLA PROCESSI
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

        # BOTTONI
        button_layout = QHBoxLayout()

        self.refresh_btn = QPushButton("Aggiorna")
        self.kill_btn = QPushButton("Termina Processo")

        button_layout.addWidget(self.refresh_btn)
        button_layout.addWidget(self.kill_btn)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        # EVENTI
        self.refresh_btn.clicked.connect(self.load_processes)
        self.kill_btn.clicked.connect(self.kill_process)

        # TIMER AUTO REFRESH
        self.timer = QTimer()
        self.timer.timeout.connect(self.load_processes)
        self.timer.start(3000)

        # STILE
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e2e;
                color: white;
                font-size: 14px;
            }

            QTableWidget {
                background-color: #2b2b3a;
                gridline-color: #444;
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
            'cpu_percent',
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
            for column, value in enumerate(process):

                item = QTableWidgetItem(str(value))

                self.table.setItem(row, column, item)

    def kill_process(self):

        selected_row = self.table.currentRow()

        if selected_row == -1:
            QMessageBox.warning(
                self,
                "Errore",
                "Seleziona un processo"
            )
            return

        pid_item = self.table.item(selected_row, 1)

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