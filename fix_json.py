
import json
import os

tr_file = 'data/dil/tr.json'
en_file = 'data/dil/en.json'

if os.path.exists(tr_file):
    with open(tr_file, 'r', encoding='utf-8') as f:
        d = json.load(f)
    d['etiket_dikkat'] = '[DİKKAT]'
    d['etiket_uyari'] = '[UYARI]'
    d['etiket_bilgi'] = '[BİLGİ]'
    d['ticker_bugun_bitiyor'] = 'SÜRESİ BUGÜN BİTİYOR!'
    with open(tr_file, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=4)

if os.path.exists(en_file):
    with open(en_file, 'r', encoding='utf-8') as f:
        d = json.load(f)
    d['etiket_dikkat'] = '[ATTENTION]'
    d['etiket_uyari'] = '[WARNING]'
    d['etiket_bilgi'] = '[INFO]'
    d['ticker_bugun_bitiyor'] = 'EXPIRES TODAY!'
    with open(en_file, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=4)
