from pymongo import MongoClient
import json
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener


# Consumer keys and access tokens, used for OAuth
consumer_key = 'cPWTw5c40SX6Iu9XeJuW4NIoI'
consumer_secret = 'L79cBaSIrBAV16iJcslbTuttZMYmJvZHaq24LkBKJhKS1e7yl6'
access_token = '738404396321538049-lJ9WtMNL66vsmacMOHJQ8uNdrRvZaFV'
access_token_secret = 'cH8kBtLIEdG52E1NM8EVZTeLfLUysRuB5XPmN7XMn0bQt'


class MyListener(StreamListener):

    def on_data(self, raw_data):
        try:
            '''here we will collect data and store thm in mongodb'''
            client = MongoClient('localhost', 27017)
            db = client.tsadb
            tweet = json.loads(raw_data)
            db.tweets.insert(tweet)
            print('data inserted')

            return True
        except:
            print('exception occurred\n\n')       # debug to test if on_data() working or not
            return True

    def on_error(self, status_code):
        return True


def main():
    # track_list = [str(x) for x in input("enter topics about you want to do a Sentiment analysis : ").split()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitter_stream = Stream(auth, MyListener())
    # filter can be modified to get necessary data
    """
    # pc games    -->  "#LeagueOfLegends", "#csgo", "#counterstrike", "#counterstrikeglobaloffensive",
    # fb games    -->  "#CriminalCase", "#candycrush", "#farmheroessaga"
    # mobile games-->  "#PokemonGO", "#COC","#candycrush"
    """
    track_list = ["#PokemonGO", "#COC", "#LeagueOfLegends", "#csgo", "#counterstrike", "#counterstrikeglobaloffensive",
                  "#CriminalCase", "#candycrush", "#8ballpool", "#farmheroessaga"]
    twitter_stream.filter(track=track_list)


if __name__ == '__main__':
    main()
