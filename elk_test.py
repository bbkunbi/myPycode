from elasticsearch import Elasticsearch
import utils
import pandas as pd
from elasticsearch import helpers
'''
def get_connection():
    con=Elasticsearch(HOST="localhost",PORT=9200)
    print(con)
    return con

print("function called")
def get_all_indexes():
    es = utils.get_connection()
    try:
        res=es.indices.get_alias("*")
        for i in res:
            print(i)
        print(res)
    except Exception as e:
        print(e)
        
get_connection()        
get_all_indexes()
print("all index fetched")
'''

con=Elasticsearch(HOST="localhost",PORT=9200)
print(con)

#print("function called")
es = Elasticsearch()
#es = utils()
print(es)
try:
    res=es.indices.get_alias("*")
    for i in res:
        print("index is ==> ",i)
    print(res)
except Exception as e:
    print(e)
        
try:
    response = es.get(index="tgc_hardware", doc_type="title",id = "ant")  # It returnsjson response {'_index': 'student', '_type': 'information', '_id': '1', '_version': 3, '_seq_no': 2, '_primary_term': 1, 'found': True, '_source': {'name': 'Utkars', 'email': 'AAAutkarsh@gmail.com', 'age': '22'}}
    print(response)
except Exception as e:
    print(e)
