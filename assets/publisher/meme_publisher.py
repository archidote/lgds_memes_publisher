from assets.common_features.select_image import * 
from assets.controller import * 

def meme_source_and_publish(bot_anwser=False):
    
    emojis = ['🙂', '😀', '😃', '😆', '😉', '🐦', '😛', '😅']
    sentences = ['Bonjour à tous !', 'Salutations !', 'Hey !', 'Hello', 'Have a good day', 'Passez une bonne journée', 'Hi', 'Une image vaut mille mots - Confucius']
    random_emoji = random.randint(0, len(emojis) - 1)
    random_sentence = random.randint(0, len(sentences) - 1)   
    
    if bot_anwser == False : 

            
        choice = randrange(5) 
        if(choice <= 2) :
            logging.info("A new meme has been downloaded from le-guide-du-secops.fr/lgds_meme_base")
            lgds_memes_base()
            tweet = sentences[random_sentence]+" "+emojis[random_emoji]+" #picoftheday \nSource : LGDS memes base 🗃️"+bot_end_message
            
        else : 
            res = meme_from_reddit ()
            if res == "meme_from_reddit" : 
                logging.info("A new meme has been downloaded from r/ProgrammerHumor")
                reddit_post_title = meme_from_reddit_title()
                tweet = "Source : @Reddit r/ProgrammerHumor \n\nPost title : "+reddit_post_title+bot_end_message
            else : # The Reddit meme is a gif, so I force to use a classic sentence and use my own lgds meme base
                tweet = sentences[random_sentence]+" "+emojis[random_emoji]+" #picoftheday"+bot_end_message
                
        media = api.media_upload("assets/common_features/tmp_local_meme.png") 
        api.update_status(status=tweet, media_ids=[media.media_id])
        
    else : 
        
        logging.info("A new meme has been downloaded from le-guide-du-secops.fr/lgds_meme_base in reply of the user's order (/meme)")
        lgds_memes_base()
        tweet = sentences[random_sentence]+" "+emojis[random_emoji]+" #picoftheday "+bot_end_message+" Source : LGDS memes base 🗃️"