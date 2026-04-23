with open('fatura_masaustu.py', encoding='utf-8') as f:
    text = f.read()

import re

# Add sidebar version
old_sidebar = '        self.sidebar_layout.addStretch()'
new_sidebar = '''        self.sidebar_layout.addStretch()

        self.lbl_version = QLabel("v1.0.0")
        self.lbl_version.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_version.setStyleSheet("color: #64748b; font-size: 11px;")
        self.sidebar_layout.addWidget(self.lbl_version)'''
text = text.replace(old_sidebar, new_sidebar)

# Add License dialog and checking logic before class FaturaApp
license_code = '''
class LicenseDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Lisans Aktivasyonu")
        self.setFixedSize(400, 200)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowCloseButtonHint)
        self.setStyleSheet("font-family: Quicksand; font-size: 14px;")
        
        layout = QVBoxLayout(self)
        
        self.info_lbl = QLabel("Uygulama süresi doldu.\\nLütfen 15 günlük yeni lisans anahtarını girin.")
        self.info_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.info_lbl)
        
        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("LCS-XXXX-XXXX")
        self.key_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.key_input.setStyleSheet("font-size: 16px; font-weight: bold; padding: 5px;")
        layout.addWidget(self.key_input)
        
        self.btn_verify = QPushButton("Doğrula ve Etkinleştir")
        self.btn_verify.setStyleSheet("background-color: #10b981; color: white; padding: 10px; font-weight: bold; border-radius: 5px;")
        self.btn_verify.clicked.connect(self.verify_key)
        layout.addWidget(self.btn_verify)

        self.error_lbl = QLabel("")
        self.error_lbl.setStyleSheet("color: red; font-size: 12px;")
        self.error_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.error_lbl)

    def verify_key(self):
        key = self.key_input.text().strip().upper()
        if not key:
            self.error_lbl.setText("Lütfen bir lisans anahtarı girin.")
            return

        import hashlib
        parts = key.split('-')
        if len(parts) == 3 and parts[0] == 'LCS':
            expected_hash = hashlib.sha256((parts[1] + "GELIR_GIDER_SECRET_2026").encode()).hexdigest()[:4].upper()
            if parts[2] == expected_hash:
                # Add 15 days
                self.save_new_license()
                self.accept()
                return

        self.error_lbl.setText("Geçersiz lisans anahtarı!")

    def save_new_license(self):
        lic_file = os.path.join(os.path.expanduser('~'), '.gelir_gider_license.json')
        from datetime import datetime, timedelta
        try:
            with open(lic_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except:
            data = {}
        
        new_expire = datetime.now() + timedelta(days=15)
        data['expire_date'] = new_expire.isoformat()
        
        with open(lic_file, 'w', encoding='utf-8') as f:
            json.dump(data, f)


class FaturaApp'''

text = text.replace('class FaturaApp', license_code)

init_check = '''        self.init_ui()
        self.check_license()

    def check_license(self):
        lic_file = os.path.join(os.path.expanduser('~'), '.gelir_gider_license.json')
        try:
            from datetime import datetime
            with open(lic_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            expire_date = datetime.fromisoformat(data['expire_date'])
        except:
            # First run, force lock
            from datetime import datetime
            expire_date = datetime(2000, 1, 1)

        if datetime.now() > expire_date:
            dlg = LicenseDialog(self)
            dlg.exec()
'''
text = text.replace('        self.init_ui()\n', init_check)

with open('fatura_masaustu.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Added License Dialog and Version Label.')