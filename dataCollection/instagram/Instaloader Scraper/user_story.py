from instaloader import Instaloader, Hashtag, Profile, InstaloaderContext
from itertools import dropwhile, takewhile
import datetime
import os
from pymongo import MongoClient
import ssl


db = MongoClient("", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

def get_instance():
    scraper = Instaloader(
        compress_json=False, 
        download_pictures=False,
        download_videos=False,
        download_video_thumbnails=False,
        max_connection_attempts=0
    )
    
    return scraper


def scrape_userstories(profilename_list):
    scraper = get_instance()
    scraper.login("", "")
    for profile_name in profilename_list:
        db_name = db.instagram.user_stories
        profile = Profile.from_username(scraper.context, profile_name)
        current_count = 0
        skip_count = 0
        for story in scraper.get_stories():
            for item in story.get_items():
                profile = item.profile
                storyitem = item.url
                storytype = item.typename
                timestamp = item.date_local
                print(profile)
                print(storyitem)
                print(storytype)
                print(timestamp)
                story_item = {
                    "profile_name": profile,
                    "story_type": storytype,
                    "story_item": storyitem,
                    "timestamp": timestamp,
                }

                result_status = db_name.insert_one(story_item)


profile_detail = ["platform1094","freshfruitslab","herit8ge"]
scrape_userstories(profile_detail)


