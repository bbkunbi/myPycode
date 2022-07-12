
##################################################################################

# Name: 
# Description: Script is used to send servo real time attribute on web page 
# Link: http://192.168.8.225:5000/gmrt   ==> 
# Version: 01
# Author: bhavesh kunbi (Telemetry Lab, 8330 , GMRT-NCRA-TIFR)
# Last Modified date: 08.07.2022 , to add hardware details in elk v1.0
##################################################################################
from flask import Flask,render_template, request,json
from flask import Flask, jsonify, render_template, request
import webbrowser
import time
import json
import tango
from tango import DeviceProxy
import csv
from flask import Flask, render_template, request, jsonify
from flask import Flask,render_template,request
from flask import Flask, redirect, url_for, render_template, request
import datetime
import pandas as pd
from datetime import datetime
from datetime import datetime
from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch
'''
app = Flask(__name__, template_folder='template')
@app.route("/servo")
def index():
    return render_template("index19_1.html")  
@app.route('/gmrtservo', methods=["GET"])
def gmrtservo():
    return render_template("servowebpage2.html",dict1=dict1) # web page template designed
if __name__ == '__main__':
    app.run()
    #app.run(host='192.168.8.233', port=5000, debug=True)
'''
es = Elasticsearch()

app = Flask(__name__, template_folder='template')

@app.route('/') # it is used to send data in ELk
def index():
    #results = es.get(index='contents', doc_type='title', id='my-new-slug')
    #return "Welcome to ELK with FLASK to store GMRT hardware deatils in [ + Elasticsearch + ]."
    #return render_template("elk_v1.html")
    return render_template("index871.html") 

#@app.route('/insert_data', methods=['POST'])
#def insert_data():
'''
@app.route('/get_data', methods=['GET'])
def get_data():
    results = es.get(index='tgc_hardware', doc_type='title', body = tgc)
    #print(results)
    #somedata = "tgc"
    return render_template("index872.html",results=results)
'''
@app.route('/ant') # it send to get_data loop   it is used to read data
def ant():
    #results = es.get(index='contents', doc_type='title', id='my-new-slug')
    #return "Welcome to ELK with FLASK to store GMRT hardware deatils in [ + Elasticsearch + ]."
    #return render_template("elk_v1.html")
    return render_template("index873.html")

@app.route('/insert_data', methods=["POST"]) # '/'send to this page
def insert_data():
    # http://localhost:5000/users?name=lenin&surname=falconi
    ant = request.form.get('ant')
    usb_id = request.form.get('usb_id')
    lmc = request.form.get('lmc')

    tgc = {
            'antenna name' : ant,
            'usb cable id': usb_id,
            'LMC machine number': lmc
          }
    #return 'This is {} {}'.format(name, surname)
    result = es.index(index='tgc_hardware', doc_type='title', id=ant, body=tgc)
    return render_template("elk_result.html",usb_id=usb_id,lmc=lmc,ant=ant)
    #return jsonify(result)

@app.route('/get_data', methods=["GET"]) # '/ant sent to this page'
def get_data():
    #ant = 'w01'
    ant = request.args.get('ant')
    print(ant)
    #for ant in tgc_hardware:
    tgc = es.get(index='tgc_hardware', doc_type='title',id = ant)
    return render_template("get.html", tgc=tgc )

#app.run(port=5000, debug=True)
if __name__=="__main__":
    app.run()
    #get_data_from_es()
