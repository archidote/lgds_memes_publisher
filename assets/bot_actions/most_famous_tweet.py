from assets.controller import *

def most_famous_tweet_of_the_previous_month(choice) : # favorite || retweet
    
    fr_to_en = {"favorite": "favorisé", "retweet": "retweeté"}

    date = datetime.now()
    current_month = date.strftime('%m')
    previous_month = ""
    
    if current_month == "01" : # The prevous month of 01 is 12 not 0 :p 
        previous_month = 12 
    else : 
        previous_month = (int(current_month)) - 1
    
    array = []
    
    try :
        most_famous_tweet = api.user_timeline(screen_name = 'LeGuideDuSecOps', count = 150, include_rts = False, exclude_replies = True ) # Analyse the last 150 tweets of the account 
        for status in most_famous_tweet:
            date_trantyped = datetime.strptime(status._json["created_at"], '%a %b %d %H:%M:%S %z %Y')
            if date_trantyped.month == previous_month : 
                array.append([status._json[choice+"_count"], "https://twitter.com/"+twitter_user_account+"/status/"+status._json["id_str"]+""])   
        most_famous_tweet = max(array)
        tweet = "À ne pas manquer - Le tweet le plus "+fr_to_en[choice]+" ("+str(most_famous_tweet[0])+" fois) du mois précédent  :\n"+most_famous_tweet[1]+bot_end_message
            
        api.update_status(status=tweet)
        logging.info("The most "+choice+" tweet of the previous month has been republished with a formal message succefully. (tweet id : "+most_famous_tweet[1]+")")
        
    except (RuntimeError, TypeError, NameError, Exception) as e :
        
        logging.error("Fatal error : "+e+"")

