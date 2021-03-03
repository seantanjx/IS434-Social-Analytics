from instaloader import Instaloader, Hashtag, Profile, InstaloaderContext
from itertools import dropwhile, takewhile
import datetime
import os
import csv
import time
import requests
from bs4 import BeautifulSoup

def read_file(filename):
    result = []
    with open(filename, 'r') as f:
        for line in f:
            result.append(line.strip())
    return result

def get_next_target(filename):
    with open(filename, 'r') as f:
        target = f.readline().strip()
    with open(filename, 'r') as r:
        lines = r.readlines()
    with open(filename, 'w') as w:
        w.writelines(lines[1:])
    return target

def write_file(write_list, filename):
    with open(filename, 'w') as f:
        result = ''
        for line in write_list:
            have_emoji = False
            for ch in line:
                if len(ch) != len(ch.encode()):
                    have_emoji = True
            if not have_emoji:
                result += line + '\n'
        f.write(result.strip())

def append_file(append_list, filename):
    with open(filename, 'a') as f:
        result = ''
        for line in append_list:
            have_emoji = False
            for ch in line:
                if len(ch) != len(ch.encode()):
                    have_emoji = True
            if not have_emoji:
                result += line + '\n'
        f.write(result)

def append_name(profile_name, filename):
    with open(filename, 'a') as f:
        profile_name = profile_name + '\n'
        f.write(profile_name)

def user_tracked(profile_name):
    # Track if user has been scraped
    tracked_list = read_file("tracked_list.txt")
    if profile_name in tracked_list:
        return True
    return False

def get_login(filename):
    with open(filename, 'r') as f:
        login_credentials = f.readline().strip().split()
        username = login_credentials[0]
        password = login_credentials[1]
    with open(filename, 'r') as r:
        lines = r.readlines()
    with open(filename, 'w') as w:
        w.writelines(lines[1:])
    return username, password

def get_instance():
    scraper = Instaloader(
        compress_json=False, 
        download_pictures=False,
        download_videos=False,
        download_video_thumbnails=False,
        max_connection_attempts=0
    )
    
    return scraper

def scrape_following_followers(filename):
    
    #Get instance
    scraper = get_instance()
    
    # Login
    scraper.login("jackthesmurffff2", "jack555")
    
    target_profiles = read_file(filename)

    for profile_name in target_profiles:
        profile = Profile.from_username(scraper.context, profile_name)
        print("Getting 'following'")
        following = profile.get_followees()
        newFollowing = sorted(following, key=lambda x: x.userid, reverse=False)
        print("Getting 'followers'")
        followers = profile.get_followers()
        newFollowers = sorted(followers, key=lambda x: x.userid, reverse=False)

        # saving following to csv
        print("Saving" + profile_name + "following to file...")
        fCount = 0
        with open(profile_name + "_following.csv", 'w', newline='') as followingCSV:
            followingWriter = csv.writer(followingCSV, delimiter=',')
            for f in newFollowing:
                fCount += 1
                followingWriter.writerow([f.userid, f.username])

        os.renames(profile_name + "_following.csv", profile_name + "_" + str(fCount) + "_following.csv")

        # saving follower to csv
        print("Saving" + profile_name + "follower to file")
        fCount = 0
        with open(profile_name + "_followers.csv", 'w', newline='') as followerCSV:
            followerWriter = csv.writer(followerCSV, delimiter=',')
            followerWriter.writerow(
                ['User ID', 'Username', 'Fullname', 'Followed by you', 'Blocked by you', 'Follows you', 'Profile URL',
                'Avatar URL'])
            for f in newFollowers:
                fCount += 1
                followerWriter.writerow(
                    [f.userid, f.username])
                # , f.followed_by_viewer, f.blocked_by_viewer, f.follows_viewer, f.profile_pic_url, f.get_profile_pic_url(),
                # f.external_url

        os.renames(profile_name + "_followers.csv", profile_name + "_" + str(fCount) + "_followers.csv")
        # ---------------------------------------------------------------------------------------------
        print("Saved")
        
    scraper.close()

def scrape_followers(profile_name):
    scraper = get_instance()
    scraper.login("jackthesmurffff18@gmail.com", "Jack1111") #(jackthesmurffff, jack321)

    profile = Profile.from_username(scraper.context, profile_name)
    print("Getting FFL 'followers'")
    followers = profile.get_followers()
    newFollowers = sorted(followers, key=lambda x: x.username, reverse=False)

    # saving follower to csv
    print("Saving " + profile_name + " follower to file")
    fList = []
    with open("freshfruitslab_followers.csv", 'w', newline='') as followerCSV:
        followerWriter = csv.writer(followerCSV, delimiter=',')
        followerWriter.writerow(['Target Followers'])
        for f in newFollowers:
            rowData = profile_name + " " + f.username
            print(rowData)
            fList.append(f.username)
            followerWriter.writerow([rowData])
    write_file(fList, "targets.txt")

    #subsequent followers

    count = 0 #count to prevent rate limit
    should_pause = False
    profile_name = get_next_target("targets.txt")
    try:
        while profile_name != "":
            fList = []
            count += 1
            newFollowers = []
            print(count)
            if count == 20: #pause after 30 request
                print("20s sleep zZzZz")
                time.sleep(20)
                count = 0
            try:
                if should_pause: #puase after scrapping followers
                    print("30s sleep zZzZz")
                    time.sleep(30)
                    should_pause = False

                profile = Profile.from_username(scraper.context, profile_name)
                print("Getting " + profile_name + " 'followers'")
                followers = profile.get_followers()
                newFollowers = sorted(followers, key=lambda x: x.username, reverse=False)
                if len(newFollowers) > 0:
                    should_pause = True

            except Exception as e: # in case of 400 bad request -> due to over request limit on instagram
                print(e)
                wait = input("PRESS ENTER TO CONTINUE")
                print("BACK TO WORK :c")

            # saving subsequent follower to csv
            if len(newFollowers) > 0:
                print("Saving " + profile_name + " follower to file")
                with open("freshfruitslab_followers.csv", 'a', newline='') as followerCSV:
                    followerWriter = csv.writer(followerCSV, delimiter=',')
                    for f in newFollowers:
                        rowData = profile_name + " " + f.username
                        print(rowData)
                        fList.append(f.username)
                        followerWriter.writerow([rowData])
            # print("=== newfList ===")
            # print(newfList)
            # print("=== fList ===")
            # print(fList)
            append_file(fList, "targets.txt")
            profile_name = get_next_target("targets.txt")
    except Exception as e:
        print(e)
        print("error")

    scraper.close()

#to be used only after 1st scrapper is ran
def scrape_followers_2():
    scraper = get_instance()
    username, password = get_login('instagram_acc.txt')
    print("Login -> " + username)
    scraper.login(username, password)

    #subsequent followers
    count = 1 #count to prevent rate limit
    should_pause = False
    profile_name = get_next_target("targets.txt")
    try:
        while profile_name != "":
            print("\nprofile_name -> " + profile_name)
            # Cut nodes by half
            if count % 2 == 0:
                print(f"count={count}->alternate skipzz")
                profile_name = get_next_target("targets.txt")
                profile_name = get_next_target("targets.txt")
                profile_name = get_next_target("targets.txt")
                #write to tracked_list
                # append_name(profile_name, "tracked_list.txt")
                count += 1
                continue
            # Track if user has been scraped
            user_tracked_check = user_tracked(profile_name)
            if user_tracked_check:
                print("skip, user already tracked: ")
                profile_name = get_next_target("targets.txt")
                #write to tracked_list
                # append_name(profile_name, "tracked_list.txt")
                # count += 1
                continue
            #write to tracked_list
            append_name(profile_name, "tracked_list.txt")
            print("append to tracked_list.txt")
            fList = []
            count += 1
            newFollowers = []
            print("count" + str(count))
            if count == 15: #pause after 15 request
                print(f"count={count}->15s sleep zZzZz")
                time.sleep(20)
                count = 1
            try:
                if should_pause: #puase after scrapping followers
                    # print("20s sleep zZzZz")
                    # time.sleep(20)
                    should_pause = False

                profile = Profile.from_username(scraper.context, profile_name)
                print("Getting " + profile_name + " 'followers'")
                print(profile)
                followers = profile.get_followers()
                newFollowers = sorted(followers, key=lambda x: x.username, reverse=False)
                if len(newFollowers) > 0:
                    should_pause = True

            except Exception as e: # in case of 400 bad request -> due to over request limit on instagram
                print(e)
                # wait = input("PRESS ENTER TO CONTINUE")
                #close old login
                scraper.close()

                #new login
                scraper = get_instance()
                username, password = get_login('instagram_acc.txt')
                print("Login -> " + username)
                scraper.login(username, password)
                
                print("BACK TO WORK :c")

            # saving subsequent follower to csv
            if len(newFollowers) > 0:
                print("Saving " + profile_name + " follower to file")
                with open("freshfruitslab_followers.csv", 'a', newline='') as followerCSV:
                    followerWriter = csv.writer(followerCSV, delimiter=',')
                    for f in newFollowers:
                        rowData = profile_name + " " + f.username
                        print(rowData)
                        fList.append(f.username)
                        followerWriter.writerow([rowData])

            append_file(fList, "targets.txt")
            # print("10s sleep zZzZz")
            # if count % 3 == 0:
            #     time.sleep(12)
            profile_name = get_next_target("targets.txt")

    except Exception as e:
        print(e)
        print("error")

    scraper.close()

def scrape_beautiful_followers():
    instagram_url = "https://www.instagram.com/"
    profile_url = "jackphannnn"
    response = requests.get(f"{instagram_url}/{profile_url}")
    print(response.status_code)
    if response.ok:
        # print(response.content)
        soup = BeautifulSoup(response.content, 'html.parser')
        # print(soup)
        # print(soup.find_all('span', class_=''))
        print(response.content)

def followers_url():
    target_profiles = read_file("targets.txt")
    instagram_url = "https://www.instagram.com"
    url_list = []
    for profile_name in target_profiles:
        url = f"{instagram_url}/{profile_name}/"
        url_list.append(url)

    write_file(url_list,"url.txt")


# scrape_beautiful_followers()
# followers_url()

#freshfruitslab
#(jackthesmurffff, jack456)
#(jackthesmurffff2, jack789)

# scrape_following_followers("target_profile.txt")
# scrape_followers("freshfruitslab")
scrape_followers_2()

# write_file(['jack', 'phan'], 'target.txt')
# a = get_next_target('test.txt')



# ========= Other commands ===============
# Save all files into this folder relative to the programme
#if not os.path.isdir('raw_insta_data'):
#    os.mkdir('raw_insta_data')
#os.chdir('raw_insta_data')

#Filter Parameter
start_date = datetime.datetime(2016, 12, 17)
end_date = datetime.datetime(2020, 10, 15)

# To scrape data from endpoints
# scrape_profile("target_profile.txt")
# scrape_hashtag('target_hashtags.txt')

# Snowballing the recommended hashtag and accounts to continue scraping
# get_suggested_account('target_profile.txt')
# get_suggested_tag('target_hashtags.txt')