import pymongo
from time import clock
start_time = clock()

client = pymongo.MongoClient('localhost', 27017)
db = client.tsadb
# cursor to store distinct user id from db
cursor = db.TSAtweets.distinct("user.id_str")
# already got info about them
already_exist = db.DistinctUser.distinct("user.id_str")
# take every distinct user id from cursor and get their details from TSAtweets and store to new db DistinctUser
for i in cursor:
    if i not  in already_exist:
        db.DistinctUser.insert(db.TSAtweets.find({"user.id_str": i},  {"user": 1, "_id": 0}))

print("total time :", round(clock()-start_time, 2), "seconds")
