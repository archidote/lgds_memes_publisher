from random import randrange
from assets.controller import * 


def select_random_article () : 
    
    response = http_request_session.get("https://le-guide-du-secops.fr/wp-json/wp/v2/posts/")
    
    wp_total_posts = int(response.headers["x-wp-total"])    
    wp_total_posts_random_magnitude = str(randrange(int(wp_total_posts)))

    response = http_request_session.get("https://le-guide-du-secops.fr/wp-json/wp/v2/posts?offset="+wp_total_posts_random_magnitude+"&per_page=1")
    data = response.json()
    logging.info(f'''Random article from lgds has been fetched {data[0]["link"]}''')
    
    return data[0]["link"]
    
    