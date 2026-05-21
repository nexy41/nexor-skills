#!/usr/bin/env python3
"""Simple manifest generator: parses SKILL.md files (title from first H1) and outputs JSON manifest."""
import json,sys,os,re
skill_dir = os.path.join(os.path.dirname(__file__), '../../marketing')
skill_dir = os.path.abspath(skill_dir)
manifests = []
for root,dirs,files in os.walk(skill_dir):
    if 'SKILL.md' in files:
        p = os.path.join(root,'SKILL.md')
        with open(p,'r',encoding='utf8') as f:
            text=f.read()
        title = re.search(r'^#\s*(.+)$', text, re.M)
        desc = text.split('\n',2)[2] if '\n' in text else ''
        manifests.append({'id': os.path.basename(root), 'path': p, 'title': title.group(1) if title else os.path.basename(root), 'description': desc[:800]})
outdir = os.path.join(os.path.dirname(__file__), 'manifests')
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir,'marketing_manifests.json'),'w',encoding='utf8') as o:
    json.dump(manifests,o,indent=2)
print('Wrote', len(manifests), 'manifests to', os.path.join(outdir,'marketing_manifests.json'))
