#!/usr/bin/env python3
"""NexMa Telegram adapter (read-only skeleton).
Usage: set TELEGRAM_BOT_TOKEN and run. Exposes /marketing <skill_id> to show skill summary.
"""
import os,json
MANIFEST=os.path.join(os.path.dirname(__file__),'manifests','marketing_manifests.json')
if not os.path.exists(MANIFEST):
    print('Manifest missing; run manifest_generator.py first')
    exit(1)
man = json.load(open(MANIFEST))
# Minimal local test interface
print('NexMa adapter loaded with', len(man), 'skills')
print('Sample skill IDs:', [m['id'] for m in man][:10])
