#########################################################
##########TOP 10 percentage of post interm of likes######

from itertools import islice
from math import ceil
from instaloader import Instaloader, Profile
from pymongo import MongoClient
import ssl

db = MongoClient("", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

db_name = db.instagram.top10post_intermsoflikes

def get_instance():
    scraper = Instaloader(
        compress_json=False, 
        download_pictures=False,
        download_videos=False,
        download_video_thumbnails=False,
        max_connection_attempts=0
    )
    
    return scraper

def top_post(profile_detail):
    scraper = get_instance()
    X_percentage = 10
  
    for profile_name in profile_detail:
        profile = Profile.from_username(scraper.context,profile_name)
        posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda p:p.likes + p.comments, reverse=True)

        for post in islice(posts_sorted_by_likes, ceil(profile.mediacount * X_percentage / 100)):
            
            time = post.date_utc
            post_type = post.typename
            post_detail = post.url
            caption = post.caption
            hashtags = post.caption_hashtags
            likes = post.likes 
            comment = post.comments

            item = {
                "Cafe": profile_name,
                "timestamp": time,
                "post_type": post_type, #The differetnt types of post will gather how many likes
                "post_detail": post_detail, 
                "caption": caption,
                "number_of_likes": likes, #Unique number of likes 
                "number_of_comments": comment,
            }

            result_status = db_name.insert_one(item)
            print(result_status)



profile_detail = ["platform1094","freshfruitslab","herit8ge"]

#Get Top 10% Post
top_post(profile_detail)