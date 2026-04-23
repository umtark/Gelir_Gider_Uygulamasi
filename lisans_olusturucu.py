import sys
import uuid
import hashlib
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt6.QtCore import Qt

def generate_key():
    token = str(uuid.uuid4()).split('-')[0].upper()
    secret = "GELIR_GIDER_SECRET_2026"
    hashed = hashlib.sha256((token + secret).encode()).hexdigest()[:4].upper()
    return f"LCS-{token}-{hashed}"

class LicenseGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gelir Gider - Lisans Üretici (15 Günlük)")
        self.setFixedSize(350, 200)
        self.setStyleSheet("font-family: Quicksand; font-size: 14px;")
        
        layout = QVBoxLayout(self)
        
        self.lbl = QLabel("Yeni bir lisans anahtarı oluşturun\n(Bu anahtar uygulamaya +15 gün kazandırır):")
        self.lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.lbl)
        
        self.btn = QPushButton("Lisans Üret")
        self.btn.setStyleSheet("background-color: #10b981; color: white; padding: 10px; font-weight: bold; border-radius: 5px;")
        self.btn.clicked.connect(self.generate)
        layout.addWidget(self.btn)
        
        self.out_box = QLineEdit()
        self.out_box.setReadOnly(True)
        self.out_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.out_box.setStyleSheet("font-size: 16px; font-weight: bold; padding: 5px;")
        layout.addWidget(self.out_box)

    def generate(self):
        key = generate_key()
        self.out_box.setText(key)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = LicenseGenerator()
    win.show()
    sys.exit(app.exec())
