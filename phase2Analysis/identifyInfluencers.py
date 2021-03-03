### 5. Identify influencers

# (Amongst the tagged post, who are the influencers of the post? Which influencer is not doing well?)

# 1. Loop through tagged posts 
# 2. Get usernames
# 3. Using username, get list of followers and count of followers for the followers
#     1. Throw into another datatable
# 4. Data table then sort to find top 10 influencers engaged (post type and engagement rate) 
# - Benchmarking: define how many followers = an influencer *(600? 700 followers?)*
# - Average over max (subsequent engagement)
#     - likes / impressions
#         - impressions = followers * (randbetween(7,10)*10)

from instaloader import Instaloader, Hashtag, Profile, InstaloaderContext
from pymongo import MongoClient
import ssl
from pprint import pprint
from random import randrange
import requests


db = MongoClient("",
                 ssl=True, ssl_cert_reqs=ssl.CERT_NONE)



def identify_influencers():
    people_who_tagged_ffl = get_users_who_tagged_ffl()
    db_name = db.instagram.related_influencer_strength

    print(len(people_who_tagged_ffl.items()))

    for person,count_of_likes_and_comments in people_who_tagged_ffl.items():

        # https://stackoverflow.com/questions/52225334/webscraping-instagram-follower-count-beautifulsoup
        # ------------------------------------------------------------
        username =  person
        url = 'https://www.instagram.com/' + username
        r = requests.get(url).text

        start = '"edge_followed_by":{"count":'
        end = '},"followed_by_viewer"'
        if r.find(start) >= 0:
            followers= int(r[r.find(start)+len(start):r.rfind(end)])

            start = '"edge_follow":{"count":'
            end = '},"follows_viewer"'
            following= int(r[r.find(start)+len(start):r.rfind(end)])

            print(person, followers, following)
            # ------------------------------------------------------------

            if(followers > 5000):
                impression = followers * (randrange(30,50)/100)
            elif(followers > 4000):
                impression = followers * (randrange(40,60)/100)
            elif(followers > 3000):
                impression = followers * (randrange(50,70)/100)
            elif(followers > 2000):
                impression = followers * (randrange(60,80)/100)
            else:
                impression = followers * (randrange(70,90)/100)
            
            if (impression == 0):
                impression = 1
            print(followers)
            print(impression)

            result_status = db_name.insert_one({
                "profile_name": person,
                "followers": followers,
                "no_of_likes_and_comments": count_of_likes_and_comments,
                "engagement_result": (count_of_likes_and_comments/impression) * 100,
            })
            print("Inserted " + person)
        

        


def get_users_who_tagged_ffl():
    datatable = {}

    # get followers
    db2 = db.instagram.freshfruitlab_taggedpost
    data = db2.find()

    people_who_tagged_ffl = {}
    for key in data:
        # print(key["username"]) # here contains all the users who tagged ffl
        people_who_tagged_ffl[key['username']] = int(key['number_of_likes']) + int(key['number_of_comments'])
    return people_who_tagged_ffl

identify_influencers()
