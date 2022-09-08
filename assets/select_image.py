import requests
import random
from assets.functions import * 
from assets.controller import *
from bs4 import BeautifulSoup

def lgds_memes_base (url='https://le-guide-du-secops.fr/lgds_memes_base/', ext='PNG', params={}):
    
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
    
    with open('assets/tmp_local_meme', 'wb') as handler:
        handler.write(img_data)
        logging.info('New meme from lgds memes base has been downloaded')

def meme_from_reddit(): 
    url = "https://www.reddit.com/r/ProgrammerHumor/.json"

    resp = requests.get(url=url,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'})
    data = resp.json() 
    if "url_overridden_by_dest" in data["data"]["children"][1]["data"] : # if the post is a meme file, then :
        trendingRedditMeme = data["data"]["children"][1]["data"]["url_overridden_by_dest"]
        if check_file_extension(trendingRedditMeme) == ".gif" : 
            print ("meme is a gif from reddit, (incompatible) so I try to use a meme from my own collection")
            lgds_memes_base() 
        else :
            img_data = requests.get(trendingRedditMeme).content
            with open('assets/tmp_local_meme', 'wb') as handler:
                handler.write(img_data)
                logging.info('New meme from Reddit has been downloaded')
                return "meme_from_reddit"
    else : # use my own collection of memes
        lgds_memes_base()
        logging.info('Reddit top post isn\'t a meme, I will use the lgds_meme_base')

def meme_from_reddit_title() : 
    url = "https://www.reddit.com/r/ProgrammerHumor/.json"
    resp = requests.get(url=url,headers = {'User-agent': 'lgds_publisher'})
    data = resp.json() 
    return data["data"]["children"][1]["data"]["title"]

