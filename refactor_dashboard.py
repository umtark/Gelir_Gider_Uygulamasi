import re, shutil

# Backup
shutil.copy("fatura_masaustu.py", "fatura_masaustu.py.bak")

with open("fatura_masaustu.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Menu Buttons creation
old_menu_btns = '''        self.btn_menu_fatura = QToolButton()
        self.btn_menu_fatura.setText(_t("menu_fatura", "Fatura\\nYönetimi"))
        self.btn_menu_fatura.setIcon(QIcon("data/anim/Menu_fatura.png"))
        self.btn_menu_fatura.setIconSize(QSize(110, 110))
        self.btn_menu_fatura.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.btn_menu_fatura.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.btn_menu_arac = QToolButton()'''

new_menu_btns = '''        self.btn_menu_dashboard = QToolButton()
        self.btn_menu_dashboard.setText(_t("menu_dashboard", "Ana Sayfa\\nPaneli"))
        # We don't have a specific icon, maybe reuse Ayarlar or Fatura?
        # A good fallback is the check icon or similar if they have it
        # Try to use a placeholder or something simple
        self.btn_menu_dashboard.setIcon(QIcon("data/anim/Genel statistikler.png") if os.path.exists("data/anim/Genel statistikler.png") else QIcon("data/anim/raporlar.png"))
        self.btn_menu_dashboard.setIconSize(QSize(110, 110))
        self.btn_menu_dashboard.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.btn_menu_dashboard.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.btn_menu_fatura = QToolButton()
        self.btn_menu_fatura.setText(_t("menu_fatura", "Fatura\\nYönetimi"))
        self.btn_menu_fatura.setIcon(QIcon("data/anim/Menu_fatura.png"))
        self.btn_menu_fatura.setIconSize(QSize(110, 110))
        self.btn_menu_fatura.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.btn_menu_fatura.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.btn_menu_arac = QToolButton()'''

content = content.replace(old_menu_btns, new_menu_btns)

# 2. Add btn_menu_dashboard to the sidebar layout loop
content = content.replace(
'''for btn in (self.btn_menu_fatura, self.btn_menu_arac, self.btn_menu_ayarlar):''',
'''for btn in (self.btn_menu_dashboard, self.btn_menu_fatura, self.btn_menu_arac, self.btn_menu_ayarlar):'''
)

# 3. Connect buttons routing offsets
content = content.replace(
'''        self.btn_menu_fatura.clicked.connect(lambda: self.switch_page(0))
        self.btn_menu_arac.clicked.connect(lambda: self.switch_page(1))
        self.btn_menu_ayarlar.clicked.connect(lambda: self.switch_page(2))''',
'''        self.btn_menu_dashboard.clicked.connect(lambda: self.switch_page(0))
        self.btn_menu_fatura.clicked.connect(lambda: self.switch_page(1))
        self.btn_menu_arac.clicked.connect(lambda: self.switch_page(2))
        self.btn_menu_ayarlar.clicked.connect(lambda: self.switch_page(3))'''
)

# 4. Hide texts in toggle
content = content.replace(
'''            self.btn_menu_fatura.setText(" \\n ")
            self.btn_menu_arac.setText(" \\n ")
            self.btn_menu_ayarlar.setText(" \\n ")''',
'''            self.btn_menu_dashboard.setText(" \\n ")
            self.btn_menu_fatura.setText(" \\n ")
            self.btn_menu_arac.setText(" \\n ")
            self.btn_menu_ayarlar.setText(" \\n ")'''
)

content = content.replace(
'''            self.btn_menu_fatura.setText(_t("menu_fatura", "Fatura\\nYönetimi"))
            self.btn_menu_arac.setText(_t("menu_arac", "Araç\\nYönetimi"))
            self.btn_menu_ayarlar.setText(_t("menu_ayarlar", "Ayarlar"))''',
'''            self.btn_menu_dashboard.setText(_t("menu_dashboard", "Ana Sayfa\\nPaneli"))
            self.btn_menu_fatura.setText(_t("menu_fatura", "Fatura\\nYönetimi"))
            self.btn_menu_arac.setText(_t("menu_arac", "Araç\\nYönetimi"))
            self.btn_menu_ayarlar.setText(_t("menu_ayarlar", "Ayarlar"))'''
)

# 5. SetChecked offsets
content = content.replace(
'''        self.btn_menu_fatura.setChecked(index == 0)
        self.btn_menu_arac.setChecked(index == 1)
        self.btn_menu_ayarlar.setChecked(index == 2)''',
'''        self.btn_menu_dashboard.setChecked(index == 0)
        self.btn_menu_fatura.setChecked(index == 1)
        self.btn_menu_arac.setChecked(index == 2)
        self.btn_menu_ayarlar.setChecked(index == 3)'''
)

# 6. ApplyTheme texts
content = content.replace(
'''        self.btn_menu_fatura.setText(_t("menu_fatura", "Fatura\\nYönetimi"))
        self.btn_menu_arac.setText(_t("menu_arac", "Araç\\nYönetimi"))
        self.btn_menu_ayarlar.setText(_t("menu_ayarlar", "Ayarlar"))''',
'''        self.btn_menu_dashboard.setText(_t("menu_dashboard", "Ana Sayfa\\nPaneli"))
        self.btn_menu_fatura.setText(_t("menu_fatura", "Fatura\\nYönetimi"))
        self.btn_menu_arac.setText(_t("menu_arac", "Araç\\nYönetimi"))
        self.btn_menu_ayarlar.setText(_t("menu_ayarlar", "Ayarlar"))'''
)

# 7. Add Dashboard Page into Stack setup
page_dashboard_code = '''
        # --- DASHBOARD PAGE ---
        self.page_dashboard = QWidget()
        dash_lyt = QVBoxLayout(self.page_dashboard)
        dash_lyt.setContentsMargins(20, 20, 20, 35)
        
        dash_title = QLabel(_t("dashboard_title", "Sistem Genel Özeti (Dashboard)"))
        dash_title.setFont(get_custom_font("Quicksand", 20, QFont.Weight.DemiBold))
        dash_title.setStyleSheet("padding: 10px; background-color: transparent;")
        dash_lyt.addWidget(dash_title)

        # Top KPI Cards
        kpi_w = QWidget()
        kpi_lyt = QHBoxLayout(kpi_w)
        kpi_w.setStyleSheet("background-color: transparent;")
        dash_lyt.addWidget(kpi_w)

        def create_kpi(title, value_lbl):
            f = QFrame()
            f.setStyleSheet("""
                QFrame {
                    background-color: #2e1065;
                    border-radius: 8px;
                    border: 1px solid #7c3aed;
                }
                QLabel { background-color: transparent; }
            """)
            l = QVBoxLayout(f)
            t = QLabel(title)
            t.setFont(get_custom_font("Quicksand", 12))
            t.setStyleSheet("color: #a78bfa;")
            value_lbl.setFont(get_custom_font("Quicksand", 18, QFont.Weight.Bold))
            value_lbl.setStyleSheet("color: white;")
            l.addWidget(t)
            l.addWidget(value_lbl)
            return f

        self.kpi_arac_sayisi = QLabel("0")
        self.kpi_gider_aylik = QLabel("0.00 TL")
        self.kpi_gelir_aylik = QLabel("0.00 TL")
        self.kpi_uyarilar = QLabel("0")

        kpi_lyt.addWidget(create_kpi(_t("kpi_toplam_arac", "Toplam Aktif Araç"), self.kpi_arac_sayisi))
        kpi_lyt.addWidget(create_kpi(_t("kpi_aylik_gider", "Bu Ayki Giderler"), self.kpi_gider_aylik))
        kpi_lyt.addWidget(create_kpi(_t("kpi_aylik_gelir", "Bu Ayki Gelirler"), self.kpi_gelir_aylik))
        kpi_lyt.addWidget(create_kpi(_t("kpi_kritik_uyari", "Kritik Uyarýlar (Geçen/Yaklaþan)"), self.kpi_uyarilar))

        # Bottom Tables Left/Right split
        dash_tables_w = QWidget()
        dash_tables_lyt = QHBoxLayout(dash_tables_w)
        dash_lyt.addWidget(dash_tables_w, stretch=1)

        # Left Table (Alerts)
        gp_alerts = QGroupBox(_t("dash_alerts", "Acil Durumlar & Yaklaþan Bakýmlar"))
        gp_alerts.setStyleSheet("QGroupBox { background-color: transparent; font-weight: bold; border: 1px solid #dc2626; border-radius: 6px; margin-top: 15px;} QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top center; color: #ef4444; }")
        al_lyt = QVBoxLayout(gp_alerts)
        self.table_alerts = QTableWidget()
        self.table_alerts.setColumnCount(4)
        self.table_alerts.setHorizontalHeaderLabels([_t("plaka", "Plaka"), _t("uyari_tipi", "Uyarý Tipi"), _t("durum", "Durum"), _t("kalan", "Kalan")])
        self.table_alerts.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table_alerts.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table_alerts.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        al_lyt.addWidget(self.table_alerts)
        dash_tables_lyt.addWidget(gp_alerts, stretch=1)

        # Right Table (Recent Activity)
        gp_events = QGroupBox(_t("dash_events", "Son Hareketler (þlemler & Adýmlar)"))
        gp_events.setStyleSheet("QGroupBox { background-color: transparent; font-weight: bold; border: 1px solid #2563eb; border-radius: 6px; margin-top: 15px;} QGroupBox::title { subcontrol-origin: margin; subcontrol-position: top center; color: #3b82f6; }")
        ev_lyt = QVBoxLayout(gp_events)
        self.table_events = QTableWidget()
        self.table_events.setColumnCount(3)
        self.table_events.setHorizontalHeaderLabels([_t("tarih", "Tarih"), _t("olay", "Olay & Detay"), _t("tutar", "Tutar/Maliyet")])
        self.table_events.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table_events.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table_events.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        ev_lyt.addWidget(self.table_events)
        dash_tables_lyt.addWidget(gp_events, stretch=1)

        self.stack.addWidget(self.page_dashboard)
'''

# Find the spot to inject dashboard page layout. We can inject it right before self.stack.addWidget(self.page_fatura)
# But wait, self.stack.addWidget operations are spread around.
# Actually I'll replace the first stack.addWidget so it places self.page_dashboard first.
content = content.replace('        self.stack.addWidget(self.page_fatura)', page_dashboard_code + '\\n        self.stack.addWidget(self.page_fatura)')


# 8. Remove the TickerWidget completely from fatura_masaustu.py
# First find line: self.arac_ticker = TickerWidget()
# arac_lyt.addWidget(self.arac_ticker)
# Just regex remove them.
content = re.sub(r'\\s*self\.arac_ticker = TickerWidget\\(\\)', '', content)
content = re.sub(r'\\s*arac_lyt\\.addWidget\\(self\\.arac_ticker\\)\\s*', '\\n', content)
content = re.sub(r'class TickerWidget\\(QWidget\\):.*?(?=\\nclass )', '', content, flags=re.DOTALL) # remove class TickerWidget


with open("fatura_masaustu.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Dashboard refactor script done!")
