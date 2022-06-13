#https://github.com/ronidas39/elkpython/blob/main/Tutorial5/tutorial5.py   --> to read file and update ELK

from elasticsearch import Elasticsearch
import json
import time

# set up connection -------------------------
es = Elasticsearch ()
print(es.ping())
# create index ------------------------------
#es.indices.create(index = "a1")
#indices = es.indices.get ("*")
#display all indices -------------------------

#for index in indices:
    #print(index)
# create indices using list ------------------
subsys = ['b1','d1']

for new_index in subsys:
    try:
        response = es.indices.create(index = new_index)
        print(response)
    except Exception as e:
        print("index is already exist") 
