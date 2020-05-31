import tweepy
import json
from api_operations import get_tweet, get_url_to_ss, get_imgur_client, post_tweet
from screenshot import get_png, get_embedded_tweet
import logging


class StreamListener(tweepy.StreamListener):

    def __init__(self, api):
        self.api = api

    def on_status(self, status):

        try:
            logging.info('received mention from @{}'.format(status.user.screen_name))

            id = status.id
            user = status.user.screen_name
            
            parent_tweet_id = status.in_reply_to_status_id
            parent_tweet = get_tweet(self.api, parent_tweet_id)
            parent_user = parent_tweet.user.screen_name

            ## get url from embedded version of tweet #
            url = get_url_to_ss(parent_tweet_id, parent_user)
            logging.info('embedded tweet url: {}'.format(url))

            tweet_html = get_embedded_tweet(url).json()['html']
            png = get_png(tweet_html)

            imgur_client = get_imgur_client()
            logging.info('uploading to imgur')
            imgur_url = imgur_client.upload_from_path('tweet.png')['link']
            logging.info('uploaded image with url: {}'.format(imgur_url))
            
            
            ans_tweet = post_tweet(self.api, user, imgur_url, id)
            logging.info('posted tweet with id: {}'.format(ans_tweet.id))
            


        except Exception as e:
            logging.error(e)
