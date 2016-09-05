import pymongo

# pc games    -->  "#LeagueOfLegends", "#csgo", "#counterstrike", "#counterstrikeglobaloffensive",
# fb games    -->  "#CriminalCase", "#candycrush", "#farmheroessaga"
# mobile games-->  "#PokemonGO", "#COC","#candycrush"
client = pymongo.MongoClient('localhost', 27017)
db = client.tsadb
# total tweets
total_tweet = db.tweetsDemo.find().count()
print(total_tweet)
# irrelevant twit that does not contain any hashtag
irrelevent_tweet = db.tweetsDemo.find({'entities.hashtags': [ ]}).count()
print("Irrelevant : ",irrelevent_tweet)

# all hashtag in db
cursor = db.tweetsDemo.find({},{"entities.hashtags.text":1,"_id":0})
hashtags = []
for element in cursor:
    for t in element['entities']['hashtags']:
        hashtags.append(t['text'])

# print(hashtags)
st = set(hashtags)
# print(st)


leagueOfLegends = db.tweetsDemo.find({'entities.hashtags.text': {'$regex': 'LeagueOfLegends', '$options':'i'}}).count()
print("League of Legends: ",leagueOfLegends)
counterStrike = db.tweetsDemo.find(
    { "$or":
          [
              {'entities.hashtags.text': {'$regex': 'csgo', '$options':'i'}},
              {'entities.hashtags.text': {'$regex': 'counterstrike', '$options':'i'}},
              {'entities.hashtags.text': {'$regex': 'counterstrikeglobaloffensive', '$options':'i'}}
          ]
    }).count()
print("Counter Strike: ",counterStrike)
criminalCase = db.tweetsDemo.find({'entities.hashtags.text': {'$regex': 'CriminalCase', '$options':'i'}}).count()
print("Criminal Case: ",criminalCase)
candycrush = db.tweetsDemo.find({'entities.hashtags.text': {'$regex': 'candycrush', '$options':'i'}}).count()
print("candycrush: ",candycrush)
farmheroessaga = db.tweetsDemo.find({'entities.hashtags.text': {'$regex': 'farmheroessaga', '$options':'i'}}).count()
PokemonGO = db.tweetsDemo.find({'entities.hashtags.text': {'$regex': 'PokemonGO', '$options':'i'}}).count()
print("PokemonGO: ",PokemonGO)
COC = db.tweetsDemo.find({'entities.hashtags.text': {'$regex': 'COC', '$options':'i'}}).count()
print("COC: ",COC)
total = leagueOfLegends+counterStrike+criminalCase+candycrush+farmheroessaga+PokemonGO+COC+irrelevent_tweet
print("total related: ",total)


# plot graph about specific games related tweets
import matplotlib.pyplot as plt
import numpy as np
plt.rcdefaults()
x = np.array([leagueOfLegends,counterStrike,criminalCase,candycrush,farmheroessaga,PokemonGO,COC,irrelevent_tweet])
x = x/100
print(x)
fig, ax = plt.subplots()
objects = ('leagueOfLegends','counterStrike','criminalCase','candycrush','farmheroessaga','PokemonGO','COC','irrelevent_tweet')
y_pos = np.arange(len(objects))
bars = plt.bar(y_pos,x,align='center', alpha=.5,color='r')
#  print percentage in graph bar
for rect in bars:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2., 0.99*height,
            '%d' % int(height) + "%", ha='center', va='bottom')

plt.xticks(y_pos,objects, rotation = 40)
plt.ylabel("collected tweets * 100")
plt.title("Gamewise Tweets collection")
text = 'leagueOfLegends '+str(leagueOfLegends)+'\ncounterStrike '+str(counterStrike)+'\ncriminalCase '+str(criminalCase)\
       +'\ncandycrush '+str(candycrush)+'\nfarmheroessaga '+str(farmheroessaga)+'\nPokemonGO '+str(PokemonGO)\
       +'\nCOC '+str(COC)+'\nirrelevent_tweet '+str(irrelevent_tweet)
plt.text(0.1,45,text)
plt.grid(True)
plt.show()



# plot graph about platform specific games related tweets
x = np.array([leagueOfLegends+counterStrike+candycrush,criminalCase+candycrush+farmheroessaga,PokemonGO+COC+candycrush])
x = x/100
print(x)
fig, ax = plt.subplots()
objects = ('PC','Browser based', 'mobile')
y_pos = np.arange(len(objects))
bars = plt.bar(y_pos,x,align='center', alpha=.5,color='r')
#  print percentage in graph bar
for rect in bars:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2., 0.99*height,
            '%d' % int(height) + "%", ha='center', va='bottom')

plt.xticks(y_pos,objects, rotation = 40)
plt.ylabel("collected tweets * 100")
plt.title("Platform based Tweets collection")
text = 'PC    '+str(leagueOfLegends+counterStrike+candycrush)+'\nBrowser based  '\
    +str(criminalCase+candycrush+farmheroessaga)+'\nmobile  '+str(PokemonGO+COC+candycrush)
plt.text(0.1,45,text)
plt.grid(True)
plt.show()