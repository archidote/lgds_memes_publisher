from assets.controller import * 



def check_file_extension (path) : 
    response = requests.get(path)
    content_type = response.headers['content-type']
    extension = mimetypes.guess_extension(content_type)
    return extension

def twitter_api_random_fetch_in_secondes () : 
    random_in_sec = random.randint(15, 30)
    print (random_in_sec)
    return random_in_sec