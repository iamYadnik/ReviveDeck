import sys
import os
import shutil
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog, QMessageBox
)

CONFIG_DIR = "config/"
BACKUP_DIR = "backups/"

class BackupRestoreGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Backup & Restore Manager")
        self.setGeometry(300, 250, 500, 250)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("📦 Backup or restore your configuration files")
        layout.addWidget(self.label)

        self.backup_button = QPushButton("Create Backup")
        self.backup_button.clicked.connect(self.create_backup)
        layout.addWidget(self.backup_button)

        self.restore_button = QPushButton("Restore from Backup")
        self.restore_button.clicked.connect(self.restore_backup)
        layout.addWidget(self.restore_button)

        self.setLayout(layout)
        os.makedirs(BACKUP_DIR, exist_ok=True)

    def create_backup(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"revivedeck_backup_{timestamp}"
        backup_path = os.path.join(BACKUP_DIR, backup_name)
        try:
            shutil.make_archive(backup_path, 'zip', CONFIG_DIR)
            QMessageBox.information(self, "Backup Created", f"✅ Backup saved as: {backup_name}.zip")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to create backup: {e}")

    def restore_backup(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Backup Zip", BACKUP_DIR, "Zip Files (*.zip)")
        if file_path:
            try:
                shutil.unpack_archive(file_path, CONFIG_DIR, 'zip')
                QMessageBox.information(self, "Restored", "✅ Configuration restored successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to restore: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BackupRestoreGUI()
    window.show()
    sys.exit(app.exec_())