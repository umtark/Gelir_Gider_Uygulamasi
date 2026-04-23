import json

tr_path = "data/dil/tr.json"
en_path = "data/dil/en.json"

tr_keys = {
    "arac_evrak_yükle_btn": "Araç Evrakları Yükle / İncele",
    "sofor_evrak_yükle_btn": "Şoför Evrakları Yükle / İncele",
    "sofor_yok_uyari": "Bu araca kayıtlı bir şoför bulunmuyor. Önce araca bir şoför atayın.",
    "kayitli_evraklar_baslik": "Kayıtlı Evraklar:",
    "hic_evrak_yok_uyari": "Kayıtlı hiçbir evrak bulunmuyor.",
    "arac_evrak_text": "Araç",
    "sofor_evrak_text": "Şoför",
    "sofor_evraklari": "Şoför Evrakları",
    "qlabel_sofore_ait_eklenen": "Şoföre ait eklenen dosyalar (Ehliyet, SRC, Psikoteknik vs.)"
}

en_keys = {
    "arac_evrak_yükle_btn": "Load / Inspect Vehicle Documents",
    "sofor_evrak_yükle_btn": "Load / Inspect Driver Documents",
    "sofor_yok_uyari": "There is no driver registered to this vehicle. Assign a driver first.",
    "kayitli_evraklar_baslik": "Registered Documents:",
    "hic_evrak_yok_uyari": "No registered documents found.",
    "arac_evrak_text": "Vehicle",
    "sofor_evrak_text": "Driver",
    "sofor_evraklari": "Driver Documents",
    "qlabel_sofore_ait_eklenen": "Files added for the driver (License, SRC, Psychotechnical etc.)"
}

for path, new_keys in [(tr_path, tr_keys), (en_path, en_keys)]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        data.update(new_keys)
        
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Updated {path}")
    except Exception as e:
        print(f"Error updating {path}: {e}")
