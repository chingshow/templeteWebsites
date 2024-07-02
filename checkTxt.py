# -*- coding: utf-8 -*-
import os
import json
import generateHtml

with open('try.json', 'r', encoding="utf-8") as fJson:
    load_dict = json.load(fJson)

documents = load_dict['documents']['items']
folder_path = './documents/txt/'

documentLocal = []
for file in os.listdir(folder_path):
    if file.endswith('.txt'):
        documentLocal.append(file)
        #print(file)

exist = 0
for document in documentLocal:
    #print(document)
    exist = 0
    for item in documents:
        if item['no'] + ".txt" == document:
            exist = 1
            break
    if exist == 0:
        print(document)
        # 發現不存在這個文章 --> 開始產生html
        generateHtml.main(document)

# --- sort json --- #

with open('try.json', 'r', encoding="utf-8") as fJson:
    load_dict = json.load(fJson)

    documents = load_dict['documents']['items']
    for i in range(0, len(documents)):
        for j in range(i+1, len(documents)):
            if documents[i]['no'] > documents[j]['no']:
                temp = documents[i]
                documents[i] = documents[j]
                documents[j] = temp

with open('try.json', 'w', encoding="utf-8") as fJson:
    json.dump(load_dict, fJson, ensure_ascii=False, indent=4)