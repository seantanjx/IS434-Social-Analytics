import pymongo

client = pymongo.MongoClient("")
ig_db = client.instagram 
fb_db = client.facebookdata 

ig_collections = {"freshfruitlab": ig_db.freshfruitlab_postinfo, "platform1094": ig_db.platform1094_postinfo, "herit8ge": ig_db.herit8ge_postinfo}
fb_collections = {"freshfruitlab": fb_db.freshfruitlab, "platform1094": fb_db.platform1094, "herit8ge": fb_db.herit8ge}

#by average number of likes
ig_performance = {"Channel": "Instagram"}
fb_performance = {"Channel": "Facebook"}

for cafe, col in ig_collections.items():
  total_likes = 0
  for document in col.find():
    total_likes += document.get("number_of_likes")
  ig_performance[cafe] = round(total_likes / col.count())

for cafe, col in fb_collections.items(): 
  total_likes = 0 
  for document in col.find():
    total_likes += document.get("likes")
  fb_performance[cafe] = round(total_likes / col.count())

print('Instagram', ig_performance)
print('Facebook', fb_performance)


client.phase1.averageLikes.insert_many([
  ig_performance, 
  fb_performance
])