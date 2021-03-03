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
def numPosts():
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
def engagementLikes():
    result_dict = {}
    for info in insta_engagement.find():
        data = info["restaurant"]
        count = info["average_likes_engagmeent"]
        result_dict[data] = count

    return jsonify(result_dict),200

@app.route("/fb/engagement_comments", methods=["GET"])
def engagementComments():
    result_dict = {}
    for info in insta_engagement.find():
        data = info["restaurant"]
        count = info["average_comments_engagmeent"]
        result_dict[data] = count


    return jsonify(result_dict),200




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)