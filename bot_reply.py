from controller import * 
from meme_publisher import * 
from quote_publisher import * 


def detect_twitter_mention () : 
    
    bot_id = int(api.verify_credentials().id_str)
    words = ["/article", "/info", "/meme"]
    message = "If you have any questions, feel free to send us a DM @{}"
    
    mentions = api.mentions_timeline() # Finding mention tweets

    i = 0 
    for mention in mentions:
        print (mention.text)
        print (mention.id)
        with open('last_tweet_mention_id') as f:
            previous_tweet_id = f.readlines()
            print (previous_tweet_id[0])
        
        if previous_tweet_id[0] != str(mention.id) : # compare str to str. otherwise python cannot find any != between the two value 
            if mention.in_reply_to_status_id is None and mention.author.id != bot_id:
                if True in [word in mention.text.lower() for word in words]:
                    try:
                        print("Attempting to reply...")
                        api.update_status(message.format(mention.author.screen_name), in_reply_to_status_id=mention.id_str)
                        print("Successfully replied :)")
                        with open('last_tweet_mention_id', 'w') as f:
                            f.write(str(mention.id))
                    except Exception as exc:
                        print(exc)
        else : 
            print ("W: Same previous tweet id, I can't reply the same things two times to a user !")
            
        i = i + 1 
        if i == 1 : 
            break

# detect_twitter_mention()