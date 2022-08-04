from select_image import * 
from controller import * 


def meme_publisher():
    
    choice = reddit_or_my_own_memes_collection()
    media = api.media_upload("tmp_local_meme.jpg")
    emojis = ['🙂', '😀', '😃', '😆', '😉', '🐦', '😛', '😅']
    sentences = ['Bonjour à tous !', 'Salutations !', 'Hey !', 'Hello', 'Have a good day', 'Passez une bonne journée', 'Hi', 'Une image vaut mille mots - Confucius']
    random_emoji = random.randint(0, len(emojis) - 1)
    random_sentence = random.randint(0, len(sentences) - 1)    
    
    if choice == True : # LGDS Own meme base 
        print ("LGDS Own meme base")
        tweet = sentences[random_sentence]+" "+emojis[random_emoji]+" #picoftheday 🤖"
        
    else : # Reddit 
        print ("Reddit")
        reddit_post_title = meme_from_reddit_title()
        tweet = sentences[random_sentence]+" "+emojis[random_emoji]+" #picoftheday 🤖\nFrom @Reddit r/ProgrammerHumor \nPost title : "+reddit_post_title
        
    api.update_status(status=tweet, media_ids=[media.media_id])
    