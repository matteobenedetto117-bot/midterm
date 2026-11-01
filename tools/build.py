"""Ricostruisce index.html da tools/template.html + dati/*.json.
Uso (dalla radice del repository): python3 tools/build.py"""
import json, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = lambda *a: os.path.join(R, *a)
t = open(p('tools', 'template.html'), encoding='utf-8').read()
j = lambda f: json.dumps(json.load(open(p('dati', f), encoding='utf-8')), ensure_ascii=False)
html = (t.replace('__GEO__', open(p('tools', 'geo.json')).read())
         .replace('__HDATA__', j('camera_data.json'))
         .replace('__GDATA__', j('gov_data.json'))
         .replace('__DATA__', j('senato_data.json')))
open(p('index.html'), 'w', encoding='utf-8').write(html)
print('index.html aggiornato')
