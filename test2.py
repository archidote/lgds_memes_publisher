from bs4 import BeautifulSoup
import requests

url = 'https://le-guide-du-secops.fr/lgds_memes_base'
ext = 'JPG'

def listFD(url, ext=''):
    page = requests.get(url).text
    print (page)
    soup = BeautifulSoup(page, 'html.parser')
    # print soup.find_all('a')
    for node in soup.find_all('a'): 
        if node.get('href').endswith(ext):
            return node 
print (listFD(url,ext))
