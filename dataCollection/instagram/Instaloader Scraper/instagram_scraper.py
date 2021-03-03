from instaloader import Instaloader, Hashtag, Profile, InstaloaderContext
from itertools import dropwhile, takewhile
import datetime
import os
from pymongo import MongoClient
import ssl


db = MongoClient("", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

def read_file(filename):
    result = []
    with open(filename, 'r') as f:
        for line in f:
            result.append(line.strip())
    return result

def write_file(write_list, filename):
    with open(filename, 'a') as f:
        result = ''
        for line in write_list:
            have_emoji = False
            for ch in line:
                if len(ch) != len(ch.encode()):
                    have_emoji = True
                    
            if not have_emoji:
                result += line + '\n'
                    
        f.write(result.strip())

def get_instance():
    scraper = Instaloader(
        compress_json=False, 
        download_pictures=False,
        download_videos=False,
        download_video_thumbnails=False,
        max_connection_attempts=0
    )
    
    return scraper

def db_detail(profile_name):
    if profile_name == "platform1094":
        db_name = db.instagram.platform1094_postinfo
    elif profile_name == "freshfruitslab":
        db_name = db.instagram.freshfruitlab_postinfo
    else:
        db_name = db.instagram.herit8ge_postinfo
    return db_name

def db_detail_tagged(profile_name):
    if profile_name == "platform1094":
        db_name = db.instagram.platform1094_taggedpost
    elif profile_name == "freshfruitslab":
        db_name = db.instagram.freshfruitlab_taggedpost
    else:
        db_name = db.instagram.herit8ge_taggedpost
    return db_name
    
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


def general_account_info(profilename_list):
    scraper = get_instance()
    scraper.login("", "")
    all_followers_cafe = []
    for profile_name in profilename_list:
        db_name = db.instagram.general_information
        profile = Profile.from_username(scraper.context, profile_name)
        total_post = profile.mediacount
        igtv_count = profile.igtvcount
        number_followers = profile.followers
        number_followees = profile.followees
        business_category = profile.business_category_name
        biography = profile.biography
        profile_pic = profile.profile_pic_url

        followers_list = profile.get_followers()
        follower_userlist = []
        for i in followers_list:
            follower_userlist.append(i.username)

        all_followers_cafe.append([profile_name,follower_userlist])

        followees_list = profile.get_followees()
        followee_userlist = []
        for i in followees_list:
            followee_userlist.append(i.username)
        
        profile_item = {
            "profile_name": profile_name,
            "total_post": total_post,
            "igtv_count": igtv_count,
            "no_of_followers": len(follower_userlist),
            "no_of_followees": len(followee_userlist),
            "business_category": business_category,
            "biography": biography,
            "profile_pic": profile_pic,
            "followers_info": follower_userlist,
            "followeee_info": followee_userlist
        }

        result_status = db_name.insert_one(profile_item)
        print(result_status)
    return all_followers_cafe

def scrape_tagged_posts(profilename_list):
    scraper = get_instance()
    for profile_name in profilename_list:
        db_name = db_detail_tagged(profile_name)
        current_count = 0
        skip_count = 0
        
        profile = Profile.from_username(scraper.context, profile_name)
        tagged_post = profile.get_tagged_posts() 
        print ('Scraping Username:   ' + profile.username)
        for post in tagged_post:
            if post.date > start_date and post.date < end_date:
                current_count += 1
                username = post.owner_username
                time = post.date_utc
                post_type = post.typename
                post_detail = post.url
                caption = post.caption
                hashtags = post.caption_hashtags
                likes = post.likes 
                comment = post.comments

                all_comments = post.get_comments()
                comments_info = []
                for i in all_comments:
                    comments_info.append(i.text)

                all_likes = post.get_likes()
                profile_info = []
                for i in all_likes:
                    profile_info.append(i.username)
                
                item = {
                    "timestamp": time,
                    "username": username,
                    "post_type": post_type, #The differetnt types of post will gather how many likes
                    "post_detail": post_detail, 
                    "caption": caption,
                    "hashtags": hashtags,
                    "number_of_likes": likes, #Unique number of likes 
                    "number_of_comments": comment,
                    "commnets_info": comments_info,
                    "profile_likes": profile_info,
                }
                result_status = db_name.insert_one(item)
                print(result_status)
            else:
                skip_count += 1
                print ('[ {} / {} ]'.format(current_count + skip_count, profile.mediacount), 'Skipping')
    
    scraper.close()       

def followers_list(profilename_list):
    scraper = get_instance()
    scraper.login("", "")
    db_name = db.instagram.followers_detail_platform1094 #Update the db to the correct cafe name
    all_followers_cafe = []
    for profile_name in profilename_list:
        for profile_name_info in profile_name[1]:
            profile = Profile.from_username(scraper.context, profile_name_info)
            followers_list = profile.get_followers()
            follower_userlist = []
            for i in followers_list:
                follower_userlist.append(i.username)

            followees_list = profile.get_followees()
            followee_userlist = []
            for i in followees_list:
                followee_userlist.append(i.username)
            
            profile_item = {
                "profile_name": profile_name,
                "followers_info": follower_userlist,
            }

            all_followers_cafe.append([profile_name, followee_userlist])

            result_status = db_name.insert_one(profile_item)
            print(result_status)
    return all_followers_cafe

def scrape_profile(profilename_list):
    #Get instance
    scraper = get_instance()
  
    
    for profile_name in profilename_list:
        db_name = db_detail(profile_name)
        current_count = 0
        skip_count = 0
        
        profile = Profile.from_username(scraper.context, profile_name)
        user_posts = profile.get_posts() 
        
        # for post in takewhile(lambda p: p.date > start_date, dropwhile(lambda p: p.date > end_date, user_posts)):
        #     scraper.download_post(post, target=profile.username)
        print ('Scraping Username:   ' + profile.username)
        for post in user_posts:
            if post.date > start_date and post.date < end_date:
                current_count += 1
                print ('[ {} / {} ]'.format(current_count + skip_count, profile.mediacount), end=" ")
                time = post.date_utc
                post_type = post.typename
                post_detail = post.url
                caption = post.caption
                hashtags = post.caption_hashtags
                likes = post.likes 
                comment = post.comments
                video = post.is_video
                video_view = post.video_view_count
                video_duration = post.video_duration

                all_comments = post.get_comments()
                comments_info = []
                for i in all_comments:
                    comments_info.append(i.text)

                all_likes = post.get_likes()
                profile_info = []
                for i in all_likes:
                    profile_info.append(i.username)
                
                item = {
                    "timestamp": time,
                    "post_type": post_type, #The differetnt types of post will gather how many likes
                    "post_detail": post_detail, 
                    "caption": caption,
                    "hashtags": hashtags,
                    "number_of_likes": likes, #Unique number of likes 
                    "number_of_comments": comment,
                    "commnets_info": comments_info,
                    "profile_likes": profile_info,
                    "video": video,
                    "video_views": video_view,
                    "video_duration": video_duration #how will the duration affect the views (Get the count and plot the chart)

                }
                result_status = db_name.insert_one(item)
                print(result_status)
            else:
                skip_count += 1
                print ('[ {} / {} ]'.format(current_count + skip_count, profile.mediacount), 'Skipping')
    
    scraper.close()


start_date = datetime.datetime(2014, 6, 8)
end_date = datetime.datetime(2020, 10, 15)
# profile_detail = ["platform1094","freshfruitslab","herit8ge"]
profile_detail = ["freshfruitslab"]

# To scrape data from endpoints

#To extract all the posts
scrape_profile(profile_detail)

#Change the index depends on which cafe you want to run


#To extract the profile information
# followers_info = general_account_info(profile_detail)
# followers_detail = followers_info

# followers_list(followers_detail[0])
# followers_info.followers_list(followers_info[0])

#To extract the tagged information
# scrape_tagged_posts(profile_detail)

# User Stories
# scrape_userstories(profile_detail)

