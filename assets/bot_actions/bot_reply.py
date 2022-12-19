from assets.common_features.articles import select_random_article
from assets.controller import * 
from assets.publisher.meme_publisher import * 
from assets.publisher.quote_publisher import *
from assets.bot_actions.whoami import * 


def detect_twitter_mention () : 
        
        mentions = api.mentions_timeline() # Finding mention(s) tweets 
        logging.info('Twitter API fetching for new mention')
                      
        i = 0 
        for mention in mentions:
            
            bot_id = int(api.verify_credentials().id_str)
            
            words = [["/article", "Hello 😊 @{} Voici un article tiré au sort rien que pour toi \n "+select_random_article()+""+bot_end_message], 
                    ["/info", "Hello 😊 @{} Pour toutes informations, envois nous un MP (message privé) 😊"], 
                    ["/meme", "Hello 😊 @{} voici un meme tiré au sort rien que pour toi"+bot_end_message+""],
                    ["/whoami", "Hello 😊 @{} voici quelques informations à propos de toi :\n"+whoami(mention.author.screen_name)+""+bot_end_message+""],
                    ["/hello", "Hey 😊 @{} Voici les actions que je suis capable de réaliser : \n"]]
        
            with open('assets/bot_actions/last_tweet_mention_id') as f:
                previous_tweet_id = f.readlines()
                    
            if previous_tweet_id[0] != str(mention.id) : # compare str to str. otherwise python cannot find any != between the two value 
                if mention.in_reply_to_status_id is None and mention.author.id != bot_id:
                    if (mention.favorited) != True : # If the tweet has been already favorited, then : 
                        api.create_favorite(mention.id)
                        logging.info('tweet '+str(mention.id)+' was favorited')
                        
                    for word in words : 
                        if word[0] in mention.text :
                            message = word[1]
                            if word[0] == "/meme" : 
                                meme_source_and_publish(bot_anwser=True)
                                media = api.media_upload("assets/common_features/tmp_local_meme.JPG") 
                                api.update_status(message.format(mention.author.screen_name), in_reply_to_status_id=mention.id_str, media_ids=[media.media_id])
                                logging.info('meme has been fetched and published in the reply of the following tweet : '+str(mention.id))
                            elif word[0] == "/hello":
                                message += ""+iterate_over_a_the_first_case_of_a_double_list(words)+""+bot_end_message
                                api.update_status(message.format(mention.author.screen_name), in_reply_to_status_id=mention.id_str)
                            else : # /info /article /whoami
                                api.update_status(message.format(mention.author.screen_name), in_reply_to_status_id=mention.id_str)
                                logging.info('action '+word[0]+' was published in the reply of the following tweet : '+str(mention.id))
        
                    with open('assets/bot_actions/last_tweet_mention_id', 'w') as f:
                        f.write(str(mention.id))
                        logging.info(str(mention.id)+' has been written to the file assets/bot_actions/last_tweet_mention_id')
            else : 
                logging.info('W: Same previous tweet id ('+str(mention.id)+'), I can\'t reply twice to the same tweet"')
                    
            i = i + 1 
            if i == 1 : 
                break