import tweepy
import sqlite3
import os
import sys 
import logging
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


######## Logging library  ###########

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler('assets/logs/logs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)


logger.addHandler(file_handler)
logger.addHandler(stdout_handler)

######### Bot end message #############

bot_end_message = "\n\n From LGDS bot 🤖 with ❤️"