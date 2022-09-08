import requests 
from random import randrange


def select_random_article () : 
    
    response = requests.get("https://le-guide-du-secops.fr/wp-json/wp/v2/posts/")
    
    # wp_total_pages = int(response.headers["x-wp-totalpages"])
    wp_total_posts = int(response.headers["x-wp-total"])    
    wp_total_posts_random_magnitude = str(randrange(int(wp_total_posts)))

    response = requests.get("https://le-guide-du-secops.fr/wp-json/wp/v2/posts?offset="+wp_total_posts_random_magnitude+"&per_page=1")
    data = response.json()
    
    return data[0]["link"]
    
        
# print(select_random_article())