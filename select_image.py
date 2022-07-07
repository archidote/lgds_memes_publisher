from cherrypy import url
import requests
import random
from bs4 import BeautifulSoup


def sorted_index_of_by_file_ext(url='https://le-guide-du-secops.fr/lgds_memes_base/', ext='PNG', params={}):
    
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
    
    with open('tmp_local_meme.jpg', 'wb') as handler:
        handler.write(img_data)
        return 0; 
