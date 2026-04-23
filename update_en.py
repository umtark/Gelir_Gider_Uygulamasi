import json

with open('data/dil/en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)

# Update translating the recently added missing items
translations = {
    'tarih_gecmis': 'Expired!',
    'pdf_kasko_b': 'Casco',
    'gun_kaldi': 'days left',
    'pdf_ruhsat_no': 'License No',
    'genel_bakim_lbl': 'Last Gen. Maint:',
    'yukleniyor': 'Loading...',
    'pdf_trafik_s': 'Traffic Ins.',
    'kayit_duzenle': 'Edit Record',
    'pdf_plaka': 'Plate',
    'pdf_firma_kimlik': 'Company / ID',
    'yaklasti': 'Approaching',
    'dikkat': 'Attention',
    'pdf_sasi_no': 'Chassis No',
    'pdf_muayene_t': 'Inspection D.',
    'pdf_yil_yakit': 'Year / Fuel',
    'tarih_km_ph': 'E.g: 21.04.2026 / 150.000',
    'vergi_tc_lbl': 'ID/Tax No:',
    'pdf_marka_model': 'Brand/Model',
    'pdf_km': 'Mileage',
    'yeni_kayit_ekle': 'Add New Record',
    'pdf_utts': 'UTTS',
    'cok_az_kaldi': 'Very Soon!',
    'yeni_icerik_ekle': '+ Add',
    'yag_bakim_lbl': 'Last Oil Maint:',
    'iyi_durumda': 'Valid',
    'yok_chk': 'None / Unknown'
}

for k, v in translations.items():
    en[k] = v

with open('data/dil/en.json', 'w', encoding='utf-8') as f:
    json.dump(en, f, ensure_ascii=False, indent=4)

print("Updated EN JSON translations!")
