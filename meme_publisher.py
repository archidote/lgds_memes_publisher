import tweepy
import os
from dotenv import load_dotenv
from select_image import * 


load_dotenv()

def meme_publisher():
    
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

    sorted_index_of_by_file_ext()
    # Upload image
    media = api.media_upload("tmp_local_meme.jpg")

    # Post tweet with image
    tweet = ""
    api.update_status(status=tweet, media_ids=[media.media_id])


meme_publisher()