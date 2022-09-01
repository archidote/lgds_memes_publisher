from articles import select_random_article
from controller import * 
from meme_publisher import * 
from quote_publisher import * 


def detect_twitter_mention () : 
    
    bot_id = int(api.verify_credentials().id_str)
    words = [["/article", "Hello 😊 @{} Voici un article tiré au sort rien que pour toi \n "+select_random_article()+" \n From LGDS bot with love 🤖"], 
             ["/info", "Hello 😊 @{} Pour toutes informations, envois nous un MP (message privé) 😊"], 
             ["/meme", "Hello 😊 @{} voici un meme tiré au sort rien que pour toi"]]
       
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
                for word in words : 
                    if word[0] in mention.text :
                        try:
                            if word[0] == "/meme" : 
                                message = word[1]
                                media = api.media_upload("tmp_local_meme") 
                                api.update_status(message.format(mention.author.screen_name), in_reply_to_status_id=mention.id_str, media_ids=[media.media_id])
                            else : 
                                print("Attempting to reply...")
                                print (mention.text)
                                print (word[1])
                                message = word[1]
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

detect_twitter_mention()