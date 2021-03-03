from flask import Flask, jsonify, request
import pymongo
from flask_cors import CORS
from os import environ
from bson.json_util import dumps
from pymongo import MongoClient
from datetime import datetime 
from datetime import timedelta  
import ssl

import calendar 

import json

app = Flask(__name__)
instagramDB = MongoClient("", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

CORS(app)

db_insta = instagramDB['instagram']
post_ffl = db_insta['freshfruitlab_postinfo']

db_fb = instagramDB['facebookdata']
post_ffl_fb = db_fb['freshfruitlab']

db_competitor = instagramDB["competitors"]
enchanted_freq = db_competitor["enchantedcafe_ig_postinfo"]
handlerbar_freq = db_competitor["handlebaroriginal_ig_postinfo"]
hatterstreet_freq = db_competitor["hatterstreet_ig_postinfo"]
whiterabbit_freq = db_competitor["thewhiterabbitsg_ig_postinfo"]

#number_of_followers
@app.route("/insta/postdateinformation", methods=['GET'])
def postDate():
    #past 6 months
    list_result = {}
    temp_date = "01/03/2020"
    end_date = "14/10/2020"
    temp_date = datetime.strptime(temp_date, "%d/%m/%Y")
    end_date = datetime.strptime(end_date, "%d/%m/%Y")
    while temp_date.date() < end_date.date():
        list_result[str(temp_date.date())] = 0
        temp_date = temp_date + timedelta(days=1)  

    for info in post_ffl.find():
        timestamp = info["timestamp"]
        date = timestamp.date()
        print(date)
        if str(date) in list_result:
            temp_count = list_result[str(date)]
            list_result[str(date)] = temp_count + 1

    result = {
        "result": list_result
    }

    return jsonify(result),200

@app.route("/fb/postdateinformation", methods=['GET'])
def postDateFb():
    #past 6 months
    list_result = {}
    temp_date = "01/03/2020"
    end_date = "14/10/2020"
    temp_date = datetime.strptime(temp_date, "%d/%m/%Y")
    end_date = datetime.strptime(end_date, "%d/%m/%Y")
    while temp_date.date() < end_date.date():
        list_result[str(temp_date.date())] = 0
        temp_date = temp_date + timedelta(days=1)  

    for info in post_ffl_fb.find():
        timestamp = info["timestamp"]
        if timestamp != None:
            date = timestamp.date()
            print(date)
            if str(date) in list_result:
                temp_count = list_result[str(date)]
                list_result[str(date)] = temp_count + 1

    result = {
        "result": list_result
    }

    return jsonify(result),200

@app.route("/insta/enchanted_freq", methods=['GET'])
def enchantedFreq():
    #past 6 months
    list_result = {}
    temp_date = "14/09/2020"
    end_date = "14/10/2020"
    temp_date = datetime.strptime(temp_date, "%d/%m/%Y")
    end_date = datetime.strptime(end_date, "%d/%m/%Y")
    while temp_date.date() < end_date.date():
        list_result[str(temp_date.date())] = 0
        temp_date = temp_date + timedelta(days=1)  

    for info in enchanted_freq.find():
        timestamp = info["timestamp"]
        print(info)
        date = timestamp.date()
        print(date)
        if str(date) in list_result:
            temp_count = list_result[str(date)]
            list_result[str(date)] = temp_count + 1

    result = {
        "result": list_result
    }

    return jsonify(result),200

@app.route("/insta/handlerbar_freq", methods=['GET'])
def handlerbarFreq():
    #past 6 months
    list_result = {}
    temp_date = "14/09/2020"
    end_date = "14/10/2020"
    temp_date = datetime.strptime(temp_date, "%d/%m/%Y")
    end_date = datetime.strptime(end_date, "%d/%m/%Y")
    while temp_date.date() < end_date.date():
        list_result[str(temp_date.date())] = 0
        temp_date = temp_date + timedelta(days=1)  

    for info in handlerbar_freq.find():
        timestamp = info["timestamp"]
        date = timestamp.date()
        print(date)
        if str(date) in list_result:
            temp_count = list_result[str(date)]
            list_result[str(date)] = temp_count + 1

    result = {
        "result": list_result
    }

    return jsonify(result),200

@app.route("/insta/hatterstreet_freq", methods=['GET'])
def hatterstreetFreq():
    #past 6 months
    list_result = {}
    temp_date = "14/09/2020"
    end_date = "14/10/2020"
    temp_date = datetime.strptime(temp_date, "%d/%m/%Y")
    end_date = datetime.strptime(end_date, "%d/%m/%Y")
    while temp_date.date() < end_date.date():
        list_result[str(temp_date.date())] = 0
        temp_date = temp_date + timedelta(days=1)  

    for info in hatterstreet_freq.find():
        timestamp = info["timestamp"]
        date = timestamp.date()
        print(date)
        if str(date) in list_result:
            temp_count = list_result[str(date)]
            list_result[str(date)] = temp_count + 1

    result = {
        "result": list_result
    }

    return jsonify(result),200

@app.route("/insta/whiterabbit_freq", methods=['GET'])
def whiterabbitFreq():
    #past 6 months
    list_result = {}
    temp_date = "14/09/2020"
    end_date = "14/10/2020"
    temp_date = datetime.strptime(temp_date, "%d/%m/%Y")
    end_date = datetime.strptime(end_date, "%d/%m/%Y")
    while temp_date.date() < end_date.date():
        list_result[str(temp_date.date())] = 0
        temp_date = temp_date + timedelta(days=1)  

    for info in whiterabbit_freq.find():
        timestamp = info["timestamp"]
        date = timestamp.date()
        print(date)
        if str(date) in list_result:
            temp_count = list_result[str(date)]
            list_result[str(date)] = temp_count + 1

    result = {
        "result": list_result
    }

    return jsonify(result),200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009, debug=True)