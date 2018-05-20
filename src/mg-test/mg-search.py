import os
import re
import sys
import json
import requests
import pymongo
client = pymongo.MongoClient('localhost', 27017)
db = client['youtube']
collect = db['records']

ans = collect.find({

        "$and" : [
            {"pubtime" : {"$lte":"2018"}},
            {"pubtime" : {"$gte":"2015"}}
        ]
    }
).sort("cview", pymongo.DESCENDING).limit(10)
# ASCENDING
for rec in ans:
    print(rec, '\n')