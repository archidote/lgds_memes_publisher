import tweepy
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

######## Twitter API Creds #########

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

######## Twitter API Auth ##########

api = tweepy.API(auth)

######## Sqlit3 Connexion ###########

sqliteConnection = sqlite3.connect('assets/lgds_publisher.db', check_same_thread=False)
cursor = sqliteConnection.cursor()