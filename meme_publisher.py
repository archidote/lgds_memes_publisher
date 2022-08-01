from more_itertools import random_permutation
from select_image import * 
from controller import * 


def img_publisher():
    
    reddit_or_my_own_memes_collection()
    media = api.media_upload("tmp_local_meme.jpg")

    emojis = ['🙂', '😀', '😃', '😆', '😉', '🐦', '😛', '😅']
    sentences = ['Bonjour à tous !', 'Salutations !', 'Hey !', 'Hello', 'Have a good day', 'Passez une bonne journée', 'Hi', 'Une image vaut mille mots - Confucius']

    random_emoji = random.randint(0, len(emojis) - 1)
    random_sentence = random.randint(0, len(sentences) - 1)
    
    tweet = sentences[random_sentence]+" "+emojis[random_emoji]+" #picoftheday"
    api.update_status(status=tweet, media_ids=[media.media_id])
