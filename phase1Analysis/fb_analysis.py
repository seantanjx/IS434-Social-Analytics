from pymongo import MongoClient
import ssl
from pprint import pprint

db = MongoClient("",
                 ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

# post engagement rate = (post interactions / total follower count) * 100

# instagram


def getFacebookPostTaggedInfo(restaurant, db_name, followers):
    dt = {}

    # get followers
    db2 = db.instagram.general_information
    i = db2.find_one(filter={'profile_name': restaurant})
    dt['followers'] = followers

    post_count = 0
    like_sum = 0
    comment_sum = 0
    likes_weight = 0
    comments_weight = 0
    for i in db_name.find():
        post_count += 1
        like_sum += i['likes']
        comment_sum += i['comments']
        likes_weight += i['likes']/dt['followers']
        comments_weight += i['comments']/dt['followers']

    # for reference
    dt['restaurant'] = restaurant
    # get metrics
    dt['post_count'] = post_count
    dt['like_sum'] = like_sum
    dt['comment_sum'] = comment_sum
    dt['likes_per_post'] = int(like_sum / post_count)
    dt['comments_per_post'] = round(
        (comment_sum / post_count), 2)
    dt['average_likes_engagmeent'] = round(
        (likes_weight / post_count)*100, 2)
    dt['average_comments_engagmeent'] = round(
        (comments_weight / post_count)*100, 2)

    db_name = db.phase1.facebook_engagement
    result = db_name.insert_one(dt)
    return result


ffl_post_info = getFacebookPostTaggedInfo(
    'freshfruitslab', db.facebookdata.freshfruitlab, 5533)
herit8ge_post_info = getFacebookPostTaggedInfo(
    'herit8ge', db.facebookdata.herit8ge, 428)
platform1094_post_info = getFacebookPostTaggedInfo(
    'platform1094', db.facebookdata.platform1094, 9795)

# Formula: Sum(number of likes/number of followers)/post count & Sum(number of comments/number of followers)/post count
# Limitations: Not accurate as number of followers fluctuates/increases as time goes by, but we are aggregating it based on the latest follower count

pprint(ffl_post_info)
pprint(herit8ge_post_info)
pprint(platform1094_post_info)
