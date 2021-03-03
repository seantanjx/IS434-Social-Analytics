from pymongo import MongoClient
import ssl
from pprint import pprint

db = MongoClient("",
                 ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

# post engagement rate = (post interactions / total follower count) * 100

#instagram
def getInstagramPostTaggedInfo(restaurant, native_post_db_name, tagged_post_db_name):
    dt = {'native_post': {}, 'tagged_post': {}}

    # get followers
    db2 = db.instagram.general_information
    general_info = db2.find_one(filter={'profile_name': restaurant})
    dt['followers'] = general_info['no_of_followers']

    post_count = 0
    like_sum = 0
    comment_sum = 0
    likes_weight = 0
    comments_weight = 0
    for i in native_post_db_name.find():
        post_count += 1
        like_sum += i['number_of_likes']
        comment_sum += i['number_of_comments']
        likes_weight += i['number_of_likes']/dt['followers']
        comments_weight += i['number_of_comments']/dt['followers']

    # for reference
    dt['restaurant'] = restaurant
    # get metrics
    dt['native_post']['post_count'] = post_count
    dt['native_post']['like_sum'] = like_sum
    dt['native_post']['comment_sum'] = comment_sum
    dt['native_post']['likes_per_post'] = int(like_sum / post_count)
    dt['native_post']['comments_per_post'] = round(
        (comment_sum / post_count), 2)
    dt['native_post']['average_likes_engagment'] = round(
        (likes_weight / post_count)*100, 2)
    dt['native_post']['average_comments_engagment'] = round(
        (comments_weight / post_count)*100, 2)

    post_count = 0
    like_sum = 0
    comment_sum = 0

    for i in tagged_post_db_name.find():
        post_count += 1
        like_sum += i['number_of_likes']
        comment_sum += i['number_of_comments']

    dt['tagged_post']['post_count'] = post_count
    dt['tagged_post']['like_sum'] = like_sum
    dt['tagged_post']['comment_sum'] = comment_sum
    dt['tagged_post']['likes_per_post'] = round(like_sum / post_count, 2)
    dt['tagged_post']['comments_per_post'] = round(comment_sum / post_count, 2)

    db_name = db.phase1.instagram_engagement
    result = db_name.insert_one(dt)
    return result


ffl_post_info = getInstagramPostTaggedInfo(
    'freshfruitslab', db.instagram.freshfruitlab_postinfo, db.instagram.freshfruitlab_taggedpost)
herit8ge_post_info = getInstagramPostTaggedInfo(
    'herit8ge', db.instagram.herit8ge_postinfo, db.instagram.herit8ge_taggedpost)
platform1094_post_info = getInstagramPostTaggedInfo(
    'platform1094', db.instagram.platform1094_postinfo, db.instagram.platform1094_taggedpost)

#Formula: Sum(number of likes/number of followers)/post count & Sum(number of comments/number of followers)/post count
#Limitations: Not accurate as number of followers fluctuates/increases as time goes by, but we are aggregating it based on the latest follower count

pprint(ffl_post_info)
pprint(herit8ge_post_info)
pprint(platform1094_post_info)

