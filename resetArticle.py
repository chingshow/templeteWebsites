# -*- coding: utf-8 -*-
import os
import json
import generateHtml
import glob


with open('content_try.json', 'r', encoding="utf-8") as fJson:
    load_dict = json.load(fJson)

load_dict['documents']['items'] = []

with open('content_try.json', 'w', encoding="utf-8") as fJson:
    json.dump(load_dict, fJson, ensure_ascii=False, indent=4)

all_text = glob.glob('documents/*.html')
for t in all_text:
    os.remove(t)

all_text = glob.glob('documents/txt/*.txt')
for t in all_text:
    os.remove(t)

all_text = glob.glob('documents/txt/*.md')
for t in all_text:
    os.remove(t)

