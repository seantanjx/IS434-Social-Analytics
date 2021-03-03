import ffl
import herit8ge
import platform1094
from pymongo import MongoClient
import ssl
import csv

client = MongoClient("", ssl=True, ssl_cert_reqs=ssl.CERT_NONE)

ffl_value, ffl_reviews = ffl.main()
herit8ge_value, herit8ge_reviews = herit8ge.main()
platform1094_value, platform1094_reviews = platform1094.main()

# 1.0 For Burpple Data
db = client.burppleData

# 1.1 Burpple Data - FFL
col = db.freshfruitlab

# change data to dictionary before pushing to mongo
data = {
    "Categories": ffl_value[1],
    "Location": ffl_value[2],
    "Number_of_Reviews": len(ffl_value[4]),
    "Reviews": ffl_value[4],
}

col.insert_one(data)


# 1.2 Burpple Data - Herit8ge
col = db.herit8ge

data = {
    "Categories": herit8ge_value[1],
    "Location": herit8ge_value[2],
    "Number_of_Reviews": len(herit8ge_value[4]),
    "Reviews": herit8ge_value[4],
}

col.insert_one(data)



# 1.3 Burpple Data - Platform 1094
col = db.platform1094

data = {
    "Categories": platform1094_value[1],
    "Location": platform1094_value[2],
    "Number_of_Reviews": len(platform1094_value[4]),
    "Reviews": platform1094_value[4],
}

col.insert_one(data)



# 2.0 For Burpple Reviews
db = client.burppleReviews

# 2.1 Burpple Reviews - FFL
col = db.freshfruitlab
col.insert_many(ffl_reviews)


# 2.2 Burpple Reviews - Herit8ge
col = db.herit8ge
col.insert_many(herit8ge_reviews)

# 2.3 Burpple Reviews - Platform 1094
col = db.platform1094
col.insert_many(platform1094_reviews)

print('Success')


