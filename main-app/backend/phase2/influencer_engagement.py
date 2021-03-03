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


@app.route("/influencer_engagement/influencers_strength", methods=["GET"])
def influencers_strength():
    result_dict = {}
    influencer_strength = instagramDB.instagram.related_influencer_strength
    for info in influencer_strength.find():
        # {"ahpuingang" : "6.921373200442968", ...}
        result_dict[info["profile_name"]] = {
            "no_of_likes_and_comments" : info["no_of_likes_and_comments"],
            "followers" : info["followers"],
            "engagement_rate": info["engagement_result"],

        }
    return json.dumps({"result" :result_dict})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011, debug=True)