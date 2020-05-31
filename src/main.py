import tweepy
from secrets import *
from stream import StreamListener
from api_operations import get_twitter_api, get_tweet
from screenshot import get_png
import logging

logging.basicConfig(level = logging.INFO)


def main():


    ## get authenticated twitter api ##
    twitter_api = get_twitter_api()

    ## instantiate listener from stream api ##
    mention_listener = StreamListener(twitter_api)

    ##  start stream and track mentions to @ss_this_tweet ##
    
    stream = tweepy.Stream(auth=twitter_api.auth, listener=mention_listener)
    stream.filter(track=['ss_this_tweet'], is_async=True)
    logging.info('started tracking user mentions')


if __name__ == '__main__':
    main()
