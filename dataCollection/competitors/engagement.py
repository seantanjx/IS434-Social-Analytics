# sum(number of likes per post / followers) / number of posts

from pymongo import MongoClient
import ssl
from collections import defaultdict
from pprint import pprint
from os import path

db = MongoClient("",
                 ssl=True, ssl_cert_reqs=ssl.CERT_NONE)


def db_detail(profile_name):
    if profile_name == "windowsillpies":
        db_name = db.competitors.windowsillpies_ig_postinfo
    elif profile_name == "thewhiterabbitsg":
        db_name = db.competitors.thewhiterabbitsg_ig_postinfo
    elif profile_name == "hatterstreet":
        db_name = db.competitors.hatterstreet_ig_postinfo
    elif profile_name == "enchantedcafe":
        db_name = db.competitors.enchantedcafe_ig_postinfo
    else:
        db_name = db.competitors.handlebaroriginal_ig_postinfo
    return db_name


def get_engagement(profile_names):
    for competitor in profile_names:
        profile_name, followers = competitor[0], competitor[1]
        db_name = db_detail(profile_name)
        post_count = db_name.count_documents()
        no_of_likes = 0
        no_of_comments = 0
        weighted_likes = 0
        weighted_comments = 0
        for post in db_name.find():
            no_of_likes += post['number_of_likes']
            no_of_comments += post['number_of_comments']
            weighted_likes += post['number_of_likes']/followers
            weighted_comments += post['number_of_comments']/followers

        likes_engagement_rate = round((weighted_likes/post_count)*100, 2)
        comments_engagement_rate = round((weighted_comments/post_count)*100, 2)

        item = {
            "profile_name": profile_name,
            "total_post": post_count,
            "no_of_followers": followers,
            "total_likes": no_of_likes,
            "total_comments": no_of_comments,
            "engagement_rate(likes)": likes_engagement_rate,
            "engagement_rate(comments)": comments_engagement_rate
        }

        post_db_name = db.competitors.competitor_ig_analysis
        result_status = post_db_name.insert_one(item)
        print(result_status)


profile_detail = ["windowsillpies", "thewhiterabbitsg",
                  "hatterstreet", "enchantedcafe", "handlebaroriginal"]
followers_list = [7669, 4214, 5611, 16300, 702]

get_engagement(list(zip(profile_detail, followers_list)))
