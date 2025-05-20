import psutil
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar, QTimer

class SystemStatsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("System Monitor")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.cpu_label = QLabel("CPU Usage")
        self.cpu_bar = QProgressBar()
        layout.addWidget(self.cpu_label)
        layout.addWidget(self.cpu_bar)

        self.ram_label = QLabel("RAM Usage")
        self.ram_bar = QProgressBar()
        layout.addWidget(self.ram_label)
        layout.addWidget(self.ram_bar)

        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000)  # update every second

    def update_stats(self):
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent

        self.cpu_bar.setValue(int(cpu))
        self.ram_bar.setValue(int(ram))