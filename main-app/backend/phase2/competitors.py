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
mongoDB = MongoClient("", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

CORS(app)

db_competitors = mongoDB['competitors']
ffl_competitor = db_competitors['competitor_ig_analysis']
hashtag_freq = db_competitors['hashtag_frequency']

instagram = mongoDB['instagram'] 
ffl_10competitor = instagram["top10competitorpost_intermsoflikes"]


phase2 = mongoDB['phase2'] 
competitor_interaction = phase2["competitor_interaction"]
competitor_ig_interaction = phase2["competitor_ig_interaction"]


@app.route("/competitor/likes_comments", methods=['GET'])
def competitorLikes():
    competitor_info = {}
    for info in ffl_competitor.find():
        list_info = []
        profile_name = info["profile_name"]
        total_likes = info["total_likes"]
        total_comments = info["total_comments"]
        list_info.append(total_likes)
        list_info.append(total_comments)
        competitor_info[profile_name] = list_info

    result = {
       "result": competitor_info
    }
    return jsonify(result),200

@app.route("/competitor/engagement_rate", methods=['GET'])
def competitorEngagemen():
    competitor_info = {}
    for info in ffl_competitor.find():
        list_info = []
        profile_name = info["profile_name"]
        engagement_rate = info["engagement_rate(likes)"]
        comments_rate = info["engagement_rate(comments)"]
        list_info.append(engagement_rate)
        list_info.append(comments_rate)
        competitor_info[profile_name] = list_info

    result = {
       "result": competitor_info
    }
    return jsonify(result),200

@app.route("/competitor/post_number", methods=['GET'])
def postNumber():
    total_post = {}
    for info in ffl_competitor.find():
        profile_name = info["profile_name"]
        total_post_number = info["total_post"]
        total_post[profile_name] = total_post_number
    
    result = {
       "result": total_post
    }

    return jsonify(result),200

@app.route("/competitor/intermlikes", methods=['GET'])
def competitorPostLikesComments():
    competitor_dict = {"windowsillpies": [], "thewhiterabbitsg": [], "hatterstreet": [], "enchantedcafe": [], "handlebaroriginal": []}
    competitor_caption_interaction_dict = {}
    phase2 = mongoDB['phase2'] 
    competitor_ig_interaction = phase2["competitor_ig_interaction"]
    for data in competitor_ig_interaction.find(): 
        # interaction_type = data['interaction_type']
        # if (len(interaction_type) > 0):
        #     competitor_caption_interaction_dict["post_detail"] = data['interaction_type'][1]
        # else:
        #     competitor_caption_interaction_dict["post_detail"] = data['interaction_type'][0]
        competitor_caption_interaction_dict[data['post_detail']] = data['interaction_type'][0]
    
    for info in ffl_10competitor.find():
        profile_name = info["Cafe"]
        list_of_info = competitor_dict[profile_name]
        templist = []
        caption = info["caption"]
        num_likes = info["number_of_likes"]
        number_comments = info["number_of_comments"]
        post_detail = info['post_detail']
        competitor_ig_interaction = competitor_caption_interaction_dict[post_detail]
        # print(competitor_ig_interaction)
        list_of_info.append([caption, num_likes, number_comments, competitor_ig_interaction])
    
    result = {
       "result": competitor_dict
    }

    return jsonify(result),200

@app.route("/competitor/hashtag", methods=['GET'])
def competitorHashtag():
    dict_hash = {}
    for info in hashtag_freq.find():
        hashtag = info["Hashtag"]
        freq = info["Frequency"]
        dict_hash[hashtag] = freq
    sorted_hashtag = sorted(dict_hash.items(), key=lambda x: x[1], reverse=True)
   
    result = {
       "result": sorted_hashtag
    }
    
    return jsonify(result),200


@app.route("/competitor/posttype", methods=['GET'])
def competitorPostSummary():
    final_dict = {}
    enchanted = db_competitors['enchantedcafe_ig_postinfo']
    handlebar = db_competitors['handlebaroriginal_ig_postinfo']
    hatterstreet = db_competitors['hatterstreet_ig_postinfo']
    whiterabbit = db_competitors['thewhiterabbitsg_ig_postinfo']
    illipies = db_competitors['windowsillpies_ig_postinfo']
    list_of_info = [enchanted, handlebar, hatterstreet, whiterabbit, illipies]
    counter = 0
    for data in list_of_info:
        counter += 1
        result = postTypeInfo(data)
        if counter == 1:
            final_dict["enchanted"] = result
        elif counter == 2:
            final_dict["handlebar"] = result
        elif counter == 3:
            final_dict["hatterstreet"] = result
        elif counter == 4:
            final_dict["whiterabbit"] = result
        else:
            final_dict["illipies"] = result
    
    result = {
       "result": final_dict
    }

    return jsonify(result),200

    
def postTypeInfo(data):
    dict_detail = {}
    count_image = 0
    count_sidecar = 0
    count_video = 0
    image_likes = 0
    sidecar_likes = 0
    video_likes = 0
    image_comments = 0
    sidecar_comments = 0
    video_comments = 0
    for info in data.find():
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
    
    avg_likes_image = 0
    avg_comments_sidecar = 0
    avg_likes_sidecar = 0
    avg_comments_sidecar = 0
    avg_likes_video = 0
    avg_comments_video = 0
    if image_likes != 0 and count_image != 0:
        avg_likes_image = image_likes/count_image
    if image_comments != 0 and count_image != 0:
        avg_comments_image = image_comments/count_image

    if sidecar_likes != 0 and count_sidecar != 0:
        avg_likes_sidecar = sidecar_likes/count_sidecar
    if sidecar_comments != 0 and count_sidecar != 0:
        avg_comments_sidecar = sidecar_comments/count_sidecar

    if video_likes != 0 and count_video != 0: 
        avg_likes_video = video_likes/count_video
    if video_comments != 0 and count_video != 0:
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

    return result

@app.route("/competitor/interaction_type", methods=['GET'])
def competitorInteractionType():
    dict_result = {"competition": [], "featured": [], "product": [], "promotion": [], "infographics": [], "others": []}
    for info in competitor_interaction.find():
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
    app.run(host='0.0.0.0', port=5008, debug=True)