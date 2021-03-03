import pymongo
import csv

client = pymongo.MongoClient("")
ig_db = client.instagram 
fb_db = client.facebookdata 

ig_collection = ig_db.freshfruitlab_postinfo
ig_array = [["post_url", "caption", "likes", "comments", "post_type"]]
fb_collection = fb_db.freshfruitlab
fb_array = [["post_url", "caption", "likes", "comments", "post_image"]]

for document in ig_collection.find():
  ig_array.append([document.get("post_detail"), document.get("caption"), document.get("number_of_likes"),document.get("number_of_comments"),document.get("post_type")])

for document in fb_collection.find():
  image_posts = len(document.get("post_image"))
  fb_array.append([document.get("post_url"), document.get("post_caption"), document.get("likes"),document.get("comments"), image_posts])

# with open('facebook.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerows(fb_array)

competition = {"interaction_type": "competition", "count": 0, "likes": 0, "comments": 0, "avg_likes": 0, "avg_comments": 0 } 
featured = {"interaction_type": "featured", "count": 0, "likes": 0, "comments": 0, "avg_likes": 0, "avg_comments": 0 }  
product = {"interaction_type": "product", "count": 0, "likes": 0, "comments": 0, "avg_likes": 0, "avg_comments": 0 } 
promotion = {"interaction_type": "promotion", "count": 0, "likes": 0, "comments": 0, "avg_likes": 0, "avg_comments": 0 } 
infographics = {"interaction_type": "infographics", "count": 0, "likes": 0, "comments": 0, "avg_likes": 0, "avg_comments": 0 }  
others = {"interaction_type": "others", "count": 0, "likes": 0, "comments": 0, "avg_likes": 0, "avg_comments": 0 } 

with open("competitor_interaction_types.csv", encoding="utf-8") as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=",")

  # for i in range(len(next(csv_reader))): 
  #   if i > 5: 
  #     header[i] = {"interaction_type": header[i], "count": 0, "likes": 0, "comments": 0, "avg_likes": 0, "avg_comments": 0 }
  #     print(header[i])

  csv_file.readline() 
  
  for row in csv_reader:
    if row[6] != "": 
      competition["count"] += 1
      competition["likes"] += int(row[2])
      competition["comments"] += int(row[3])
    if row[7] != "": 
      featured["count"] += 1
      featured["likes"] += int(row[2])
      featured["comments"] += int(row[3])
    if row[8] != "": 
      product["count"] += 1
      product["likes"] += int(row[2])
      product["comments"] += int(row[3])
    if row[9] != "": 
      promotion["count"] += 1
      promotion["likes"] += int(row[2])
      promotion["comments"] += int(row[3])
    if row[10] != "": 
      infographics["count"] += 1
      infographics["likes"] += int(row[2])
      infographics["comments"] += int(row[3])
    if row[11] != "": 
      others["count"] += 1
      others["likes"] += int(row[2])
      others["comments"] += int(row[3])
  
  for type in [competition, featured, product, promotion, infographics, others]: 
    type["avg_likes"] = round(type["likes"] / type["count"])
    type["avg_comments"] = round(type["comments"] / type["count"])

print(competition, featured, product, promotion, infographics, others)

client.phase2.competitor_interaction.insert_many([
  competition, 
  featured,
  product,
  promotion, 
  infographics, 
  others
])