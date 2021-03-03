from instaloader import Instaloader, Hashtag, Profile, InstaloaderContext
import csv

def get_instance():
    scraper = Instaloader(
        compress_json=False, 
        download_pictures=False,
        download_videos=False,
        download_video_thumbnails=False,
        max_connection_attempts=0
    )
    
    return scraper

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

def append_name(profile_name, filename):
    with open(filename, 'a') as f:
        profile_name = profile_name + '\n'
        f.write(profile_name)

try:
    scraper = get_instance()
    # username, password = get_login('instagram_acc.txt')
    # print("Login -> " + username)
    # scraper.login(username, password)

    profile_name = get_next_target("targets.txt")
    while profile_name != "":
        try:
            # Track if user has been scraped
            user_tracked_check = user_tracked(profile_name)
            if user_tracked_check:
                print("skip, user already tracked: " + profile_name)
                profile_name = get_next_target("targets.txt")
                continue
            else:
                append_name(profile_name, "tracked_list.txt")

            profile = Profile.from_username(scraper.context, profile_name)

            likes = set()
            print("Fetching likes of all posts of profile {}.".format(profile.username))
            c = 0
            for post in profile.get_posts():
                print(post)
                likes = likes | set(post.get_likes())
                c += 1
                if c >= 10: #likes from max 50 post
                    break

            # print("Fetching followers of profile {}.".format(profile.username))
            # followers = profile.get_followers()
            # intersect = likes.intersection(followers)
            # real_follower = list(intersect)

            # saving follower to csv
            print("Saving "+ str(len(likes)) + " follower to file")
            fList = []
            with open("followers.csv", 'a', newline='') as followerCSV:
                followerWriter = csv.writer(followerCSV, delimiter=',')
                # for f in real_follower:
                for f in likes:
                    rowData = profile_name + " " + f.username
                    print(rowData)
                    fList.append(f.username)
                    followerWriter.writerow([rowData])
            append_file(fList, "targets.txt")

            profile_name = get_next_target("targets.txt")
            print("end of loop\n")


            # ghosts = followers - likes

            # print("Storing ghosts into file.")
            # with open("inactive-users.txt", 'w') as f:
            #     for ghost in ghosts:
            #         print(ghost.username, file=f)

        except Exception as e:
            print(e)
            print('error -> change account')
            scraper.close()

            scraper = get_instance()
            # username, password = get_login('instagram_acc.txt')
            # print("Login -> " + username)
            # scraper.login(username, password)

        
except Exception as e:
    print(e)
    print('error')
