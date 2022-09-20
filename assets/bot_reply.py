from assets.articles import select_random_article
from assets.controller import * 
from assets.meme_publisher import * 
from assets.quote_publisher import * 


def detect_twitter_mention () : 
    
        bot_id = int(api.verify_credentials().id_str)
        words = [["/article", "Hello 😊 @{} Voici un article tiré au sort rien que pour toi \n "+select_random_article()+""+bot_end_message], 
                ["/info", "Hello 😊 @{} Pour toutes informations, envois nous un MP (message privé) 😊"], 
                ["/meme", "Hello 😊 @{} voici un meme tiré au sort rien que pour toi"+bot_end_message+""]]
        
        mentions = api.mentions_timeline() # Finding mention tweets

        i = 0 
        
        for mention in mentions:
        
            with open('assets/last_tweet_mention_id') as f:
                previous_tweet_id = f.readlines()
                print (previous_tweet_id[0])
                    
            if previous_tweet_id[0] != str(mention.id) : # compare str to str. otherwise python cannot find any != between the two value 
                if mention.in_reply_to_status_id is None and mention.author.id != bot_id:
                    if (mention.favorited) != True : # If the tweet has been already favorited, then : 
                        api.create_favorite(mention.id)
                        logging.info('tweet '+str(mention.id)+' was favorited')
                    for word in words : 
                        if word[0] in mention.text :
                            tries = 3
                            for trie in range(tries):
                                try:
                                    if word[0] == "/meme" : 
                                        message = word[1]
                                        meme_source_selectore_and_publish()
                                        media = api.media_upload("assets/tmp_local_meme.JPG") 
                                        api.update_status(message.format(mention.author.screen_name), in_reply_to_status_id=mention.id_str, media_ids=[media.media_id])
                                        logging.info('meme has been fetched and published in the reply of the following tweet : '+str(mention.id))
                                        break
                                    else : # /info /article 
                                        message = word[1]
                                        api.update_status(message.format(mention.author.screen_name), in_reply_to_status_id=mention.id_str)
                                        logging.info('action '+word[0]+' was published in the reply of the following tweet : '+str(mention.id))
                                        break
                                except Exception as exc:
                                    if trie < tries - 1 :
                                        logging.warning('Received invalid answer from Twitter. ({exc}) back off for 10 minutes: ')
                                        time.sleep(10*60) # Wait 10 minutes before the other tries 
                                        continue 
                                    else : 
                                        raise 
        
                    with open('assets/last_tweet_mention_id', 'w') as f:
                        f.write(str(mention.id))
                        logging.info(str(mention.id)+' has been written to the file assets/last_tweet_mention_id')
            else : 
                logging.info('W: Same previous tweet id ('+str(mention.id)+'), I can\'t reply twice to the same tweet"')
                    
            i = i + 1 
            if i == 1 : 
                break