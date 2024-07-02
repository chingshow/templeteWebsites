# -*- coding: utf-8 -*-
import os
from dominate.tags import *
import dominate
import json

def main(inputFile):
    # --------generate html from txt----------------#
    # html init
    newHtml = dominate.document()
    newHtml.add(link(rel="stylesheet", href="./styles.css"))
    newHtml.add(meta(charset="utf-8"))
    title = newHtml.add(div(id="title", className="container"))
    content = newHtml.add(div(id="content", className="container"))

    path = os.path.join('./documents/txt/', inputFile)
    print(path)
    # read txt
    f = open(path, encoding="utf-8")
    length = 0
    for line in f.readlines():
        if line[0] != ' ' and line[0] != '\n':
            if length == 0:
                num = line
                no = []
                for char in num:
                    if char != '\n':
                        no.append(char)
                no = ''.join(str(x) for x in no)
            elif length == 1:
                title.add(p(line, id="date"))
            elif length == 2:
                title_name = []
                for char in line:
                    if char != '\n':
                        title_name.append(char)
                title_name = ''.join(str(x) for x in title_name)
                title.add(h1(title_name, id="title_name"))
            elif length == 3:
                auther = []
                for char in line:
                    if char != '\n':
                        auther.append(char)
                auther = ''.join(str(x) for x in auther)
                title.add(h2(auther, id="auther"))
            else:
                content.add(p(line))
            length += 1
    f.close()

    # document name
    path = './documents/' + no + '.html'

    with open(path, 'w', encoding="utf-8") as f:
        f.write(newHtml.render())

    # --------finish generate html from txt----------------#

    # edit json

    with open('try.json', 'r', encoding="utf-8") as fJson:
        load_dict = json.load(fJson)

        documents = load_dict['documents']['items']
        newDocument = {}
        newDocument['titles'] = title_name
        newDocument['author'] = auther
        newDocument['no'] = no
        documents.append(newDocument)
    with open('try.json', 'w', encoding="utf-8") as fJson:
        json.dump(load_dict, fJson, ensure_ascii=False, indent=4)