# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 18:26:35 2020

@author: User
"""
import requests
import sys
import json

def get_id(name):
    S = requests.Session()
    URL = "https://zh.wikipedia.org/w/api.php"
    PARAMS = {
        "action": "query",
        "titles": name,
        "prop": "pageprops",
        "format": "json"
        }
    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    #rint(DATA["query"])
    pages = DATA["query"]["pages"]
    for k in pages.keys():
        info = pages[k]
        if len(info) <= 3:
            print("get id failed")
            sys.exit(0)
        wiki_id = info["pageprops"]["wikibase_item"]
    print(wiki_id)


if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        print("input error!")
        print("demo:")
        print("python getid 高永文")
        sys.exit(0)
        
    get_id(sys.argv[1])