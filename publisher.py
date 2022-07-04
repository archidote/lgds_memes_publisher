import tweepy
import os
from dotenv import load_dotenv
from datetime import datetime

# See tutorial: https://www.mattcrampton.com/blog/step_by_step_tutorial_to_post_to_twitter_using_python/

load_dotenv()

def publisher():
    
    twitter_auth_keys = {
        "consumer_key"        : os.getenv('consumer_key'),
        "consumer_secret"     : os.getenv('consumer_secret'),
        "access_token"        : os.getenv('access_token'),
        "access_token_secret" : os.getenv('access_token_secret')
    }

    auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
            )
    auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
            )
    api = tweepy.API(auth)

    tweet = "Bonjour le monde :-)"
    api.update_status(status=tweet)
   
    
publisher()