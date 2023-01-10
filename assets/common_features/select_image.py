from assets.common_features.functions import * 
from assets.controller import *
from bs4 import BeautifulSoup


def lgds_memes_base (url='https://le-guide-du-secops.fr/lgds_memes_base/', ext='png', params={}):
    
    response = http_request_session.get(url, params=params)
    
    if response.ok:
        response_text = response.text
    else:
        return response.raise_for_status()
    
    soup = BeautifulSoup(response_text, 'html.parser')
    index_of_memes_png_list = ["https://le-guide-du-secops.fr"+node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]  
    
    lenght_of_list =  len(index_of_memes_png_list)
    n = random.randint(0,lenght_of_list-1)
    img_data = http_request_session.get(index_of_memes_png_list[n]).content
    
    with open('assets/common_features/tmp_local_meme.png', 'wb') as handler:
        handler.write(img_data)
        logging.info(f'New meme from lgds memes base has been downloaded ({index_of_memes_png_list[n]})')

def meme_from_reddit(): 
    
    url = "https://www.reddit.com/r/ProgrammerHumor/.json"

    resp = http_request_session.get(url=url,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'})
    data = resp.json() 
    
    if "url_overridden_by_dest" in data["data"]["children"][1]["data"] : # if the post is a meme file, then :
        trendingRedditMeme = data["data"]["children"][1]["data"]["url_overridden_by_dest"]
        if check_file_extension(trendingRedditMeme) == ".gif" : 
            logging.info("meme is a gif from reddit, (incompatible) so I try to use a meme from my own collection")
            lgds_memes_base() 
        else :
            img_data = http_request_session.get(trendingRedditMeme).content
            with open('assets/common_features/tmp_local_meme.png', 'wb') as handler:
                if os.path.getsize('assets/common_features/tmp_local_meme.png') >= 5000000 : 
                    logging.warning("meme is > to 5 mo. I can't publish it because twitter aonly accept file which have a size < 5mo. I will try to use a meme from my own collection")
                else : 
                    handler.write(img_data)
                    logging.info('New meme from Reddit has been downloaded')
                    return "meme_from_reddit"
    else : # Use my own collection of memes
        lgds_memes_base()
        logging.info('Reddit top post isn\'t a meme, I will use the lgds_meme_base')

def meme_from_reddit_title() : 
    
    url = "https://www.reddit.com/r/ProgrammerHumor/.json"
    resp = http_request_session.get(url=url,headers = {'User-agent': 'lgds_publisher'})
    data = resp.json() 
    logging.info('Reddit fetched top post name')
    return data["data"]["children"][1]["data"]["title"]
