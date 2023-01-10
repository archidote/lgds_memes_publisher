from assets.controller import * 

def bot_retweet () : 

    search = '#cybersecurite'
    maxNumberOfTweets = 1
    
    for tweet in tweepy.Cursor(api.search_tweets, search,  result_type='recent').items(maxNumberOfTweets) :
        try:
            logging.info("I have a tweet from "+tweet.user.screen_name+" with the following hashtag : "+search+"")
            tweet.retweet()
            logging.info("I have retweeted a tweet from "+tweet.user.screen_name+"")
        except (RuntimeError, TypeError, NameError, Exception) as e :
            logging.error("Fatal error (auto retweet feature) : "+e+"")
