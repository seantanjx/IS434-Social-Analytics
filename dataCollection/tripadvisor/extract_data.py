from bs4 import BeautifulSoup
from pymongo import MongoClient
import ssl
import csv
import requests
import re
import pandas as pd


db = MongoClient("", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

def get_soup(url):

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'}

    r = s.get(url, headers=headers)

    if r.status_code != 200:
        print('status code:', r.status_code)
    else:
        return BeautifulSoup(r.content, 'html.parser')

def parse(url, response, db_name):

    if not response:
        print('no response:', url)
        return

    # get number of reviews
    num_reviews = response.find('span', class_='reviews_header_count').text
    num_reviews = num_reviews[1:-1]
    num_reviews = int(num_reviews)

    # create template for urls to pages with reviews
    url = url.replace('.html', '-or{}.html')
    print('template:', url)

    # load pages with reviews
    for offset in range(0, num_reviews, 5):
        print('url:', url.format(offset))
        url_ = url.format(offset)
        parse_reviews(url_, get_soup(url_),db_name)

def parse_reviews(url, response, db_name):
    print('review:', url)

    if not response:
        print('no response:', url)
        return

    # get every review
    for idx, review in enumerate(response.find_all('div', class_='review-container')):
        extracted = str(review.find('div', class_='ui_column is-9'))
        pos1 = extracted.find("ui_bubble_rating")
        bubble_rating = extracted[pos1:66][-1]
        
        item = {
            'review_title': review.find('span', class_='noQuotes').text,
            'review_body': review.find('p', class_='partial_entry').text,
            'bubble_rating': bubble_rating
        }

        result_status = db_name.insert_one(item)

        results.append(item) 

        # for key,val in item.items():
        #     print(key, ':', val)
        # print('----')


# --- main ---

s = requests.Session()

start_urls = [
    'https://www.tripadvisor.com/Restaurant_Review-g294265-d12127098-Reviews-Platform_1094-Singapore.html','https://www.tripadvisor.com/Restaurant_Review-g11890205-d19823548-Reviews-Herit8ge-Changi.html',
    'https://www.tripadvisor.com/Restaurant_Review-g294265-d7076613-Reviews-Fresh_Fruits_Lab-Singapore.html'
]

final_result = []
count = 0
for url in start_urls:
    results = []
    if count == 0:
        db_name = db.tripadvisiordata.reviews_platform1094
        csv = "platform1094.csv"
    elif count == 1:
        db_name = db.tripadvisiordata.reviews_herit8ge
        csv = "herit8ge.csv"
    else:
        db_name = db.tripadvisiordata.reviews_freshfruitlab
        csv = "freshfruitlab.csv"
    count += 1
    parse(url, get_soup(url),db_name)
    final_result.append(results)
    df = pd.DataFrame(results) # <--- convert list to DataFrame
    df.to_csv(csv) 

