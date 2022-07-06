from controller import * 
from datetime import datetime

def publisher():

    tweet = "Bonjour le monde :-)"
    api.update_status(status=tweet)
    
publisher()