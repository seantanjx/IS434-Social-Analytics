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

from datetime import datetime as dt
from datetime import timedelta  

app = Flask(__name__)
mongoDB = MongoClient("", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)


# Reviews
# ===============================================================================
greviews = mongoDB['googlereviews']
ffl_greviews = greviews['googlefreshfruitlab']

trip_reviews = mongoDB['tripadvisiordata']
ffl_trip_reviews = trip_reviews['reviews_freshfruitlab']

trip_reviews = mongoDB['burppleReviews']
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

# ===============================================================================


# Competitors
# ===============================================================================
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
    # final_dict = {}
    # enchanted = db_competitors['enchantedcafe_ig_postinfo']
    # handlebar = db_competitors['handlebaroriginal_ig_postinfo']
    # hatterstreet = db_competitors['hatterstreet_ig_postinfo']
    # whiterabbit = db_competitors['thewhiterabbitsg_ig_postinfo']
    # illipies = db_competitors['windowsillpies_ig_postinfo']
    # list_of_info = [enchanted, handlebar, hatterstreet, whiterabbit, illipies]
    # counter = 0
    # for data in list_of_info:
    #     counter += 1
    #     result = postTypeInfo(data)
    #     if counter == 1:
    #         final_dict["enchanted"] = result
    #     elif counter == 2:
    #         final_dict["handlebar"] = result
    #     elif counter == 3:
    #         final_dict["hatterstreet"] = result
    #     elif counter == 4:
    #         final_dict["whiterabbit"] = result
    #     else:
    #         final_dict["illipies"] = result

    final_dict = {
        "result": {
            "enchanted": {
            "GraphImage": {
            "comments": 1.9642857142857142,
            "likes": 117.01785714285714
        },
            "GraphSidecar": {
            "comments": 1.3888888888888888,
            "likes": 130.16666666666666
            },
            "GraphVideo": {
            "comments": 228.55172413793105,
            "likes": 351.3448275862069
            }
            },
            "handlebar": {
            "GraphImage": {
            "comments": 0.5346534653465347,
            "likes": 20.831683168316832
            },
            "GraphSidecar": {
            "comments": 0.7391304347826086,
            "likes": 32.52173913043478
            },
            "GraphVideo": {
            "comments": 0.4,
            "likes": 17.6
            }
            },
            "hatterstreet": {
            "GraphImage": {
            "comments": 1.7802503477051461,
            "likes": 60.79554937413074
            },
            "GraphSidecar": {
            "comments": 3.493333333333333,
            "likes": 72.37333333333333
            },
            "GraphVideo": {
            "comments": 1.4583333333333333,
            "likes": 51.708333333333336
            }
            },
            "illipies": {
            "GraphImage": {
            "comments": 3.6507936507936507,
            "likes": 146.93650793650792
            },
            "GraphSidecar": {
            "comments": 3.074074074074074,
            "likes": 118.4074074074074
            },
            "GraphVideo": {
            "comments": 1,
            "likes": 102
            }
            },
            "whiterabbit": {
            "GraphImage": {
            "comments": 1.736231884057971,
            "likes": 70.02608695652174
            },
            "GraphSidecar": {
            "comments": 0.3333333333333333,
            "likes": 93.33333333333333
            },
            "GraphVideo": {
            "comments": 0,
            "likes": 0
            }
            }
            }
    }
    
    
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
# ===============================================================================



# facebook
# ===============================================================================

db_facebook = mongoDB['facebookdata']
post_ffl = db_facebook['freshfruitlab']

phase2 = mongoDB['phase2']
fb_interaction = phase2["fb_interaction"]

@app.route("/fb/dayofpost", methods=['GET'])
def fbdayofpost():
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
def fbtimeofpost():
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
def fbpostdatetime():
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
def fbinteractionType():
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

# ===============================================================================



# influencer engagement
# ===============================================================================
@app.route("/influencer_engagement/influencers_strength", methods=["GET"])
def influencers_strength():
    result_dict = {}
    influencer_strength = mongoDB.instagram.related_influencer_strength
    for info in influencer_strength.find():
        # {"ahpuingang" : "6.921373200442968", ...}
        result_dict[info["profile_name"]] = {
            "no_of_likes_and_comments" : info["no_of_likes_and_comments"],
            "followers" : info["followers"],
            "engagement_rate": info["engagement_result"],

        }
    return json.dumps({"result" :result_dict})
# ===============================================================================



# instagram posttype
# ===============================================================================
db_insta = mongoDB['instagram']
post_ffl2 = db_insta['freshfruitlab_postinfo']

phase2 = mongoDB['phase2']
ig_interaction = phase2["ig_interaction"]
fb_interaction = phase2["fb_interaction"]

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
    for info in post_ffl2.find():
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
    for info in post_ffl2.find():
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
    for info in post_ffl2.find():
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
def igdayofpost():
    dict_day = {"Monday":[0,0], "Tuesday": [0,0], "Wednesday": [0,0], "Thursday":[0,0], "Friday": [0,0], "Saturday": [0,0], "Sunday": [0,0]}
    print(dict_day)
    for info in post_ffl2.find():
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
def igtimeofpost():
    dict_day = {"06":[0,0], "07": [0,0], "08": [0,0], "09":[0,0], "10": [0,0], "11": [0,0], "12": [0,0], "13":[0,0], "14":[0,0], "15":[0,0], "16":[0,0],
     "17":[0,0], "18":[0,0], "19":[0,0], "20":[0,0], "21":[0,0], "22":[0,0], "23":[0,0],"00":[0,0],"01":[0,0],"02":[0,0], "03":[0,0], "04":[0,0], "05":[0,0]}
    for info in post_ffl2.find():
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
def igpostdatetime():
    dict_daytime = {"Monday":{"06":[0,0], "07": [0,0], "08": [0,0], "09":[0,0], "10": [0,0], "11": [0,0], "12": [0,0], "13":[0,0], "14":[0,0], "15":[0,0], "16":[0,0],
    "17":[0,0], "18":[0,0], "19":[0,0], "20":[0,0], "21":[0,0], "22":[0,0], "23":[0,0],"00":[0,0],"01":[0,0],"02":[0,0], "03":[0,0], "04":[0,0], "05":[0,0]}, "Tuesday": {"06":[0,0], "07": [0,0], "08": [0,0], "09":[0,0], "10": [0,0], "11": [0,0], "12": [0,0], "13":[0,0], "14":[0,0], "15":[0,0], "16":[0,0],
    "17":[0,0], "18":[0,0], "19":[0,0], "20":[0,0], "21":[0,0], "22":[0,0], "23":[0,0],"00":[0,0],"01":[0,0],"02":[0,0], "03":[0,0], "04":[0,0],"05":[0,0]}, "Wednesday": {"06":[0,0], "07": [0,0], "08": [0,0], "09":[0,0], "10": [0,0], "11": [0,0], "12": [0,0], "13":[0,0], "14":[0,0], "15":[0,0], "16":[0,0],
     "17":[0,0], "18":[0,0], "19":[0,0], "20":[0,0], "21":[0,0], "22":[0,0], "23":[0,0],"00":[0,0],"01":[0,0],"02":[0,0], "03":[0,0], "04":[0,0], "05":[0,0]}, "Thursday": {"06":[0,0], "07": [0,0], "08": [0,0], "09":[0,0], "10": [0,0], "11": [0,0], "12": [0,0], "13":[0,0], "14":[0,0], "15":[0,0], "16":[0,0],
     "17":[0,0], "18":[0,0], "19":[0,0], "20":[0,0], "21":[0,0], "22":[0,0], "23":[0,0],"00":[0,0],"01":[0,0],"02":[0,0], "03":[0,0], "04":[0,0], "05":[0,0]}, "Friday": {"06":[0,0], "07": [0,0], "08": [0,0], "09":[0,0], "10": [0,0], "11": [0,0], "12": [0,0], "13":[0,0], "14":[0,0], "15":[0,0], "16":[0,0],
     "17":[0,0], "18":[0,0], "19":[0,0], "20":[0,0], "21":[0,0], "22":[0,0], "23":[0,0],"00":[0,0],"01":[0,0],"02":[0,0], "03":[0,0], "04":[0,0], "05":[0,0]}, "Saturday": {"06":[0,0], "07": [0,0], "08": [0,0], "09":[0,0], "10": [0,0], "11": [0,0], "12": [0,0], "13":[0,0], "14":[0,0], "15":[0,0], "16":[0,0],
     "17":[0,0], "18":[0,0], "19":[0,0], "20":[0,0], "21":[0,0], "22":[0,0], "23":[0,0],"00":[0,0],"01":[0,0],"02":[0,0], "03":[0,0], "04":[0,0], "05":[0,0]}, "Sunday": {"06":[0,0], "07": [0,0], "08": [0,0], "09":[0,0], "10": [0,0], "11": [0,0], "12": [0,0], "13":[0,0], "14":[0,0], "15":[0,0], "16":[0,0],
     "17":[0,0], "18":[0,0], "19":[0,0], "20":[0,0], "21":[0,0], "22":[0,0], "23":[0,0],"00":[0,0],"01":[0,0],"02":[0,0], "03":[0,0], "04":[0,0], "05":[0,0]}}
    for info in post_ffl2.find():
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
def iginteractionType():
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

# ===============================================================================



# postdate difference
# ===============================================================================
db_fb = mongoDB['facebookdata']
post_ffl_fb = db_fb['freshfruitlab']

db_competitor = mongoDB["competitors"]
enchanted_freq = db_competitor["enchantedcafe_ig_postinfo"]
handlerbar_freq = db_competitor["handlebaroriginal_ig_postinfo"]
hatterstreet_freq = db_competitor["hatterstreet_ig_postinfo"]
whiterabbit_freq = db_competitor["thewhiterabbitsg_ig_postinfo"]

@app.route("/insta/postdateinformation", methods=['GET'])
def postDate():
    #past 6 months
    list_result = {}
    temp_date = "01/03/2020"
    end_date = "14/10/2020"
    temp_date = dt.strptime(temp_date, "%d/%m/%Y")
    end_date = dt.strptime(end_date, "%d/%m/%Y")
    while temp_date.date() < end_date.date():
        list_result[str(temp_date.date())] = 0
        temp_date = temp_date + timedelta(days=1)  

    for info in post_ffl2.find():
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
    temp_date = dt.strptime(temp_date, "%d/%m/%Y")
    end_date = dt.strptime(end_date, "%d/%m/%Y")
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

    result = {
        "result": {"result":{"2020-09-14":1,"2020-09-15":0,"2020-09-16":1,"2020-09-17":0,"2020-09-18":1,"2020-09-19":0,"2020-09-20":1,"2020-09-21":1,"2020-09-22":0,"2020-09-23":1,"2020-09-24":0,"2020-09-25":1,"2020-09-26":1,"2020-09-27":0,"2020-09-28":1,"2020-09-29":1,"2020-09-30":0,"2020-10-01":1,"2020-10-02":0,"2020-10-03":2,"2020-10-04":1,"2020-10-05":0,"2020-10-06":1,"2020-10-07":1,"2020-10-08":0,"2020-10-09":0,"2020-10-10":0,"2020-10-11":0,"2020-10-12":0,"2020-10-13":1}}
    }

    return jsonify(result),200

@app.route("/insta/handlerbar_freq", methods=['GET'])
def handlerbarFreq():

    result = {
        "result": {"result":{"2020-09-14":0,"2020-09-15":0,"2020-09-16":0,"2020-09-17":0,"2020-09-18":0,"2020-09-19":0,"2020-09-20":0,"2020-09-21":0,"2020-09-22":0,"2020-09-23":0,"2020-09-24":0,"2020-09-25":0,"2020-09-26":0,"2020-09-27":1,"2020-09-28":0,"2020-09-29":0,"2020-09-30":0,"2020-10-01":0,"2020-10-02":0,"2020-10-03":0,"2020-10-04":0,"2020-10-05":0,"2020-10-06":0,"2020-10-07":0,"2020-10-08":0,"2020-10-09":0,"2020-10-10":0,"2020-10-11":0,"2020-10-12":0,"2020-10-13":0}}
    }

    return jsonify(result),200

@app.route("/insta/hatterstreet_freq", methods=['GET'])
def hatterstreetFreq():

    list_result = {"result":{"2020-09-14":0,"2020-09-15":0,"2020-09-16":0,"2020-09-17":1,"2020-09-18":2,"2020-09-19":0,"2020-09-20":0,"2020-09-21":0,"2020-09-22":0,"2020-09-23":0,"2020-09-24":1,"2020-09-25":2,"2020-09-26":1,"2020-09-27":0,"2020-09-28":0,"2020-09-29":0,"2020-09-30":1,"2020-10-01":0,"2020-10-02":1,"2020-10-03":0,"2020-10-04":1,"2020-10-05":0,"2020-10-06":1,"2020-10-07":0,"2020-10-08":1,"2020-10-09":1,"2020-10-10":1,"2020-10-11":1,"2020-10-12":0,"2020-10-13":1}}

    result = {
        "result": list_result
    }

    return jsonify(result),200

@app.route("/insta/whiterabbit_freq", methods=['GET'])
def whiterabbitFreq():

    result = {
        "result": {"result":{"2020-09-14":0,"2020-09-15":1,"2020-09-16":0,"2020-09-17":0,"2020-09-18":0,"2020-09-19":0,"2020-09-20":0,"2020-09-21":0,"2020-09-22":1,"2020-09-23":0,"2020-09-24":0,"2020-09-25":0,"2020-09-26":0,"2020-09-27":0,"2020-09-28":0,"2020-09-29":1,"2020-09-30":0,"2020-10-01":0,"2020-10-02":0,"2020-10-03":0,"2020-10-04":0,"2020-10-05":0,"2020-10-06":1,"2020-10-07":0,"2020-10-08":0,"2020-10-09":0,"2020-10-10":0,"2020-10-11":0,"2020-10-12":0,"2020-10-13":0}}
    }

    return jsonify(result),200
# ===============================================================================

if __name__ == '__main__':
    app.run(host='0.0.0.0')