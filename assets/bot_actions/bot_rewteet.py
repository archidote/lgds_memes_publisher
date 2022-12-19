from assets.controller import * 
from datetime import datetime
def bot_retweet () : 

    search = '#cybersecurity'
    maxNumberOfTweets = 1
    
    for tweet in tweepy.Cursor(api.search_tweets, search,  result_type='recent').items(maxNumberOfTweets) :
        try:
            logging.info("I have a tweet from "+tweet.user.screen_name+" with the following"+search+"")
            tweet.retweet()
            logging.info("I have retweeted a tweet from "+tweet.user.screen_name+"")
        except tweepy.TweepError as e:
            print('Error: ' + e.args[0][0]['message'])

def most_retweeted_tweet_of_the_previous_month() : 
    
    most_retweeted_tweet_artefact = api.user_timeline(screen_name = 'LeGuideDuSecOps', count = 100, include_rts = False, exclude_replies = True )
    
    date = datetime.now()
    current_month = date.strftime('%m')
    previous_month = (int(current_month)) - 1
    array = []
    
    for status in most_retweeted_tweet_artefact:
        date_trantyped = datetime.strptime(status._json["created_at"], '%a %b %d %H:%M:%S %z %Y')
        if date_trantyped.month == previous_month : 
            for url in status._json["entities"]["urls"]:
                if "twitter.com" in url["expanded_url"] : 
                    array.append([status._json["retweet_count"], url["expanded_url"]])

    most_retweeted_tweet = max(array)
    tweet = "À ne pas manquer - Le tweet le plus retweeté ("+str(most_retweeted_tweet[0])+" fois) du mois précédent  :\n"+most_retweeted_tweet[1]+bot_end_message
    
    return api.update_status(status=tweet)