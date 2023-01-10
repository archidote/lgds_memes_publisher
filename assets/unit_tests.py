from assets.controller import * 
from assets.publisher.meme_publisher import * 
from assets.publisher.quote_publisher import * 
from assets.bot_actions.retweet import * 
from assets.bot_actions.whoami import * 
from assets.bot_actions.reply import *
from random import randint
from time import sleep

# README : Please call theses two function from the "root" project"
# Just create a python.py file and paste the following 3 lines of code 
# from assets.unit_tests import * 
# core_features_tests()
# bot_features_tests() 

def core_features_tests() :
    
    print ("Core feature tests...")
    try: 
        every_x_day_of_the_month_or_not() 
        meme_from_reddit()
        meme_from_reddit_title()
        lgds_memes_base()
        
    except Exception as e : 
        print ("core features test failed "+e)

def bot_features_tests() :

    bot_functions = {0 : meme_publisher, 
           1 : quote_publisher,
           2 : lambda: whoami("LeGuideDuSecOps"),
           3 : lambda: most_famous_tweet_of_the_previous_month("retweet"),
           4 : lambda: most_famous_tweet_of_the_previous_month("favorite"),
           5 : bot_retweet,
           6 : detect_twitter_mention, 

    }

    try: 
        for n in bot_functions  : 
            print ("Test N°"+n+"")
            bot_functions[n]()
            sleep(randint(10,100))
    except Exception as e : 
         print ("bot features tests failed : "+e)