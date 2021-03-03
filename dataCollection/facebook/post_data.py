from facebook_scraper import get_posts
from pymongo import MongoClient
import ssl
import csv

db = MongoClient("", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

#Extract Post information
def get_cafe_data(cafe_name, dbname):
    for post in get_posts(cafe_name, pages=1000):
        data = db_name
        post_data = {
            'post_id': post['post_id'],
            'post_caption': post['text'],
            'timestamp': post['time'],
            'post_image': post['images'],
            'likes': post['likes'],
            'comments': post['comments'],
            'post_url': post['post_url']
        }
        result = data.insert_one(post_data)
        print(result)

#Extract post information to CSV
def extract_data_to_csv(csv_name, cafe_name):
    with open(csv_name, mode='w') as platform_name:
        data_writer = csv.writer(platform_name, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for post in get_posts(cafe_name, pages=1000):
            data_writer.writerow([post['post_id'], post['text'], post['time'], post['image'], post['likes'],post['comments'],post['post_url']])

cafes = ["Platform1094", "herit8ge", "FFLFreshFruitsLab"]
csv_name = ["fb_platform1094.csv", "fb_heritage.csv", "fb_freshfruitlab.csv"]

for i in range(1,len(cafes)):
    if i == 0:
        db_name = db.facebookdata.platform1094
    elif i == 1:
        db_name = db.facebookdata.herit8ge
    else:
        db_name = db.facebookdata.freshfruitlab
    get_cafe_data(cafes[i], db_name)
    extract_data_to_csv(csv_name[i],cafes[i])
    print('Success')



