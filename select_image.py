import requests
import random
from bs4 import BeautifulSoup

def reddit_or_my_own_memes_collection () :
    
    r = random.choice([True, False])
    if r == True :
        own_memes_base()
        return r 
    else : 
        meme_from_reddit ()
        return r

def own_memes_base(url='https://le-guide-du-secops.fr/lgds_memes_base/', ext='PNG', params={}):
    
    response = requests.get(url, params=params)
    if response.ok:
        response_text = response.text
    else:
        return response.raise_for_status()
    
    soup = BeautifulSoup(response_text, 'html.parser')
    parent = ["https://le-guide-du-secops.fr"+node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]  
    
    lenght_of_list =  len(parent)
    n = random.randint(0,lenght_of_list-1)
    img_data = requests.get(parent[n]).content
    
    print (parent[n])
    
    with open('tmp_local_meme.jpg', 'wb') as handler:
        handler.write(img_data)

def meme_from_reddit(): 
    url = "https://www.reddit.com/r/ProgrammerHumor/.json"

    resp = requests.get(url=url,headers = {'User-agent': 'lgds_publisher'})
    data = resp.json() 
    if "url_overridden_by_dest" in data["data"]["children"][1]["data"] : # if the post is a meme file, then :
        trendingRedditMeme = data["data"]["children"][1]["data"]["url_overridden_by_dest"]
        img_data = requests.get(trendingRedditMeme).content
        with open('tmp_local_meme.jpg', 'wb') as handler:
            handler.write(img_data)
    else : # use my own collection of memes
        own_memes_base()

def meme_from_reddit_title() : 
    url = "https://www.reddit.com/r/ProgrammerHumor/.json"
    resp = requests.get(url=url,headers = {'User-agent': 'lgds_publisher'})
    data = resp.json() 
    return data["data"]["children"][1]["data"]["title"]

