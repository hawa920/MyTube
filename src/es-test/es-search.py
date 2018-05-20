import os
import re
import sys
import json
import pprint
import requests
from elasticsearch import Elasticsearch
from elasticsearch import helpers
body = {
    "query": {
        "match": { 
            "title" : "justin"
        }
    }
}
es = Elasticsearch()
res = es.search(index = 'youtube', doc_type = 'records', size = 10, body = body)

#print(" response: '%s'" % (res))
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(res)