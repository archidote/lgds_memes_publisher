import time
from unittest import result 
from assets.articles import select_random_article
from assets.controller import * 
from assets.meme_publisher import * 
from assets.quote_publisher import * 


def bot_retweet () : 
    
   
    search = '#cyber'
    
    maxNumberOfTweets = 1
    
    for tweet in tweepy.Cursor(api.search_tweets, search,  result_type='recent').items(maxNumberOfTweets) :
        try:
            print('Found tweet by @' + tweet.user.screen_name)

            #Publishing retweet
            tweet.retweet()
            print ('retweeted !')

        except tweepy.TweepError as e:
            print('Error: ' + e.args[0][0]['message'])
        except StopIteration:
            break
