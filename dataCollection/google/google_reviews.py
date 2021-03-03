import requests
import json
import time
from pymongo import MongoClient
import ssl
import csv
import pandas as pd

class GooglePlaces(object):
    def __init__(self, apiKey):
        super(GooglePlaces, self).__init__()
        self.apiKey = apiKey
 
    def search_places_by_coordinate(self, location, radius, types):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        places = []
        params = {
            'location': location,
            'radius': radius,
            'types': types,
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params = params)
        results =  json.loads(res.content)
        places.extend(results['results'])
        time.sleep(2)
        while "next_page_token" in results:
            params['pagetoken'] = results['next_page_token'],
            res = requests.get(endpoint_url, params = params)
            results = json.loads(res.content)
            places.extend(results['results'])
            time.sleep(2)
        return places
 
    def get_place_details(self, place_id, fields):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/details/json"
        params = {
            'placeid': place_id,
            'fields': ",".join(fields),
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params = params)
        place_details =  json.loads(res.content)
        return place_details



db = MongoClient("", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)


db_name = db.googlereviews.googleplatform1094

for i in range(3):
    result = []
    if i == 0:
        location = "1.323778,103.865097"
        db_name = db.googlereviews.googleplatform1094
        csv = "platform1094.csv"
    elif i == 1:
        location = "1.318588, 103.909564"
        db_name = db.googlereviews.googlefreshfruitlab
        csv = "freshfruitlab.csv"
    else:
        location = "1.360860,103.989619"
        db_name = db.googlereviews.googleherit8ge
        csv = "herit8ge.csv"
    
    api = GooglePlaces("AIzaSyCapf_gEK_P1r64LeWzJ0kqo5fH5p3lEJI")
    places = api.search_places_by_coordinate(location, "2", "restaurant")
    fields = ['name', 'formatted_address', 'international_phone_number', 'website', 'rating', 'review']
    
    for place in places:
        details = api.get_place_details(place['place_id'], fields)
        try:
            name = details['result']['name']
        except KeyError:
            name = ""
        
        try:
            reviews = details['result']['reviews']
        except KeyError:
            reviews = []


        for review in reviews:
            author_name = review['author_name']
            rating = review['rating']
            text = review['text']
            time_info = review['relative_time_description']

            item = {
                'review_author': author_name,
                'rating': rating,
                'reviews': text,
                'timestamp': time_info
            }

            result_status = db_name.insert_one(item)
            result.append(item)

    df = pd.DataFrame(result) # <--- convert list to DataFrame
    df.to_csv(csv) 



    

