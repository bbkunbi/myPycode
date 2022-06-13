from elasticsearch import Elasticsearch
import json
from bs4 import BeautifulSoup 
import requests 
from datetime import datetime
from math import sqrt
from time import sleep
from datetime import date
from flask import Flask, render_template
from tango import DeviceProxy
import csv
from flask import Flask, render_template, request, jsonify
import datetime

device = DeviceProxy("tango://c02:10000/LMC/C02/SERVO")
da_list = device.get_attribute_list()
'''
es = Elasticsearch()

doc = {
    'author': 'author_name',
    'text': 'Interesting content...',
    'timestamp': datetime.now(),
}
res = es.index(index="test-index", id=1, body=doc)
print(res['result'])
'''
es = Elasticsearch()
dict1 = {}


for j in range (0,10,1):
    print("---------------------------|", j ,"|--------------------------------")
    #time.sleep(3)
    for i in range(70,76,1):
           now = datetime.datetime.now()
           #print("-------",i)
           data = device[da_list[i]]
           key = [da_list[i]]
           #print(da_list[i])
           value = [data.value]
           #d = dict(zip(k,v))
           i=0
           while i < len(key):
                     dict1[key[i]] = value[i]
                     i += 1
    #print(dict1)
    dict1['timestamp'] = now
    print(dict1)
    #print("--------------------")
    #json1 = json.dumps(dict1) #use the json library to convert dict object to a JSON string
    #print(json1)
    #print("--------------------")
    #res = es.index(index="c02-index",doc_type="doc",id = j, body=dict1 )
    #res = es.index(index="c02-index",doc_type="doc", body=dict1 )
    res = es.index(index="c02-index-json1",doc_type="doc", body=dict1 )
    sleep(10)
print(res['result'])
print(" task finished")
























'''
es = Elasticsearch(
    'localhost:9200'
)


def send_json_to_elk(file_name, index_name):
    """
    file got to be in ndjson format
    """
    try:
        with open(file_name) as fp:
            for line in fp:
                line = line.replace("\n", "")
                jdoc = {"data": json.loads(line)}
                es.index(index=index_name, doc_type='_doc', body=jdoc)

        print("finished upload: " + index_name)
    except Exception as e:
        print(e)


send_json_to_elk("test.json", "test_vid")
'''
