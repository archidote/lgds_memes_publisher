from assets.controller import * 

def whoami (twitter_username) : 
    

    data = api.get_user(screen_name=twitter_username)
    response = "Nom : "+data.name+" ("+data.screen_name+")\n"
    response += "Location : "+data.location+"\n"
    response += "Tweets : "+str(data.statuses_count)+"\n"
    response += "Tweets favorisés : "+str(data.favourites_count)+"\n"
    response += "Comptes que tu suis : "+str(data.friends_count)+"\n"
    response += "Followers : "+str(data.followers_count)+"\n"
    
    # TO-DO date de création du compte twitter 
    # comptes vérifié ou non ??? 
    return response