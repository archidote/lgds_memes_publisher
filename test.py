import requests

def meme_from_reddit(): 
    url = "https://www.reddit.com/r/ProgrammerHumor/new/.json"

    resp = requests.get(url=url,headers = {'User-agent': 'lgds_publisher'})
    data = resp.json() 
    print (data)
    
meme_from_reddit()