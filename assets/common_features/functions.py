from assets.controller import * 
from assets.bot_actions.most_famous_tweet import *

def detect_control_c_signal_handler(sig, frame):
    
    checking = input(f'''Ctrl-c was pressed. Do you really want to exit ? ({bot_name} paused) - [y/n] ''')
    
    if checking == "y":
        logging.info(f'''{bot_name} has been stopped manually''')    
        return sys.exit(0)
    else:
        return ""  
     
def check_file_extension (path) : 
    
    response = requests.get(path)
    content_type = response.headers['content-type']
    extension = mimetypes.guess_extension(content_type)
    
    return extension

def iterate_over_a_the_first_case_of_a_double_list(_list) :
    
    _return = ""
    
    for l in _list: 
        if l[0] == "/hello" : 
            break
        _return += l[0]+"\n"
        
    return _return
    
def every_x_day_of_the_month_or_not():
    
    day_of_month = datetime.now().day
    
    if (day_of_month == 3) :
        logging.info("First day of the month - Calling most_famous_tweet_of_the_previous_month(\"favorite\")...")
        most_famous_tweet_of_the_previous_month("favorite")    
    elif (day_of_month == 4) :
        logging.info("First day of the month - Calling most_famous_tweet_of_the_previous_month(\"retweet\")...")
        most_famous_tweet_of_the_previous_month("retweet")
    else : 
        logging.info(f'''Today we are not the 1st || 2st day of the month ({str(day_of_month)}, so no scheduled actions will be executed.)''')
        
def count_meme_lgds_base (url='https://le-guide-du-secops.fr/lgds_memes_base/', ext='png', params={}):
    
    response = http_request_session.get(url, params=params)
    
    if response.ok:
        response_text = response.text
    else:
        return response.raise_for_status()
    
    soup = BeautifulSoup(response_text, 'html.parser')
    index_of_memes_png_list = ["https://le-guide-du-secops.fr"+node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]  
    
    lenght_of_list =  len(index_of_memes_png_list)
    logging.info("Number of items into lgds memes base "+str(today)+" : "+str(lenght_of_list)+"")
    return lenght_of_list
    
def is_meme_base_is_updated(): 

    lgds_meme_base = count_meme_lgds_base()
    _today = today.strftime("%m/%d/%Y")
    
    cursor.execute('''SELECT * FROM lgds_memes''')
    raws = cursor.fetchall()
    old_memes_count_lgds_base = raws[0][0]

    print (_today,lgds_meme_base)
    
    if lgds_meme_base != old_memes_count_lgds_base: 
        print ("updated ! ")
        cursor.execute(f"""DELETE FROM lgds_memes""")
        cursor.execute(f"""INSERT INTO lgds_memes(count,date) VALUES('{lgds_meme_base}','{_today}')""")
        sqliteConnection.commit()
        difference = lgds_meme_base - old_memes_count_lgds_base
        tweet = "La base de meme LGDS a été mise à jours ;-)\n"+str(lgds_meme_base)+" memes au compteur. ("+str(difference)+" en plus)"+bot_end_message # Faire la != entre l'ancienne valeur et la nouvelle.
        api.update_status(status=tweet)
        logging.info(f''' LGDS meme base () registered new meme(s) ({str(difference)}). TOTAL : {lgds_meme_base}''')
    else : 
        logging.info(f''' LGDS meme base () has not registered any new meme''')

def detect_if_website_is_down() :
    return 