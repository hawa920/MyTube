import os
import re
import sys
import json
import requests
import pymongo
client = pymongo.MongoClient('localhost', 27017)
db = client['youtube']
collect = db['records']
db.records.drop()