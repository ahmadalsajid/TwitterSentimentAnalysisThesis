from pymongo import MongoClient
import json
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from Key import *
from GameCategory import *

class MyListener(StreamListener):

    def on_data(self, raw_data):
        try:
            '''here we will collect data and store thm in mongodb'''
            client = MongoClient('localhost', 27017)
            db = client.tsadb
            tweet = json.loads(raw_data)
            db.tweetstest.insert(tweet)
            print('data inserted')

            return True
        except:
            print('exception occurred\n\n')       # debug to test if on_data() working or not
            return True

    def on_error(self, status_code):
        return True


def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitter_stream = Stream(auth, MyListener())
    # taking hashtag list from GameCategory.py
    twitter_stream.filter(track=all_hashtags)


if __name__ == '__main__':
    main()
