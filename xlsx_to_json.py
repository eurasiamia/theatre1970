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

# ── NODES (컬럼 인덱스 기준) ──
# 0:class, 1:sub class, 2:dcterms:identifier, 3:title(한글), 4:title(영문),
# 5:start_date, 6:end_date, 7:유형, 8:genreValue, 9:URL, 10:SameAs, 11:adress, 12:bibo Info
df_nodes = xl['nodes']
nodes = []
for _, r in df_nodes.iterrows():
    node = {
        'id':       to_str(r.iloc[2]),
        'title':    to_str(r.iloc[3]),
        'class':    to_str(r.iloc[0]),
        'subclass': to_str(r.iloc[1]),
        'address':  to_str(r.iloc[11]),
        'url':      to_str(r.iloc[9]),
        'sameAs':   to_str(r.iloc[10]),
    }
    if node['id']:
        nodes.append(node)

# ── LINKS (컬럼 인덱스 기준) ──
# 0:class(subject), 1:ID(subject), 2:class(Object), 3:IDObject),
# 4:relation(한), 5:relation(영), 6:채록문 페이지, 7:채록문 시리즈번호
df_links = xl['links']
links = []
for _, r in df_links.iterrows():
    link = {
        'source':   to_str(r.iloc[1]),
        'target':   to_str(r.iloc[3]),
        'relation': to_str(r.iloc[4]),
        'page':     to_str(r.iloc[6]),
        'series':   to_str(r.iloc[7]),
    }
    if link['source'] and link['target']:
        links.append(link)

# foaf:Person ↔ Performance 관계에서 채록문 정보 제거
node_info = {n['id']: n for n in nodes}
for l in links:
    src_n = node_info.get(l['source'], {})
    tgt_n = node_info.get(l['target'], {})
    is_person = lambda n: n.get('subclass') == 'foaf:Person'
    is_perf   = lambda n: (n.get('class') or '').lower() == 'performance'
    if (is_person(src_n) and is_perf(tgt_n)) or (is_person(tgt_n) and is_perf(src_n)):
        l['page'] = None
        l['series'] = None

with open(NODES_OUT, 'w', encoding='utf-8') as f:
    json.dump(nodes, f, ensure_ascii=False, indent=2)

with open(LINKS_OUT, 'w', encoding='utf-8') as f:
    json.dump(links, f, ensure_ascii=False, indent=2)

print(f'노드 {len(nodes)}개 → {NODES_OUT}')
print(f'링크 {len(links)}개 → {LINKS_OUT}')
