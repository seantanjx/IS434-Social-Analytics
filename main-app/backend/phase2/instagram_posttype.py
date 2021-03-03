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
instagramDB = MongoClient("", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

CORS(app)

db_insta = instagramDB['instagram']
post_ffl = db_insta['freshfruitlab_postinfo']

phase2 = instagramDB['phase2']
ig_interaction = phase2["ig_interaction"]
fb_interaction = phase2["fb_interaction"]

#number_of_followers
@app.route("/insta/posttype", methods=['GET'])
def posttype():
    count_image = 0
    count_sidecar = 0
    count_video = 0
    image_likes = 0
    sidecar_likes = 0
    video_likes = 0
    image_comments = 0
    sidecar_comments = 0
    video_comments = 0
    for info in post_ffl.find():
        post_info = info["post_type"]
        if post_info == "GraphImage":
            count_image += 1
            image_likes += info["number_of_likes"]
            image_comments += info["number_of_comments"]
        elif post_info == "GraphSidecar":
            count_sidecar += 1
            sidecar_likes += info["number_of_likes"]
            sidecar_comments += info["number_of_comments"]
        elif post_info == "GraphVideo":
            count_video += 1
            video_likes += info["number_of_likes"]
            video_comments += info["number_of_comments"]

    #manipulate the average engagement 
    avg_likes_image = image_likes/count_image
    avg_comments_image = image_comments/count_image

    avg_likes_sidecar = sidecar_likes/count_sidecar
    avg_comments_sidecar = sidecar_comments/count_sidecar

    avg_likes_video = video_likes/count_video
    avg_comments_video = video_comments/count_video

    result = {
        "GraphImage": {
            "likes":avg_likes_image,
            "comments":avg_comments_image
        },
        "GraphSidecar": {
            "likes":avg_likes_sidecar,
            "comments":avg_comments_sidecar
        },
        "GraphVideo": {
            "likes":avg_likes_video,
            "comments":avg_comments_video
        },
    }
    return jsonify(result),200

@app.route("/insta/posttypecount", methods=['GET'])
def posttypecount():
    count_image = 0
    count_sidecar = 0
    count_video = 0
    for info in post_ffl.find():
        post_info = info["post_type"]
        if post_info == "GraphImage":
            count_image += 1
        elif post_info == "GraphSidecar":
            count_sidecar += 1

        elif post_info == "GraphVideo":
            count_video += 1

    result = {
        "GraphImage": count_image,
        "GraphSidecar": count_sidecar,
        "GraphVideo": count_video,
    }
    return jsonify(result),200

## Do one to see video duration will affect the number of views

@app.route("/insta/videoduration", methods=['GET'])
def videoduration():
    #y-axis = likes
    #x-axix = length of video
    temp_id = 0
    dict_result = {}
    for info in post_ffl.find():
        post_info = info["post_type"]
        if post_info == "GraphVideo":
            temp_id += 1
            video_views = info["video_views"]
            video_duration = info["video_duration"]
            dict_result[temp_id] = [video_views, video_duration]
    
    result = {
        "result": dict_result
    }

    return jsonify(result),200

@app.route("/insta/dayofpost", methods=['GET'])
def dayofpost():
    dict_day = {"Monday":[0,0], "Tuesday": [0,0], "Wednesday": [0,0], "Thursday":[0,0], "Friday": [0,0], "Saturday": [0,0], "Sunday": [0,0]}
    print(dict_day)
    for info in post_ffl.find():
        timestamp = str(info["timestamp"])
        date_temp = timestamp.split(" ")[0]
        print(date_temp)
        date_list = date_temp.split("-")
        date_str = date_list[2] + " " + date_list[1] + " " + date_list[0]
        day = findDay(date_str)
        numLikes = info["number_of_likes"]
        templist = dict_day[day]
        templist[0] += 1
        templist[1] += numLikes
        dict_day[day] = templist

    average_dict = {}
    for key, value in dict_day.items():
        avg_likes = value[1] / value[0]
        average_dict[key] = avg_likes
    
    result = {
        "result": average_dict
    }
    #dict [post and likes]

    return jsonify(result),200


#Time of post in general
@app.route("/insta/timeofpost", methods=['GET'])
def timeofpost():
    dict_day = {"06":[0,0], "07": [0,0], "08": [0,0], "09":[0,0], "10": [0,0], "11": [0,0], "12": [0,0], "13":[0,0], "14":[0,0], "15":[0,0], "16":[0,0],
     "17":[0,0], "18":[0,0], "19":[0,0], "20":[0,0], "21":[0,0], "22":[0,0], "23":[0,0],"00":[0,0],"01":[0,0],"02":[0,0], "03":[0,0], "04":[0,0], "05":[0,0]}
    for info in post_ffl.find():
        timestamp = str(info["timestamp"])
        date_temp = timestamp.split(" ")[1]
        date_list = date_temp.split(":")
        time = date_list[0]
        numLikes = info["number_of_likes"]
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
@app.route("/insta/postdatetime", methods=['GET'])
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
        date_str = date_list[2] + " " + date_list[1] + " " + date_list[0]
        day = findDay(date_str)

        #Time 
        date_list = date_temp[1].split(":")
        time = date_list[0]

        temp_dict = dict_daytime[day]
        if type(temp_dict) is not list:
            temp_list = temp_dict[time]
            
            numLikes = info["number_of_likes"]

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

@app.route("/insta/interaction_type", methods=['GET'])
def interactionType():
    dict_result = {"competition": [], "featured": [], "product": [], "promotion": [], "infographics": [], "others": []}
    for info in ig_interaction.find():
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

@app.route("/insta/total_interaction", methods=['GET'])
def interactionCount():
    dict_result = {"competition": 0, "featured": 0, "product": 0, "promotion": 0, "infographics": 0, "others": 0}
    for info in ig_interaction.find():
        interaction_type = info["interaction_type"]
        count = info["count"]
        temp_value = dict_result[interaction_type]
        temp_value += count
        dict_result[interaction_type] = temp_value
    for info in fb_interaction.find():
        interaction_type = info["interaction_type"]
        count = info["count"]
        temp_value = dict_result[interaction_type]
        temp_value += count
        dict_result[interaction_type] = temp_value
    
    result = {
        "result": dict_result
    }
    
    return jsonify(result),200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)