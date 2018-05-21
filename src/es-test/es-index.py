from elasticsearch import Elasticsearch

def DeleteIndex(INDEX_NAME):
    es = Elasticsearch()
    if es.indices.exists(INDEX_NAME):
        print("deleting '%s' index..." % (INDEX_NAME))
        res = es.indices.delete(index = INDEX_NAME)
        print(" response: '%s'" % (res))
    else:
        print('Index doesn\'t exsit.')


def CreateIndex(INDEX_NAME):
    es = Elasticsearch()

    request_body = {
        "mappings": {
            "records": {
                "properties": {
                    "url": {
                        "type": "text"
                    },
                    "imgurl" : {
                        "type": "text"
                    },
                    "title": {
                        "type": "text",
                    },
                    "pubtime" : {
                        "type" : "text"
                    },
                    "owner" : {
                        "type" : "text"
                    },                    
                    "vlen" : {
                        "type" : "text"
                    },
                    "cview" : {
                        "type" : "long"
                    },
                     "clike" : {
                        "type" : "integer"
                    },
                    "chate" : {
                        "type" : "integer"
                    },
                    "subscribe" : {
                        "type" : "integer"
                    }
                }
            }
        }
    }
    print("creating '%s' index..." % (INDEX_NAME))
    res = es.indices.create(index = INDEX_NAME, body = request_body)
    print(" response: '%s'" % (res))


if __name__ == "__main__":
    DeleteIndex('youtube')
    CreateIndex('youtube')