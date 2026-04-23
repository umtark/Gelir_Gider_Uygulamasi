import re

with open('fatura_masaustu.py', encoding='utf-8') as f:
    text = f.read()

def find_matches(pattern):
    matches = re.findall(pattern, text)
    return [m[0] or m[1] for m in matches if any(m)]

print("Labels:", find_matches(r'QLabel\(\s*\'(.*?)\'\s*\)|QLabel\(\s*\"(.*?)\"\s*\)'))
print("Buttons:", find_matches(r'QPushButton\(\s*\'(.*?)\'\s*\)|QPushButton\(\s*\"(.*?)\"\s*\)'))
print("Groupboxes:", find_matches(r'QGroupBox\(\s*\'(.*?)\'\s*\)|QGroupBox\(\s*\"(.*?)\"\s*\)'))

# Tabs
tabs = re.findall(r'addTab\(.*?(?:\"|\')(.*?)(?:\"|\')\)', text)
print("Tabs:", tabs)
