import pymongo
time_zone_list = []

client = pymongo.MongoClient('localhost', 27017)
db = client.tsadb
tweets = db.tweetsDemo.find({},{"user.time_zone":1,"_id":0})
for t in tweets:
    print(t)
    time_zone_list.append(t["user"]['time_zone'])
# total time zone
print(time_zone_list)
print(len(time_zone_list))
# unique time zone
unique_time_zone_list = set(time_zone_list)
print(unique_time_zone_list)
print(len(unique_time_zone_list))
# count time zone status
dict_of_time_zone = dict.fromkeys(unique_time_zone_list,0)
print(dict_of_time_zone)
for t_z in time_zone_list:
    dict_of_time_zone[t_z] += 1;

print(dict_of_time_zone)

# plot graph
# import matplotlib.pyplot as plt
# plt.bar(range(len(dict_of_time_zone)),dict_of_time_zone.values(), align = 'center')
# plt.xticks(range(len(dict_of_time_zone)), list(dict_of_time_zone.keys()))
# plt.show()


