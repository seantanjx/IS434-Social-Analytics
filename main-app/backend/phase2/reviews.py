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
reviews = MongoClient("", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

CORS(app)

greviews = reviews['googlereviews']
ffl_greviews = greviews['googlefreshfruitlab']

trip_reviews = reviews['tripadvisiordata']
ffl_trip_reviews = trip_reviews['reviews_freshfruitlab']

trip_reviews = reviews['burppleReviews']
ffl_burp_reviews = trip_reviews['freshfruitlab']

#number of reviews
@app.route("/reviews/countall", methods = ['GET'])
def countReviews():
    google_reviews = ffl_greviews.find().count()
    trip_reviews = ffl_trip_reviews.find().count()
    burp_reviews = ffl_trip_reviews.find().count()

    result = {
        "google": google_reviews,
        "trip": trip_reviews,
        "burp": burp_reviews
    }

    return jsonify(result),200

@app.route("/reviews/grating", methods=['GET'])
def getGReviews():
    ratings_dict = {0: 0, 1:0, 2:0, 3:0,4:0, 5:0}
    for info in ffl_greviews.find():
        rating = info["rating"]
        ratings_dict[rating] += 1

    result = {
        "result": ratings_dict
    }

    return jsonify(result),200


@app.route("/reviews/trating", methods=['GET'])
def getTReviews():
    ratings_dict = {"0": 0, "1":0, "2":0, "3":0, "4" :0, "5" :0}
    for info in ffl_trip_reviews.find():
        rating = info["bubble_rating"]
        ratings_dict[rating] += 1

    result = {
        "result": ratings_dict
    }

    return jsonify(result),200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007, debug=True)