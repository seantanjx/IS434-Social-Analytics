from flask import Flask, jsonify, request
import pymongo
from flask_cors import CORS
from os import environ
from bson.json_util import dumps
from pymongo import MongoClient

import ssl
import datetime 
import calendar 

import json

app = Flask(__name__)
facebookDB = MongoClient("", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

CORS(app)

db_facebook = facebookDB['facebookdata']
post_ffl = db_facebook['freshfruitlab']

phase2 = facebookDB['phase2']
fb_interaction = phase2["fb_interaction"]

@app.route("/fb/dayofpost", methods=['GET'])
def dayofpost():
    dict_day = {"Monday":[0,0], "Tuesday": [0,0], "Wednesday": [0,0], "Thursday":[0,0], "Friday": [0,0], "Saturday": [0,0], "Sunday": [0,0]}
    print(post_ffl)
    for info in post_ffl.find():
        timestamp = str(info["timestamp"])
        date_temp = timestamp.split(" ")[0]
        date_list = date_temp.split("-")
        if len(date_list) > 2:
            date_str = date_list[2] + " " + date_list[1] + " " + date_list[0]
            day = findDay(date_str)
            numLikes = info["likes"]
            templist = dict_day[day]
            templist[0] += 1
            templist[1] += numLikes
            dict_day[day] = templist

    average_dict = {}
    for key, value in dict_day.items():
        if value[0] != 0:
            avg_likes = value[1] / value[0]
            average_dict[key] = avg_likes
        else:
            average_dict[key] = 0
    
    result = {
        "result": average_dict
    }
    #dict [post and likes]

    return jsonify(result),200


#Time of post in general
@app.route("/fb/timeofpost", methods=['GET'])
def timeofpost():
    dict_day = {"06":[0,0], "07": [0,0], "08": [0,0], "09":[0,0], "10": [0,0], "11": [0,0], "12": [0,0], "13":[0,0], "14":[0,0], "15":[0,0], "16":[0,0],
     "17":[0,0], "18":[0,0], "19":[0,0], "20":[0,0], "21":[0,0], "22":[0,0], "23":[0,0],"00":[0,0],"01":[0,0],"02":[0,0], "03":[0,0], "04":[0,0], "05":[0,0]}
    for info in post_ffl.find():
        timestamp = str(info["timestamp"])
        if len(timestamp.split(" ")) > 1:
            date_temp = timestamp.split(" ")[1]
            date_list = date_temp.split(":")
            if len(date_list) > 2:
                time = date_list[0]
                numLikes = info["likes"]
                templist = dict_day[time]
                templist[0] += 1
                templist[1] += numLikes
                dict_day[time] = templist

    average_dict = {}
    for key, value in dict_day.items():
        if value[0] != 0:
            avg_likes = value[1] / value[0]
            average_dict[key] = avg_likes
        else:
            average_dict[key] = 0
    
    result = {
        "result": average_dict
    }

    return jsonify(result),200

#Time of post that is map to the date
@app.route("/fb/postdatetime", methods=['GET'])
def postdatetime():
    dict_daytime = {"Monday":{"06":[0,0], "07": [0,0], "08": [0,0], "09":[0,0], "10": [0,0], "11": [0,0], "12": [0,0], "13":[0,0], "14":[0,0], "15":[0,0], "16":[0,0],
    "17":[0,0], "18":[0,0], "19":[0,0], "20":[0,0], "21":[0,0], "22":[0,0], "23":[0,0],"00":[0,0],"01":[0,0],"02":[0,0], "03":[0,0], "04":[0,0], "05":[0,0]}, "Tuesday": {"06":[0,0], "07": [0,0], "08": [0,0], "09":[0,0], "10": [0,0], "11": [0,0], "12": [0,0], "13":[0,0], "14":[0,0], "15":[0,0], "16":[0,0],
    "17":[0,0], "18":[0,0], "19":[0,0], "20":[0,0], "21":[0,0], "22":[0,0], "23":[0,0],"00":[0,0],"01":[0,0],"02":[0,0], "03":[0,0], "04":[0,0],"05":[0,0]}, "Wednesday": {"06":[0,0], "07": [0,0], "08": [0,0], "09":[0,0], "10": [0,0], "11": [0,0], "12": [0,0], "13":[0,0], "14":[0,0], "15":[0,0], "16":[0,0],
     "17":[0,0], "18":[0,0], "19":[0,0], "20":[0,0], "21":[0,0], "22":[0,0], "23":[0,0],"00":[0,0],"01":[0,0],"02":[0,0], "03":[0,0], "04":[0,0], "05":[0,0]}, "Thursday": {"06":[0,0], "07": [0,0], "08": [0,0], "09":[0,0], "10": [0,0], "11": [0,0], "12": [0,0], "13":[0,0], "14":[0,0], "15":[0,0], "16":[0,0],
     "17":[0,0], "18":[0,0], "19":[0,0], "20":[0,0], "21":[0,0], "22":[0,0], "23":[0,0],"00":[0,0],"01":[0,0],"02":[0,0], "03":[0,0], "04":[0,0], "05":[0,0]}, "Friday": {"06":[0,0], "07": [0,0], "08": [0,0], "09":[0,0], "10": [0,0], "11": [0,0], "12": [0,0], "13":[0,0], "14":[0,0], "15":[0,0], "16":[0,0],
     "17":[0,0], "18":[0,0], "19":[0,0], "20":[0,0], "21":[0,0], "22":[0,0], "23":[0,0],"00":[0,0],"01":[0,0],"02":[0,0], "03":[0,0], "04":[0,0], "05":[0,0]}, "Saturday": {"06":[0,0], "07": [0,0], "08": [0,0], "09":[0,0], "10": [0,0], "11": [0,0], "12": [0,0], "13":[0,0], "14":[0,0], "15":[0,0], "16":[0,0],
     "17":[0,0], "18":[0,0], "19":[0,0], "20":[0,0], "21":[0,0], "22":[0,0], "23":[0,0],"00":[0,0],"01":[0,0],"02":[0,0], "03":[0,0], "04":[0,0], "05":[0,0]}, "Sunday": {"06":[0,0], "07": [0,0], "08": [0,0], "09":[0,0], "10": [0,0], "11": [0,0], "12": [0,0], "13":[0,0], "14":[0,0], "15":[0,0], "16":[0,0],
     "17":[0,0], "18":[0,0], "19":[0,0], "20":[0,0], "21":[0,0], "22":[0,0], "23":[0,0],"00":[0,0],"01":[0,0],"02":[0,0], "03":[0,0], "04":[0,0], "05":[0,0]}}
    for info in post_ffl.find():
        timestamp = str(info["timestamp"])
        #Date
        date_temp = timestamp.split(" ")
        date_list = date_temp[0].split("-")
        if len(date_list) > 2:
            date_str = date_list[2] + " " + date_list[1] + " " + date_list[0]
            day = findDay(date_str)

            #Time 
            date_list = date_temp[1].split(":")
            time = date_list[0]

            temp_dict = dict_daytime[day]
            if type(temp_dict) is not list:
                temp_list = temp_dict[time]
                
                numLikes = info["likes"]

                temp_list[0] += 1
                temp_list[1] += numLikes
                temp_dict[time] = temp_list
                dict_daytime[day] = temp_dict

    average_dict = {}
    print(dict_daytime)
    for key, value in dict_daytime.items():
        print(value)
        for k,v in value.items():
            if v[0] != 0:
                avg_likes = v[1] / v[0]
                new_key = key + "-" + k
                average_dict[new_key] = avg_likes
            else:
                new_key = key + "-" + k
                average_dict[new_key] = 0

    result = {
        "result": average_dict
    }

    return jsonify(result),200

  
def findDay(date): 
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
    return (calendar.day_name[born]) 

@app.route("/fb/interaction_type", methods=['GET'])
def interactionType():
    dict_result = {"competition": [], "featured": [], "product": [], "promotion": [], "infographics": [], "others": []}
    for info in fb_interaction.find():
        interaction_type = info["interaction_type"]
        avg_likes = info["avg_likes"]
        avg_comments = info["avg_comments"]
        current_list = dict_result[interaction_type]
        current_list.append(avg_likes)
        current_list.append(avg_comments)
        dict_result[interaction_type] = current_list
    
    result = {
        "result": dict_result
    }
    return jsonify(result),200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)