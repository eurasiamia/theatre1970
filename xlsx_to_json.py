"""
small_theatre_semanticdate_2026_v3.xlsx → network_nodes.json / network_links.json 변환 스크립트
사용법: python xlsx_to_json.py
"""
import json
import pandas as pd

XLSX = 'small_theatre_semanticdate_2026_v3.xlsx'
NODES_OUT = 'network_nodes.json'
LINKS_OUT = 'network_links.json'

def to_str(v):
    if pd.isna(v):
        return None
    v = str(v).strip()
    return v if v else None

xl = pd.read_excel(XLSX, sheet_name=None)

# ── NODES ──
df_nodes = xl['nodes']
nodes = []
for _, r in df_nodes.iterrows():
    node = {
        'id':      to_str(r.get('dcterms:identifier')),
        'title':   to_str(r.get('title(한국)')),
        'class':   to_str(r.get('class')),
        'subclass': to_str(r.get('sub class')),
        'address': to_str(r.get('adress')),
        'url':     to_str(r.get('URL')),
        'sameAs':  to_str(r.get('SameAs')),
    }
    if node['id']:
        nodes.append(node)

# ── LINKS ──
df_links = xl['links']
links = []
for _, r in df_links.iterrows():
    link = {
        'source':   to_str(r.get('ID(subject)')),
        'target':   to_str(r.get('IDObject)')),
        'relation': to_str(r.get('relation(한)')),
        'page':     to_str(r.get('채록번 면번호')),
        'series':   to_str(r.get('채록번 시리즈번호')),
    }
    if link['source'] and link['target']:
        links.append(link)

with open(NODES_OUT, 'w', encoding='utf-8') as f:
    json.dump(nodes, f, ensure_ascii=False, indent=2)

with open(LINKS_OUT, 'w', encoding='utf-8') as f:
    json.dump(links, f, ensure_ascii=False, indent=2)

print(f'노드 {len(nodes)}개 → {NODES_OUT}')
print(f'링크 {len(links)}개 → {LINKS_OUT}')
