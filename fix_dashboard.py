import re

with open("fatura_masaustu.py", "r", encoding="utf-8") as f:
    content = f.read()

# Add update_dashboard
refresh_db_code = '''
    def update_dashboard(self):
        try:
            from PyQt6.QtWidgets import QTableWidgetItem
            from PyQt6.QtCore import Qt
            from datetime import datetime
            
            # 1. Araç Sayýsý
            toplam_arac = len(self.araclar)
            if hasattr(self, 'kpi_arac_sayisi'):
                self.kpi_arac_sayisi.setText(f"{toplam_arac} Adet")

            # 2. Gelir & Gider
            now = datetime.now()
            bu_ay_gelir = 0.0
            bu_ay_gider = 0.0
            tum_faturalar_olaylar = []
            
            for r in self.records:
                try:
                    fd = datetime.strptime(r["tarih"], "%d.%m.%Y")
                    # Son Hareketlere Ekler
                    tum_faturalar_olaylar.append({
                        "tarih": fd, "ilgili": r.get('fatura_no', ''),
                        "aciklama": f"Fatura: {r.get('firma', '')}", 
                        "tutar": float(r['toplam']), "tip": r['tip'], "isFatura": True
                    })
                    if fd.month == now.month and fd.year == now.year:
                        val = float(r["toplam"])
                        if r["tip"] == "Gelen":
                            bu_ay_gider += val
                        else:
                            bu_ay_gelir += val
                except: pass

            if hasattr(self, 'kpi_gelir_aylik'):
                self.kpi_gelir_aylik.setText(f"{bu_ay_gelir:,.2f} TL")
                self.kpi_gider_aylik.setText(f"{bu_ay_gider:,.2f} TL")

            # 3. Uyarýlar & Olaylar
            yaklasan_uyarilar = []
            kritik_count = 0
            
            for a in self.araclar:
                plaka = a.get("plaka", "")
                
                for belge_key, belge_adi in [("muayene_tarihi", "Muayene"), ("trafik_sigortasi_tarihi", "Sigorta"), ("kasko_tarihi", "Kasko"), ("koltuk_sigorta_tarihi", "Koltuk Sigortasý")]:
                    tarih = a.get("belgeler", {}).get(belge_key, "")
                    if tarih:
                        try:
                            td = datetime.strptime(tarih, "%d.%m.%Y")
                            kalan = (td.date() - now.date()).days
                            if kalan <= 30:
                                yaklasan_uyarilar.append((plaka, belge_adi, kalan))
                                if kalan <= 15:
                                    kritik_count += 1
                        except: pass
                
                for olay in a.get("olaylar", []):
                    try:
                        od = datetime.strptime(olay['tarih'], "%d.%m.%Y %H:%M")
                        tum_faturalar_olaylar.append({
                            "tarih": od, "ilgili": plaka, "aciklama": olay.get("mesaj",""), 
                            "tutar": float(olay.get("tutar", 0)), "tip": "Gider", "isFatura": False
                        })
                    except: pass
            
            tum_faturalar_olaylar.sort(key=lambda x: x["tarih"], reverse=True)
            
            if hasattr(self, 'kpi_uyarilar'):
                self.kpi_uyarilar.setText(f"{kritik_count} Acil")

            # Fill Alert Table
            if hasattr(self, 'table_alerts'):
                self.table_alerts.setRowCount(0)
                yaklasan_uyarilar.sort(key=lambda x: x[2])
                for r_idx, u in enumerate(yaklasan_uyarilar):
                    self.table_alerts.insertRow(r_idx)
                    
                    p_itm = QTableWidgetItem(u[0])
                    b_itm = QTableWidgetItem(u[1])
                    
                    k_itm = QTableWidgetItem(f"{u[2]} Gün")
                    if u[2] < 0:
                        k_itm.setForeground(Qt.GlobalColor.red)
                        k_itm.setText(f"GEÇT ({-u[2]} Gün)")
                    elif u[2] <= 15:
                        k_itm.setForeground(Qt.GlobalColor.red)
                    else:
                        k_itm.setForeground(Qt.GlobalColor.darkYellow)
                        
                    btn_itm = QTableWidgetItem("ncele")
                    
                    self.table_alerts.setItem(r_idx, 0, p_itm)
                    self.table_alerts.setItem(r_idx, 1, b_itm)
                    self.table_alerts.setItem(r_idx, 2, k_itm)
                    self.table_alerts.setItem(r_idx, 3, btn_itm)

            # Fill Events
            if hasattr(self, 'table_events'):
                self.table_events.setRowCount(0)
                for r_idx, ev in enumerate(tum_faturalar_olaylar[:50]):
                    self.table_events.insertRow(r_idx)
                    try:
                        t_str = ev["tarih"].strftime("%d.%m.%Y %H:%M") if not ev["isFatura"] else ev["tarih"].strftime("%d.%m.%Y")
                    except:
                        t_str = ""
                    
                    t_itm = QTableWidgetItem(t_str)
                    i_itm = QTableWidgetItem(ev["ilgili"])
                    o_itm = QTableWidgetItem(ev["aciklama"])
                    
                    tutar_val = ev["tutar"]
                    tu_itm = QTableWidgetItem(f"{tutar_val:,.2f} TL" if tutar_val else "-")
                    
                    if tutar_val > 0:
                        if ev["tip"] == "Giden" or ev["tip"] == "Gider":
                            tu_itm.setForeground(Qt.GlobalColor.red)
                            tu_itm.setText(f"- {tutar_val:,.2f} TL")
                        else:
                            tu_itm.setForeground(Qt.GlobalColor.green)
                            tu_itm.setText(f"+ {tutar_val:,.2f} TL")
                            
                    self.table_events.setItem(r_idx, 0, t_itm)
                    self.table_events.setItem(r_idx, 1, i_itm)
                    self.table_events.setItem(r_idx, 2, o_itm)
                    self.table_events.setItem(r_idx, 3, tu_itm)
                    
        except Exception as e:
            print(f"Dashboard update error: {e}")
'''

content = content.replace("    def update_ui(self):", refresh_db_code + "\\n    def update_ui(self):")

with open("fatura_masaustu.py", "w", encoding="utf-8") as f:
    f.write(content)
