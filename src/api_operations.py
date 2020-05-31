import tweepy
from secrets import *
from imgurpython import ImgurClient

def get_twitter_api():
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api


def get_tweet(api, id):
    return api.get_status(id)

def get_url_to_ss(id, user):

    return 'https://publish.twitter.com/oembed?url=https://twitter.com/{user}/status/{id}&hide_thread=1'.format(user=user, id=id)

def post_tweet(api, user, imgur_url, id):
    return api.update_status('@{} {}'.format(user, imgur_url), in_reply_to_status_id=id)

def get_imgur_client():
    return ImgurClient(imgur_client_id, imgur_client_secret)