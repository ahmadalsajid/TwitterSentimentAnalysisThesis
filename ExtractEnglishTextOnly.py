import pymongo
import csv
# from time import clock
# start_time = clock()

client = pymongo.MongoClient('localhost', 27017)
db = client.tsadb
cursor = db.TSAtweets.find(
    {"$or":
          [
              {'lang': {'$regex': 'en', '$options': 'i'}},
              {'lang': {'$regex': 'en-gb', '$options': 'i'}},
          ]
     }, {"text": 1, "_id": 0})
with open("EnglishTweet.csv", "w", newline='', encoding='UTF-16') as f:     # for UTF-16 encoding
    writer = csv.writer(f)
    for t in cursor:
        writer.writerow([t['text'],])
# print("total time :",round(clock()-start_time,2),"seconds")