from time import clock
start_time = clock()
import pymongo
# import matplotlib.pyplot as plt

client = pymongo.MongoClient('localhost', 27017)
db = client.tsadb

language_code = {

}


cursor = db.TSAtweets.find({},{"lang":1, "_id":0})
language_list = []
for element in cursor:
    try:
        language_list.append(element['lang'])
    except:
        pass
print(len(language_list))
unique_language_list = set(language_list)
print(unique_language_list)

print("total time :",round(clock()-start_time,2),"seconds")