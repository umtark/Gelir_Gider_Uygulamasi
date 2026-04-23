import json, os

def add_keys(path, updates):
    if not os.path.exists(path): return
    with open(path, 'r', encoding='utf-8') as f:
        d = json.load(f)
    for k, v in updates.items():
        d[k] = v
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=4)

en_path = os.path.join("data", "dil", "en.json")
tr_path = os.path.join("data", "dil", "tr.json")

add_keys(en_path, {
    "filo_istatistikleri": "Fleet Statistics",
    "firmasi": "Company",
    "arac_adeti": "vehicle(s)",
    "toplam_arac": "Total Vehicles",
    "sistemde_arac_yok": "No registered vehicles in the system",
    "islem_secin": "Select Action",
    "tarih_hdr": "Date",
    "aciklama_hdr": "Description",
    "tutar_hdr": "Amount",
    "iscilik_hdr": "Labor Cost",
    "islemler_hdr": "Actions",
    "tarih_km": "Date & Milage",
    "yag_cinsi": "Oil Type",
    "yag_lt": "Oil Lts",
    "yag_filtre": "Oil Filter",
    "mazot_filtre": "Fuel Filter",
    "hava_filtre": "Air Filter",
    "degisim_usta": "Mechanic",
    "isi_yaptiran": "Assigned By",
    "not_hdr": "Note",
    "tarih_kmsi_lbl": "Date / Milage:",
    "yag_cinsi_lbl": "Oil Type:",
    "yag_lt_lbl": "Oil Lts:",
    "yag_filtresi_lbl": "Oil Filter:",
    "mazot_filtresi_lbl": "Fuel Filter:",
    "hava_filtresi_lbl": "Air Filter:",
    "usta_lbl": "Mechanic:",
    "yaptiran_lbl": "Assigned By:",
    "not_lbl": "Note:",
    "tarih_lbl": "Date:",
    "aciklama_nedegisti_lbl": "Description (What changed?):",
    "malzeme_tutari_tl_lbl": "Material Amount (TL):",
    "iscilik_tl_lbl": "Labor Cost (TL):"
})

add_keys(tr_path, {
    "filo_istatistikleri": "Filo İstatistikleri",
    "firmasi": "Firması",
    "arac_adeti": "araç",
    "toplam_arac": "Toplam Araç",
    "sistemde_arac_yok": "Sistemde Kayıtlı Araç Bulunmamaktadır",
    "islem_secin": "İşlem Seçin",
    "tarih_hdr": "Tarih",
    "aciklama_hdr": "Açıklama",
    "tutar_hdr": "Tutar",
    "iscilik_hdr": "İşçilik",
    "islemler_hdr": "İşlemler",
    "tarih_km": "Değişim Tarihi & KM",
    "yag_cinsi": "Kullanılan Yağ Cinsi",
    "yag_lt": "Yağ LT.",
    "yag_filtre": "Yağ Filtresi",
    "mazot_filtre": "Mazot Filtresi",
    "hava_filtre": "Hava Filt.",
    "degisim_usta": "Değişimi Yapan Usta",
    "isi_yaptiran": "İşi Yaptıran",
    "not_hdr": "Not",
    "tarih_kmsi_lbl": "Değişim Tarihi / KMsi:",
    "yag_cinsi_lbl": "Kullanılan Yağ Cinsi:",
    "yag_lt_lbl": "Yağ LT.:",
    "yag_filtresi_lbl": "Kullanılan Yağ Filtresi:",
    "mazot_filtresi_lbl": "Mazot Filtresi:",
    "hava_filtresi_lbl": "Hava Filtresi:",
    "usta_lbl": "Değişimi Yapan Usta:",
    "yaptiran_lbl": "İşi Yaptıran:",
    "not_lbl": "Not:",
    "tarih_lbl": "Tarih:",
    "aciklama_nedegisti_lbl": "Açıklama (Ne Değişti?):",
    "malzeme_tutari_tl_lbl": "Malzeme Tutarı (TL):",
    "iscilik_tl_lbl": "İşçilik (TL):"
})

print("Done")
