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
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import time
es = Elasticsearch('localhost:9200')
print(es)
print("started")
for j in range(0,15):
    doc1 = {
        "inputs":"data" + str(j),
        "timestamp": datetime.now(),
        "outputs": str(j)
            }
    
    es.index(index="elk1", doc_type="doc1", id=j, body=doc1)
    print("sent data to elk == >",j)
    time.sleep(10)
    
print("All data sent ELk")


''' 
#code to send and get data from ELk
#https://jee-appy.blogspot.com/2019/09/python-elasticsearch-example.html
# Import elasticsearch module
from elasticsearch import Elasticsearch 
#import json


# Method to store data in elasticsearch
def send_data_to_es(data):
 es=Elasticsearch(['localhost:9200'])
 res = es.index(index='employee',doc_type='devops',body=data)
 print(res)

# Method to get data from elasticsearch
def get_data_from_es():
 es=Elasticsearch(['localhost:9200'])
 r = es.search(index="employee", body={"query": {"match": {'Name':'john'}}})
 print(r)
 print(type(r))
 print(r["hits"]["hits"][0]["_source"])

# Main function from where the execution starts
if __name__== "__main__":
 # Define a dictoinary having required data to be stored in ES
 data = {"Name": "john", "Age":27, "address": "winterfell"}
 # Call method to store data in ES
 send_data_to_es(data)
 # Call method to get data from ES
 get_data_from_es()
'''
