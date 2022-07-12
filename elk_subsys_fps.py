#------------------------------------------------------------------------------------------------------|
#   Date: 01-July-2022 || code is used to send FECB data in ELK stack
#   Author: Bhavesh Kunbi, Telemetry Lab
#   elk_subsys_fecb.py || 01.07.2022 
#   
#   FECB Monittoring Data in ELK || remember to do da_list1 when attributes delete logic active
#------------------------------import libraries--------------------------------------------------------|

# load basic libraries 
from elasticsearch import Elasticsearch # imported elasticsearch libraray and packages
import json 
import requests 
from datetime import datetime
from math import sqrt
from time import sleep
from datetime import date
from flask import Flask, render_template
from tango import DeviceProxy
import csv
import datetime
#device = DeviceProxy("tango://c02:10000/LMC/C02/SERVO")
#da_list = device.get_attribute_list()
#------------------------ Connect to localhost:9200----------------------------------------------------|
try:
    es = Elasticsearch() #connect to our cluster and created elasticsearch instance, Configuration
except Exception as e:
    print("Exception occuered:",e)
#---------------------------- List of Antenna and subsystem -------------------------------------------|
ant = ["c00","c01","c02","c03","c04","c05","c06","c08","c09","c10","c11","c12","c13","c14",
       "s01","s02","s03","s04","s06",
       "e02","e03","e04","e05","e06",
       "w01","w02","w03","w04","w05","w06"] 
#subsys = ["servo","ofcsnt","fps","fecb","sigcon"]

#ant = ["c01","s01","w04"] # for testing only
subsys = ["fps"]
#------------------------------ New index creation loop -----------------------------------------------|
'''
for subsys_index in subsys:
    try:
        response = es.indices.create(index = subsys_index)
        print(response)
    except Exception as e:
        print("index is already exist in kibana")
'''
#--------------------------------- Dictionary created ------------------------------------------------|
dict1 = {}
#---------------------------------- Function to Read all ant attributes ------------------------------|
def attributes():
    #print("****************** Read all attributes print here ********************")
    try:
        device = DeviceProxy(d)
        #now = datetime.now()
        #date = now.strftime("%d/%m/%Y")
        now = datetime.datetime.now()
        da_list = device.get_attribute_list()
        #-----------------------------------------!!
        
        if item2.upper() == "SERVO":
            da_list = device.get_attribute_list()
            da_list1 = da_list
            del da_list1[25:27] # deleted 24 25 26 attribute : responsefield and rmtResponseField
        else:
            da_list = device.get_attribute_list()
            da_list1 = da_list
            del da_list1[18:22] # deleted 24 25 26 attribute : responsefield and rmtResponseField
       
        length = len(da_list1)
        #------------------------------------------!!
    #print("Total attributes in",item2," system is" ,length)
        # new logic added to print only sel;ected attributes.
        for i in range(0,length,1):
            #if i == 0 or i == 1 or i== 16 or i == 21 or i == 35 or i == 40 or i == 41 or i == 48 or i == 49 or i == 71 or i == 72 or i == 50 or i == 51:
                data = device[da_list1[i]]
                keys = [da_list1[i]]
                values = [data.value]
                i=0
                while i < len(keys):
                    try:
                        dict1[keys[i]] = float(values[i])
                    except (ValueError, TypeError):
                        dict1[keys[i]] = values[i]
                    i += 1
                
        dict1["timestamp"] = now
        #print(dict1)
        if (dict1["port"] == 3004.0):
            #print(">>>>> created SERVO subsys index.....")
            print("sending data in ELK, index is [fecb] ........")
            res = es.index(index="gmrtfps", doc_type = "doc", body = dict1 )
        elif (dict1["port"] == 3002.0):
            #print(">>>>> created OFCSNT subsys index.....")
            print("sending data in ELK index is [ofcsnt] ........")
            #res = es.index(index="ofcsnttmp_time1", doc_type = "doc", body = dict1 )
        else:
            print("port value is not available in dict1")
        dict1.clear() # to clear dictionary to avoid overwrite key value data
        
    except Exception as e:
        print("Exception occured:",e)
        #f += 1        
        da_list1 = None
    #print("----------------------------------------------")
        
#-------------------------Number of data/log you want send or print ?-------------------------------------|
for i in range(0,5,1):
    print("#################################### ===>",i)
    for item2 in subsys:
        for item1 in ant:    #tango://c02:10000/LMC/C02/SERVO   
            d = "tango://"+item1+ ":10000/LMC/"+ item1.upper()+"/"+item2.upper()
            print(d)        
            attributes()
        #print("----------- ant all subsys  --------------")
    sleep(10)
print("Sent all data to ELK stack check [ http://192.168.8.197:5601 ] page ...")
#---------------------------------------------------------------------------------------------------------|




