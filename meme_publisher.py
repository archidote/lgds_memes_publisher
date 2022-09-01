from select_image import * 
from controller import * 


def meme_source_selectore_and_publish():
    
    emojis = ['🙂', '😀', '😃', '😆', '😉', '🐦', '😛', '😅']
    sentences = ['Bonjour à tous !', 'Salutations !', 'Hey !', 'Hello', 'Have a good day', 'Passez une bonne journée', 'Hi', 'Une image vaut mille mots - Confucius']
    random_emoji = random.randint(0, len(emojis) - 1)
    random_sentence = random.randint(0, len(sentences) - 1)   
        
    choice = random.choice([True, False])
    
    if choice == True :
        print ("LGDS Own meme base")
        lgds_memes_base()
        tweet = sentences[random_sentence]+" "+emojis[random_emoji]+" #picoftheday 🤖"
        
    else : 
        res = meme_from_reddit ()
        if res == "meme_from_reddit" : 
            print ("Reddit")
            reddit_post_title = meme_from_reddit_title()
            tweet = sentences[random_sentence]+" "+emojis[random_emoji]+" #picoftheday 🤖\nFrom @Reddit r/ProgrammerHumor \nPost title : "+reddit_post_title
        else : # The Reddit meme is a gif, so I force to use a classic sentence 
            tweet = sentences[random_sentence]+" "+emojis[random_emoji]+" #picoftheday 🤖"
            
    media = api.media_upload("tmp_local_meme") 
    api.update_status(status=tweet, media_ids=[media.media_id])
    