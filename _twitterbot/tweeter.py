import csv
import time
from collections import namedtuple

import tweepy as tweepy

import credentials

Tweet = namedtuple("Tweet", ['handle', 'url', 'score', 'content'])


auth = tweepy.OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth)


def get_tweets():
    reader = csv.reader(open('tweets.csv'))
    for handle, url, score, content in reader:
        yield Tweet(handle, url, score, content)


def send_tweets(tweets):
    for tweet in tweets:
        try:
            line = "%s - %s scores %s%% on ChatbotTech.io %s" % (
                tweet.content, tweet.handle, tweet.score, tweet.url
            )
            print(line)
            if line != '\n':
                api.update_status(line)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
        time.sleep(5)


if __name__ == "__main__":
    tweets = get_tweets()
    send_tweets(tweets)
