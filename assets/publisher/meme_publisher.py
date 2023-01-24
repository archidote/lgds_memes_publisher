from assets.common_features.select_image import * 
from assets.controller import * 

def meme_publisher():
    
    emojis = ['🙂', '😀', '😃', '😆', '😉', '🐦', '😛', '😅']
    sentences = ['Bonjour à tous !', 'Salutations !', 'Hey !', 'Hello', 'Have a good day', 'Passez une bonne journée', 'Hi', 'Une image vaut mille mots - Confucius']
    random_emoji = random.randint(0, len(emojis) - 1)
    random_sentence = random.randint(0, len(sentences) - 1)   
    
    choice = randrange(5) 
    if(choice <= 2) :
        lgds_memes_base()
        tweet = sentences[random_sentence]+" "+emojis[random_emoji]+" #picoftheday \nSource : LGDS memes base 🗃️"+bot_end_message
        logging.info("FROM meme_publisher() : Building the tweet... with the lgds meme downloaded previously.")
    else : 
        res = meme_from_reddit ()
        if res == "meme_from_reddit" : 
            reddit_post_title = meme_from_reddit_title()
            tweet = "Source : @Reddit r/ProgrammerHumor \n\nPost title : "+reddit_post_title+bot_end_message
            logging.info("FROM meme_publisher() : Building the tweet... with the reddit meme downloaded previously.")
        else : # The Reddit meme is a gif, so I force to use a classic sentence and use my own lgds meme base
            tweet = sentences[random_sentence]+" "+emojis[random_emoji]+" #picoftheday"+bot_end_message
    media = api.media_upload("assets/common_features/tmp_local_meme.png") 
    
    try: 
        api.update_status(status=tweet, media_ids=[media.media_id])
        logging.info("Tweet has been published succefully ! ")
    except Exception as e : 
        logging.info("meme_publisher() got an error during it execution :"+e)
