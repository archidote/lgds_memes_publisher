from assets.controller import * 
from assets.publisher.meme_publisher import * 
from assets.publisher.quote_publisher import * 
from assets.bot_actions.retweet import * 
from assets.bot_actions.whoami import * 
from assets.bot_actions.reply import *
from random import randint
from time import sleep


core_functions = {
        0 : lgds_memes_base,
        1 : count_meme_lgds_base,
        2 : every_x_day_of_the_month_or_not,
        3 : meme_from_reddit,
        4 : meme_from_reddit_title,

}

bot_functions = {
        1 : quote_publisher,
        2 : meme_publisher, 
        3 : lambda: whoami("LeGuideDuSecOps"),
        4 : lambda: most_famous_tweet_of_the_previous_month("retweet"),
        5 : lambda: most_famous_tweet_of_the_previous_month("favorite"),
        6 : bot_retweet,
        7 : detect_twitter_mention, 
        8 : is_meme_base_is_updated

}

def unit_tests (test) : 
    
    try: 
        if test == 0 : 
            print ("########## Core features ##########")
            for n in core_functions: 
                print ("Test N°"+str(n)+"\n")
                core_functions[n]()
                sleep(randint(5,10))
        else :
            print ("########## Bot features ##########")
            for n in bot_functions  : 
                print ("Test N°"+str(n)+"\n")
                bot_functions[n]()
                sleep(randint(10,100))
    except Exception as e : 
            print ("bot features tests failed : "+str(e))
            

def delete_tweets() : # Use with Caution !!!!!!!!

    date = '2023-01-24 15:00:00' # set the date and time of the tweet you want to delete  
    tweets = api.user_timeline(screen_name=twitter_user_account, count=5) # get tweets from the user timeline  
    for tweet in tweets:  
        if str(tweet.created_at) < str(date):
            api.destroy_status(tweet.id)