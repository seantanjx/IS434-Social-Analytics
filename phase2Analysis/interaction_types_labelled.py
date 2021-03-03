import pymongo
import csv 

client = pymongo.MongoClient("")

with open("fb_interaction_types.csv", encoding="utf-8") as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=",")
  header = next(csv_reader)

  all_posts = []

  for row in csv_reader:
    post = {"interaction_type": []}
    for i in range(len(header)):
      if i < 5: # <5 because the interaction type starts from the 5th column (aka 'competition') 
        post[header[i]] = row[i]
      else: 
        if row[i] != "": 
          post["interaction_type"].append(header[i])
    all_posts.append(post)

  for post in all_posts: 
    client.phase2.competitor_ig_interaction.insert_one(post)