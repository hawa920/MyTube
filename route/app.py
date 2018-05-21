import os
import re
import json
import random
import string
import youtube_dl
from flask_cors import CORS, cross_origin
from flask import Flask, request, send_from_directory, send_file, make_response, render_template
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import pymongo

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/", methods = ['GET', 'POST'])
@cross_origin()
def index():
  if request.method == 'POST':
    return 'Bad Request.'
  return render_template('index.html')


@app.route("/mp3-dl", methods = ['POST'])
@cross_origin()
def downloader():

  url = json.dumps(request.form.get('link'))
  url = str(url[1:len(str(url))-1])
  outfile = '../storage/' + ''.join(random.choice(string.ascii_letters+string.digits) for i in range(30)) + '.mp3'
  options = {

    'format': 'bestaudio/best',
    'postprocessors': [{
      'key': 'FFmpegExtractAudio',
      'preferredcodec': 'mp3',
    }],
    'noplaylist': True,
    'outtmpl': outfile
  }

  # Download with youtube-dl
  with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([url])
  response = make_response(send_file(outfile))
  # Http header
  response.headers['Content-Disposition'] = "attachment; filename=" + outfile[12:]
  return response
#return send_file(outfile)


@app.route("/search", methods = ['GET'])
@cross_origin()
def search():
  query = request.args.get('query')
  if query is None:
    return 'None Query.'

  # test if it's a special request
  temp = re.findall('\d+:\d+:\w+:\d+', query)
  if len(temp) is 1:
    temp = temp[0].split(':')
    ylb = temp[0]
    yrb = temp[1]
    opt = temp[2]
    num = temp[3]

    client = pymongo.MongoClient('localhost', 27017)
    db = client['youtube']
    collect = db['records']

    if opt == 'rand':
      temp = collect.aggregate([{ "$sample" : {"size" : int(num)}}])
      ret = []
      for rec in temp:
        # remove 'key:id'
        rec.pop('_id', None)
        # print(rec, '\n')
        ret.append(rec)
      return json.dumps(ret)



    temp = collect.find({

            "$and" : [
                {"pubtime" : {"$lte":yrb}},
                {"pubtime" : {"$gte":ylb}}
            ]
          }
    ).sort(opt, pymongo.DESCENDING).limit(int(num))
    ret = []

    for rec in temp:
      # remove 'key:id'
      rec.pop('_id', None)
      # print(rec, '\n')
      ret.append(rec)
    return json.dumps(ret)

  else:
    body = {
      "query": {
          "match": {
              "title" : query
          }
      }
    }
    es = Elasticsearch()
    temp = es.search(index = 'youtube', doc_type = 'records', size = 10, body = body)
    temp = temp['hits']['hits']
    res = []
    for rec in temp:
      res.append(rec['_source'])
    return json.dumps(res)


@app.route('/<path:dummy>', methods = ['GET', 'POST'])
@cross_origin()
def fallback(dummy):
  return '<h1>Bro, don\'t do this...</h1>'


if __name__ == "__main__":
  #app.run(port=5000, debug=True)
  # Comment the line above and use the line below if you launch on your own server
  app.run(host='0.0.0.0', port=5003, debug = True)
