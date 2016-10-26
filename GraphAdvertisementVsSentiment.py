# http://stackoverflow.com/questions/24399820/expression-to-remove-url-links-from-twitter-tweet
import pymongo
from time import clock
start_time = clock()
import textblob
import matplotlib.pyplot as plt
from textblob.classifiers import NaiveBayesClassifier
import re

# train Naive Bayes Classifier with training data set
with open('training.csv', 'r') as f:
    cl = NaiveBayesClassifier(f, format='csv')
# import pickle     # pickle data to save time in case of running program next times
# with open('pickle_adVsSenti/cl.pkl','wb') as f:
#     pickle.dump(cl, f)

# with open('pickle_adVsSenti/cl.pkl','rb') as f:
#     cl = pickle.load(f)

client = pymongo.MongoClient('localhost', 27017)
db = client.tsadb
cursor = db.TSAtweets.find(
    {"$or":
          [
              {'lang': {'$regex': 'en', '$options': 'i'}},
              {'lang': {'$regex': 'en-gb', '$options': 'i'}},
          ]
     }, {"text": 1, "_id": 0})

data = {
    'advertisement': 0,
    'sentiment': 0,
}
count = 0
errors = 0
for tweet in cursor:
    try:
        result = re.sub(r"http\S+", "", tweet['text'])
        res = cl.classify(result)       # classify text
        res = res.strip().lower()       # strip spaces and get to lower case
        data[res] += 1                  # increment count for related tweet
        count += 1
    except:
        errors += 1
# print(data)
# print(count,errors)

########################################################################################################################
# code snippet 2: plot percentage of advertisement vs. sentiment

df = {
    'type': ['Sentiment', 'Advertisement'],
    'count': [data['sentiment'], data['advertisement']],    # user count
}
# print(df)
total_user = data['sentiment']+data['advertisement']
print("Total user:",total_user)
# Create a figure with a single subplot
f, ax = plt.subplots(1, figsize=(10,5))
# Set bar width at 1
bar_width = 1
# positions of the left bar-boundaries
bar_l = [i for i in range(len(df['count']))]
# positions of the x-axis ticks (center of the bars as bar labels)
tick_pos = [i+(bar_width/2) for i in bar_l]
# Create the percentage of the total score the percentage value for each participant was
percentage = [(i / total_user) * 100 for i in df['count']]
# add percentage with names
for i in range(len(percentage)):
    tmp = df['type'][i]
    tmp = tmp+'  '+"%.2f" % percentage[i]+'%'
    df['type'][i] = tmp

# Create a bar chart in position bar_1
ax.bar(bar_l,
       # using percentage data
       percentage,
       # labeled
       label='Pre Score',
       # with alpha
       alpha=0.9,
       # with color
       color='#019600',
       # with bar width
       width=bar_width,
       # with border color
       edgecolor='white'
       )
# Set the ticks to be first names
plt.xticks(tick_pos, df['type'])
ax.set_ylabel("Percentage")
# ax.set_xlabel("")
plt.title('Sentiment VS. Advertisement')
# Let the borders of the graphic
plt.xlim([min(tick_pos)-bar_width, max(tick_pos)+bar_width])
plt.ylim(0, 100)
# rotate axis labels
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
# shot plot
plt.show()

########################################################################################################################
# print("total graph time :",round(clock()-start_time,2),"seconds")