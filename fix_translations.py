import json

def update_lang(file, d_entries):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print("error", e)
        data = {}
    
    for k, v in d_entries.items():
        data[k] = v
        
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

en = {
    "sofor_lbl": "Driver:",
    "sofor_tel_lbl": "Driver Phone:",
    "firma_sahibi_lbl": "Company/Owner:",
    "firma_lbl": "Company:",
    "ticker_sure_gecti": "IS EXPIRED!",
    "ticker_bugun_bitiyor": "EXPIRES TODAY!",
    "ticker_sadece": "only",
    "ticker_gun_kaldi": "days left",
    "ticker_bitisine": "Expires in",
    "ticker_tum_guncel": "All ({}) vehicles documentation and dates are up to date.",
    "ticker_bekleniyor": "Checking all system records... Please wait.",
    "muayene_kisa": "Inspection",
    "trafik_kisa": "Traffic Ins.",
    "kasko_kisa": "Casco",
    "koltuk_kisa": "Seat Ins.",
    "bilinmiyor": "UNKNOWN",
    "pdf_sofor_bilgisi": "Driver Info"
}

tr = {
    "sofor_lbl": "Araç Şoförü:",
    "sofor_tel_lbl": "Şoför Tel:",
    "firma_sahibi_lbl": "Firma/Sahibi:",
    "firma_lbl": "Firma/Sahibi:",
    "ticker_sure_gecti": "SÜRESİ GEÇTİ!",
    "ticker_bugun_bitiyor": "SÜRESİ BUGÜN BİTİYOR!",
    "ticker_sadece": "bitişine sadece",
    "ticker_gun_kaldi": "gün kaldı",
    "ticker_bitisine": "Bitişine",
    "ticker_tum_guncel": "Sistemdeki tüm ({}) araçların belgeleri ve tarihleri güncel durumda.",
    "ticker_bekleniyor": "Tüm sistem kayıtları kontrol ediliyor... Lütfen bekleyiniz.",
    "muayene_kisa": "Muayene",
    "trafik_kisa": "Trafik S.",
    "kasko_kisa": "Kasko",
    "koltuk_kisa": "Koltuk S.",
    "bilinmiyor": "BİLİNMİYOR",
    "pdf_sofor_bilgisi": "Şoför Bilgisi"
}

update_lang('data/dil/en.json', en)
update_lang('data/dil/tr.json', tr)
print("done")
