import os
import re
import sys
import json
import requests
import pymongo
client = pymongo.MongoClient('localhost', 27017)
db = client['youtube']
collect = db['records']

counter = 0
bulks = []
with open('../../storage/records', 'r') as fp:
    for line in fp:

        line = line.replace('\n', '')

        if line.startswith('@url:'):
            url = line[5:]
        elif line.startswith('@title:'):
            title = line[7:]
        elif line.startswith('@vlen:'):
            vlen = line[6:]
        elif line.startswith('@cview:'):
            cview = line[7:]
            temp = re.findall('\d', cview)
            cview = ''.join(temp)
            try:
                cview = int(cview)
            except:
                cview = 0
        elif line.startswith('@clike:'):
            clike = line[7:]
            temp = clike.replace('千', '000').replace('萬', '0000').replace('億', '00000000')
            temp = re.findall('\d', temp)
            clike = ''.join(temp)
            try:
                clike = int(clike)
            except:
                clike = 0
        elif line.startswith('@chate:'):
            chate = line[7:]
            temp = chate.replace('千', '000').replace('萬', '0000').replace('億', '00000000')
            temp = re.findall('\d', temp)
            chate = ''.join(temp)
            try:
                chate = int(chate)
            except:
                chate = 0
        elif line.startswith('@owner:'):
            owner = line[7:]
        elif line.startswith('@pubtime:'):
            pubtime = line[14:18]
        elif line.startswith('@subscribe:'):
            subscribe = line[11:]
            temp = subscribe.replace('千', '000').replace('萬', '0000').replace('億', '00000000')
            temp = re.findall('\d', temp)
            subscribe = ''.join(temp)
            try : 
                subscribe = int(subscribe)
            except:
                subscribe = 0
            bulk = {
                "id" : counter,
                "url" : url,
                "imageurl" : 'https://img.youtube.com/vi/' + url[32:] + '/hqdefault.jpg',
                "title" : title,
                "vlen" : vlen,
                "cview" : cview,
                "clike" : clike,
                "chate" : chate,
                "owner" : owner,
                "pubtime" : pubtime,
                "subscribe" : subscribe 
            }
            bulks.append(bulk)
            counter += 1

result = collect.insert_many(bulks)
print(result)