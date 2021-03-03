'''
Competitors
1) windosillpies
IG (7669 followers): https://www.instagram.com/windowsillpies/
FB: https://www.facebook.com/WindowsillPies/

2) thewhiterabbitsg
IG (4214 followers): https://www.instagram.com/thewhiterabbitsg/
FB: https://www.facebook.com/TWRsg/

3) Hatter Street
IG (5611 followers): https://www.instagram.com/hatterstreet/
FB: https://www.facebook.com/HatterStreet/

4) Monsanco enchanted cafe
IG (16300 followers): https://www.instagram.com/enchantedcafe/
FB: https://www.facebook.com/EnchantedCafeSg/

5) Handlebaroriginal
IG (702 followers): https://www.instagram.com/handlebaroriginal/
FB: https://www.facebook.com/HandlebarSGGillmanBarracks/
'''

from pymongo import MongoClient
import ssl
from collections import defaultdict
from pprint import pprint
from wordcloud import WordCloud
from os import path


db = MongoClient("",
                 ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

db_name = db.instagram.top10competitorpost_intermsoflikes

dir = path.dirname(__file__)


def get_competitor_posts():
    competitor = defaultdict(list)
    for post in db_name.find():
        competitor[post['Cafe']].append(
            {
                'post caption': post['caption'].replace("\n", ""),
                'post hashtags': post['hashtags'],
                'post likes': post['number_of_likes'],
                'post comments': post['number_of_comments']
            }
        )
    return competitor


def create_wordcloud(text):
    wordcloud = WordCloud(width=1920, height=1080).generate(text)
    wordcloud.to_file(path.join(dir, "cloud.png"))


def getHashtags_wordcloud():
    hashtag_string = ""
    competitorPosts = get_competitor_posts()
    for v in competitorPosts.values():
        for i in v:
            for hashtags in i['post hashtags']:
                if hashtags != "hatterstreet":
                    hashtag_string += hashtags + " "
    create_wordcloud(hashtag_string.rstrip())

    # to get a dictionary of hashtags and its frequency

    # hashtag_dict = defaultdict(int)
    # for v in competitorPosts.values():
    #     for i in v:
    #         for hashtags in i['post hashtags']:
    #             hashtag_dict[hashtags] += 1
    #pprint(sorted(hashtag_dict.items(), key=lambda t: t[1], reverse=True))

getHashtags_wordcloud()

# profile_detail = ["windowsillpies", "thewhiterabbitsg", "hatterstreet", "enchantedcafe", "handlebaroriginal"]