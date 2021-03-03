from flask import Flask, jsonify, request
import pymongo
from flask_cors import CORS
from os import environ
from bson.json_util import dumps
from pymongo import MongoClient
import ssl

import json

app = Flask(__name__)
instagramDB = MongoClient("", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

CORS(app)

db_fb = instagramDB['facebookdata']
platform_post = db_fb["platform1094"]
ffl_post = db_fb["freshfruitlab"]
herit8ge_post = db_fb["herit8ge"]
phase1 = instagramDB['phase1']
insta_engagement = phase1["facebook_engagement"]


#number_of_followers
@app.route("/fb/numPosts", methods=['GET'])
def fbnumPosts():
    result = []
    platform1094 = platform_post.find().count()
    ffl = ffl_post.find().count()
    herit8ge = herit8ge_post.find().count()

    result = {
        "platform1094": platform1094,
        "freshfruitlab": ffl,
        "herit8ge": herit8ge
    }
    
    return jsonify(result),200

@app.route("/fb/engagement_likes", methods=["GET"])
def fbengagementLikes():
    result_dict = {}
    for info in insta_engagement.find():
        data = info["restaurant"]
        count = info["average_likes_engagmeent"]
        result_dict[data] = count

    return jsonify(result_dict),200

@app.route("/fb/engagement_comments", methods=["GET"])
def fbengagementComments():
    result_dict = {}
    for info in insta_engagement.find():
        data = info["restaurant"]
        count = info["average_comments_engagmeent"]
        result_dict[data] = count


    return jsonify(result_dict),200


db_insta = instagramDB['instagram']
phase1 = instagramDB['phase1']
general_info = db_insta["general_information"]
platform_tagged = db_insta["platform1094_taggedpost"]
ffl_tagged = db_insta["freshfruitlab_taggedpost"]
herit8ge_tagged = db_insta["herit8ge_taggedpost"]
average_likes = phase1["averageLikes"]
insta_engagement2 = phase1["instagram_engagement"]

#number_of_followers
@app.route("/insta/numFollowers", methods=['GET'])
def numFollowers():
    result = []
    for info in general_info.find():
        data = info["profile_name"]
        followers_data = data + ":" + str(info["no_of_followers"])
        result.append(followers_data)

    result = {
        "followers": result
    }
    return jsonify(result),200

#number of posts
@app.route("/insta/numberPost", methods=["GET"])
def ignumPosts():
    result = []
    for info in general_info.find():
        data = info["profile_name"]
        post_data = data + ":" + str(info["total_post"])
        result.append(post_data)

    result = {
        "num_post": result
    }
    return jsonify(result),200


#number of tagged/mention post
@app.route("/insta/taggedPost", methods=["GET"])
def taggedPost():
    result = []
    platform1094 = platform_tagged.find().count()
    ffl = ffl_tagged.find().count()
    herit8ge = herit8ge_tagged.find().count()

    result = {
        "platform1094": platform1094,
        "freshfruitlab": ffl,
        "herit8ge": herit8ge
    }
    
    return jsonify(result),200

@app.route("/insta/average_likes", methods=["GET"])
def averageLikes():
    result = {}
    for info in average_likes.find():
        data = info["Channel"]
       
        ffl = info["freshfruitlab"]
        platform = info["platform1094"]
        heri = info["herit8ge"]
        avg_like_list = [platform,ffl,heri]

        result[data] = avg_like_list

    result = {
        "average_likes": result
    }
    return jsonify(result),200



@app.route("/insta/engagement_likes", methods=["GET"])
def igengagementLikes():
    result_dict = {}
    for info in insta_engagement2.find():
        data = info["restaurant"]
        count = info["native_post"]["average_likes_engagment"]
        result_dict[data] = count

    return jsonify(result_dict),200

@app.route("/insta/engagement_comments", methods=["GET"])
def igengagementComments():
    result_dict = {}
    for info in insta_engagement2.find():
        data = info["restaurant"]
        count = info["native_post"]["average_comments_engagment"]
        result_dict[data] = count

    return jsonify(result_dict),200




if __name__ == '__main__':
    app.run(host='0.0.0.0')