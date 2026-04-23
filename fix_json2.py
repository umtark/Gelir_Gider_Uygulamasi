
import json
import os

tr_file = 'data/dil/tr.json'
en_file = 'data/dil/en.json'

if os.path.exists(tr_file):
    with open(tr_file, 'r', encoding='utf-8') as f:
        d = json.load(f)
    d['msg_yeni_yag_bakim'] = 'Araç {} - Yeni yağ bakım kaydı eklendi.'
    d['msg_yeni_servis_bakim'] = 'Araç {} - Yeni bakım/servis kaydı eklendi.'
    d['msg_guncel_yag_bakim'] = 'Araç {} - Yağ bakım kaydı güncellendi.'
    d['msg_guncel_servis_bakim'] = 'Araç {} - Bakım/servis kaydı güncellendi.'
    with open(tr_file, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=4)

if os.path.exists(en_file):
    with open(en_file, 'r', encoding='utf-8') as f:
        d = json.load(f)
    d['msg_yeni_yag_bakim'] = 'Vehicle {} - New oil maintenance record added.'
    d['msg_yeni_servis_bakim'] = 'Vehicle {} - New maintenance/service record added.'
    d['msg_guncel_yag_bakim'] = 'Vehicle {} - Oil maintenance record updated.'
    d['msg_guncel_servis_bakim'] = 'Vehicle {} - Maintenance/service record updated.'
    with open(en_file, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=4)
