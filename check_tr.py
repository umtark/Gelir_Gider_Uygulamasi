import re
import json

with open('fatura_masaustu.py', 'r', encoding='utf-8') as f:
    text = f.read()

# find all keys used in _t()
matches = re.findall(r'_t\([\'\"](.*?)[\'\"]\s*,\s*[\'\"](.*?)[\'\"]', text)
keys = {m[0]: m[1] for m in matches}

with open('data/dil/tr.json', 'r', encoding='utf-8') as f:
    tr = json.load(f)

with open('data/dil/en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)

missing_tr = set(keys.keys()) - set(tr.keys())
missing_en = set(keys.keys()) - set(en.keys())

print('Missing TR:')
for k in missing_tr:
    print(f"  {k}: {keys[k]}")

print('Missing EN:')
for k in missing_en:
    print(f"  {k}: {keys[k]}")

# Update tr.json
for k in missing_tr:
    tr[k] = keys[k]
with open('data/dil/tr.json', 'w', encoding='utf-8') as f:
    json.dump(tr, f, ensure_ascii=False, indent=4)

# Update en.json
for k in missing_en:
    en[k] = keys[k]
with open('data/dil/en.json', 'w', encoding='utf-8') as f:
    json.dump(en, f, ensure_ascii=False, indent=4)

print("Updated both json files with the missing keys.")
