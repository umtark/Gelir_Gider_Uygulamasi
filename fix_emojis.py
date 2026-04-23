
import sys

with open('fatura_masaustu.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('🚨', '[!]')
text = text.replace('⏳', '')
text = text.replace('⚠️', '[UYARI]')
text = text.replace('⏰', '')
text = text.replace('🔔', '[BLG]')
text = text.replace('🛠️', '>>')
text = text.replace('✨✨✨', '|')
text = text.replace('🚀', '[SSTEM]')
text = text.replace('✅🎉', '')
text = text.replace('💬', '')

with open('fatura_masaustu.py', 'w', encoding='utf-8') as f:
    f.write(text)
