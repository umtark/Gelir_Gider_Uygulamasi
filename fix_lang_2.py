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
    "belirtilmemis": "Unspecified"
})

add_keys(tr_path, {
    "belirtilmemis": "Belirtilmemiş"
})

print("Done part 2")